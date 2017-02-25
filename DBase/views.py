# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth
from DBase.models import DBase
from django.template import RequestContext
from django.template import RequestContext
from django.utils import dateformat
import datetime

def res(request):
    errors = []
    if request.method == 'POST':
        if 'number' in request.POST:
            number = request.POST['number']
        if 'oper' in request.POST:
            oper = request.POST['oper']
        if 'status' in request.POST:
            stat = request.POST['status']
        if 'date' in request.POST:
            date = request.POST['date'] if request.POST['date'] !=u'' else str(datetime.date(1900,1,1))
        dbases = DBase.objects.filter(number__icontains = number,oper__icontains = oper, stat__icontains = stat, date__gte = date).order_by('date', 'time')
        return render_to_response('base_res.html', {'dbases': dbases, 'query': number, 'username': auth.get_user(request).username}, context_instance=RequestContext(request))
    else:
        return render_to_response('base_out.html', dict(errors=errors, username=auth.get_user(request).username), context_instance=RequestContext(request))