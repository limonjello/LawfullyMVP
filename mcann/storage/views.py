from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import *
from django.utils import simplejson

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from baseview import BaseView

from django import template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from storage import models

initialInfo = {
    'message': "Annotator Store API",
    'links': {
        'annotation': {
            'create': {
                'method': 'POST',
                'url': '/storage/create',
                'query': {
                    'refresh': {
                        'type': 'bool',
                        'desc': "Force an index refresh after create (default: true)"
                    }
                },
                'desc': "Create a new annotation"
            },
            'read': {
                'method': 'GET',
                'url': '/read/:id',
                'desc': "Get an existing annotation"
            },
            'update': {
                'method': 'PUT',
                'url': '/update/:id',
                'query': {
                    'refresh': {
                        'type': 'bool',
                        'desc': "Force an index refresh after update (default: true)"
                    }
                },
                'desc': "Update an existing annotation"
            },
            'delete': {
                'method': 'DELETE',
                'url': '/delete/:id',
                'desc': "Delete an annotation"
            }
        },
        'search': {
            'method': 'GET',
            'url': '/search',
            'desc': 'Basic search API'
        },
        'search_raw': {
            'method': 'GET/POST',
            'url': '/search_raw',
            'desc': 'Advanced search API -- direct access to ElasticSearch. Uses the same API as the ElasticSearch query endpoint.'
        }
    }
}
@csrf_exempt
def index(request):
    return HttpResponse(simplejson.dumps(initialInfo), mimetype='application/json')

@csrf_exempt
def create(request):
    if request.user.is_authenticated():
        param = ''
        for key in request.POST:
            param = key

        jsonParam = simplejson.loads(param)
        ann = models.Anndata.objects.create(
            user_id = request.user.id,
            permissions = simplejson.dumps(jsonParam['permissions']),
            text = jsonParam['text'],
            tags = simplejson.dumps(jsonParam['tags']),
            ranges = simplejson.dumps(jsonParam['ranges']),
            quote = simplejson.dumps(jsonParam['quote']),
            uri = simplejson.dumps(jsonParam['uri'])
        )
        ann.save()
        return HttpResponse(simplejson.dumps({'id':ann.id}), mimetype='application/json')
    else :
        return HttpResponse(simplejson.dumps({'code': 404,'message': 'Not authenticated'}), mimetype='application/json')
@csrf_exempt
def read(request):
    request_id = request.POST['id']
    results = models.Anndata.objects.filter(id=request_id)
    return HttpResponse(simplejson.dumps(results), mimetype='application/json')

@csrf_exempt
def update(request, ann_id):
    if request.user.is_authenticated():
        if request.method == 'PUT':
            jsonParam = simplejson.loads(request.body)
            selected_ann = models.Anndata.objects.get(id=ann_id)
            selected_ann.text = jsonParam['text']
            selected_ann.tags = jsonParam['tags']
            selected_ann.ranges = simplejson.dumps(jsonParam['ranges'])
            selected_ann.quote = "\"" + jsonParam['quote'] + "\""
            selected_ann.uri = "\"" + jsonParam['uri'] + "\""
            selected_ann.save()
            return HttpResponse(simplejson.dumps({'id':selected_ann.id}), mimetype='application/json')
        else :
            return HttpResponse(simplejson.dumps({'code': 404,'message': 'Not authenticated'}), mimetype='application/json')
    else :
        return HttpResponse(simplejson.dumps({'code': 404,'message': 'Not authenticated'}), mimetype='application/json')

@csrf_exempt
def delete(request, ann_id):
    if request.user.is_authenticated():
        if request.method == 'DELETE':
            selected_ann = models.Anndata.objects.get(id=ann_id)
            selected_ann.delete()
            return HttpResponse('', mimetype='text/plain')
        else :
            return HttpResponse(simplejson.dumps({'code': 404,'message': 'Not authenticated'}), mimetype='application/json')
    else:
        return HttpResponse(simplejson.dumps(initialInfo), mimetype='application/json')

@csrf_exempt
def search(request):
    cnt = models.Anndata.objects.all().count()
    result = []
    for e in models.Anndata.objects.all():
        result.append({'id': e.id,
                       'permissions': simplejson.loads(e.permissions),
                       'text': e.text,
                       'tags': simplejson.loads(e.tags),
                       'ranges': simplejson.loads(e.ranges),
                       'quote': e.quote,
                       'uri': e.uri
        });

    return HttpResponse(simplejson.dumps({'total': cnt, 'rows': result}), mimetype='application/json')

@csrf_exempt
def searchraw(request):
    return HttpResponse(simplejson.dumps(initialInfo), mimetype='application/json')
