from django.urls import path
from django.views.generic.base import RedirectView

from . import views
from .models import choices,SecretUrl,additionalHtml


urlpatterns = [
    path("", RedirectView.as_view(url='/theloner/loner', permanent=True)),
    path('loner', views.loner,name='loner'),
    path('ooo', views.searching, name='searching'),
    path('<slug:secret>', views.loner, name='lonerguessing'),
]

'''
a=SecretUrl.objects.all()

for obj in a:
    urlpatterns+=[path(f'{obj.secretWord}', views.discovered,
                       {'sw':f'{secretWord}'},name='discovered')]

it probably was inefficent anyway
'''