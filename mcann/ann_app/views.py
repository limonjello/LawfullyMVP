# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from forms import LoginForm, RegisterForm

from django import template
from annotator import settings

register = template.Library()

@register.filter
def check_login(request):
    if request.user.is_authenticated():
        return True
    else:
        return False

def do_login(request, template_name=None, **kwargs) :
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        login(request, user)
        return redirect(settings.SUB_URL+"/ann/")
    context = {}
    request_context = RequestContext(request)
    return render_to_response('signin.html', context_instance=RequestContext(request))
###z
#def do_login(request, template_name=None, **kwargs):
    #next = request.GET.get('next', None)
    #if request.method == 'POST':
        #form = LoginForm(request.POST)
        #if form.is_valid():
            #user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            #login(request, user)
            #if next is None:
                #next = '/ann/'

            #return redirect(next)
    #else:
    #    form = LoginForm()
    #ctxt = {}
    #ctxt['next'] = next
    #ctxt['login_form'] = form
    #ctxt['form'] = RegisterForm()
    #return render(request, template_name, ctxt)
    #return render_to_response('signin.html',context_instance=RequestContext(request));
###
def home(request):
    context = {'ishomepage': True};
    return render_to_response('index.html', context, context_instance=RequestContext(request));

def index(request):
    return redirect(settings.SUB_URL+'/ann/');

def aboutus(request):
    return render_to_response('aboutus.html',context_instance=RequestContext(request));

def blogpost(request):
    return render_to_response('blog-post.html',context_instance=RequestContext(request));

def blog(request):
    return render_to_response('blog.html',context_instance=RequestContext(request));

def comingsoon(request):
    return render_to_response('coming-soon.html',context_instance=RequestContext(request));

def contact(request):
    return render_to_response('contact.html',context_instance=RequestContext(request));

def faq(request):
    return render_to_response('faq.html',context_instance=RequestContext(request));

def features(request):
    return render_to_response('features.html',context_instance=RequestContext(request));

def portfolio(request):
    return render_to_response('portfolio.html',context_instance=RequestContext(request));

def pricing(request):
    return render_to_response('pricing.html',context_instance=RequestContext(request));

def reset(request):
    return render_to_response('reset.html',context_instance=RequestContext(request));

def signin(request):
    return render_to_response('signin.html',context_instance=RequestContext(request));

def signup(request):
    return render_to_response('signup.html',context_instance=RequestContext(request));
def profile(request):
    return render_to_response('profile.html',context_instance=RequestContext(request));

def template(request):
    ctxt = {};
    ctxt['currentUrl'] = request.get_full_path();
    if request.user.is_authenticated():
        ctxt['is_auth'] = True;

    return render_to_response('annotator-template.html', ctxt, context_instance=RequestContext(request));
