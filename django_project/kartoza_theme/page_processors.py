
from django import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from mezzanine.pages.models import Page
from cartridge.shop.models import Category

#
@processor_for(Category)
def author_form(request, page):

    return {"test_index": "wooohooo yeah!"}
