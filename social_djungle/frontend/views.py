# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

def index(request):
    if (not request.session.get('id', False)):
        request.session.set_test_cookie()
        t = get_template('index.html')
        context = {}
        if (request.session.get('regError', False)):
            del request.session['regError']
            context.update({ 'regError': 'Los datos de entrada no son válidos.' })
        if (request.session.get('newUser', False)):
            del request.session['newUser']
            context.update({ 'newUser': 'El usuario ha sido creado satisfactoriamente.'})
        c = RequestContext(request, context)
        return HttpResponse(t.render(c))
    else:
        return HttpResponseRedirect('/user/home')
"""
def profile(request):
    return render_to_response('profile.html')

def home(request):
    return render_to_response('home.html')
"""
def getURL(request, path):
    try:
        t = get_template('%s.html' % str(path))
    except:
        raise Http404
    else:
        c = RequestContext(request, {})
        return HttpResponse(t.render(c))
    

