from django.shortcuts import render
from django.http import HttpResponse


def testing_view(reequest):
    return HttpResponse("Привет, мирок")


def seckend_view(reequest):
    return HttpResponse("Ещё раз привет, мирок")
