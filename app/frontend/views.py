from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime, logging

logger = logging.getLogger(__name__)
# def error_400(request, exception):
#     logger.error("Error 400: [%s]"%(exception))
#     return render(request, '400.html', {}, status=400)
#
# def error_404(request, exception):
#     logger.error("Error 404: [%s]"%(exception))
#     return render(request, '404.html', {}, status=404)
#
# def error_403(request, exception):
#     logger.error("Error 403: [%s]"%(exception))
#     return render(request, '403.html', {}, status=403)
#
# def error_500(request):
#     return render(request, '500.html', {}, status=500)

class Index(LoginRequiredMixin, View):
    template = 'index.html'

    def get(self, request):
        return HttpResponseRedirect(reverse_lazy('home'))

class Home(LoginRequiredMixin, View):
    template = 'examples/dashboard.html'

    def get(self, request):
        return render(request, self.template)

class User(LoginRequiredMixin, View):
    template = 'examples/user.html'

    def get(self, request):
        return render(request, self.template)

class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')
