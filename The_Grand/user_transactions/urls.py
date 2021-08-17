from django.urls import path
from .views import home_view
from .import views

urlpatterns = [
    path('', views.home_view,name='home_view'),
    path('home', views.home,name='home'),
    path('contact', views.contact,name='contact'),
    path('booking', views.booking,name='booking'),
    path('register',views.register,name='register'),
    path('location',views.default_map,name='location'),
    path('reviews',views.comments,name='reviews'),
    path('location_detail',views.location_detail,name='location_detail'),
    path('news',views.news,name='news'),
    path('booking_detail',views.booking_detail,name='booking_detail'),
    path('event',views.event,name='event'),
    path('booking_confirm',views.booking_confirm,name='booking_confirm'),
    path('booking_view',views.booking_view,name='booking_view'),
    path('pdf_generation',views.pdf_generation,name='pdf'),
    path('restaurant',views.restaurant_view,name='restaurant'),
    path('about',views.about,name='about'),

    
    
]