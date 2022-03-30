from django.shortcuts import render
import datetime
import base64
import json
import logging
import copy
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
def index_handler(request):

    return render(request, "index.html", context={

    })