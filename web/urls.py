from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^play$',views.play, name='play'),
	url(r'^ReceivePointsTest$',views.ReceivePointsTest, name='sendPointsTest'),
	url(r'^sendPoints/$',views.send_points, name='sendPoints'),
   
]