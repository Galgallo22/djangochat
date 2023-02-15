from django.urls import path
from.import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('viewer',views.viewer, name='viewer'),
    path('contacts',views.contacts, name='contacts'),
]