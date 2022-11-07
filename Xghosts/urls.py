from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include

from manager.views import (
    index,
)
from contract.views import (
    contract_view,
)
from project.views import (
    project_view,
)
from members.views import (
    Bao, CeoNhy, HaiLong, BaoLong, HaiNam, QDice, Huyen, TanLoc, Khoa, MyAnh, bee
)
urlpatterns = [
    path('', index, name="index"),
    path('contract/', contract_view, name="contract_view"),
    path('project/', project_view, name="project_view"),
    path('CeoNhy/', CeoNhy, name="CeoNhy"),
    path('HaiLong/', HaiLong, name="HaiLong"),
    path('BaoLong/', BaoLong, name="BaoLong"),
    path('HaiNam/', HaiNam, name="HaiNam"),
    path('QDice/', QDice, name="QDice"),
    path('Huyen/', Huyen, name="Huyen"),
    path('TanLoc/', TanLoc, name="TanLoc"),
    path('Khoa/', Khoa, name="Khoa"),
    path('MyAnh/', MyAnh, name="MyAnh"),
    path('Bao/', Bao, name="Bao"),
    path('bee/', bee, name="bee")

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

