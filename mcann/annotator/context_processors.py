import settings # import the settings file

def admin_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'SUB_URL': settings.SUB_URL, 'STATIC_URL': settings.STATIC_URL}