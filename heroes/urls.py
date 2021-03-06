from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from heroes import views

urlpatterns=patterns('',
    url(r'^list/$', views.HeroList.as_view(), name='hero_list'),
    url(r'^detail/(?P<riot_id>[\w-]+)/$', views.HeroDetail.as_view(), name='hero_detail'),      
    )

