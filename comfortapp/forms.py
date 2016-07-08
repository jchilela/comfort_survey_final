#!/usr/bin/python
# -*- coding: latin-1 -*-

from django import forms
from .models import index

class index(forms.Form):
	preference = forms.CharField()