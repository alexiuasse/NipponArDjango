from django.conf import settings # import the settings file

def enterprise_name(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'NAME_OF_ENTERPRISE': settings.NAME_OF_ENTERPRISE}
