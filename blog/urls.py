from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # The P<pk> will take everything you place here and transfer it to a view as a variable called pk
    #If say /post/5 was done, it would transfer the information that pk 5
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]