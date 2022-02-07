from django.urls import path
from product import views

urlpatterns=[
    path('fcreate/',views.fproduct, name="fcreate"),
    path('ccreate/',views.cproduct.as_view(), name="ccreate"),
    path('ctemp/',views.ctemp.as_view(), name="ctemp"),
    path('ctemp1/',views.ctemp1.as_view(), name="ctemp1"),
    path('cform/',views.cform.as_view(), name="cform"),
    path('ccre/',views.ccre.as_view(), name="ccre"),
    path('chome/',views.home.as_view(), name="chome"),
    path('fselect/',views.fselect,name='fselect'),
    path('cselect/',views.cselect.as_view(),name='cselect'),
    path('pcselect/',views.pcselect.as_view(),name='pcselect'),
    path('fdetails/<pk>/',views.fdetails,name='fdetails'),
    path('cdetails/<pk>/',views.cdetails.as_view(),name='cdetails'),
    path('pcdetails/<pk>/',views.pcdetails.as_view(),name='pcdetails'),
    path('fupdate/<pk>/',views.fupdate,name='fupdate'),
    path('cupdate/<pk>/',views.cupdate.as_view(),name='cupdate'),
    path('pcupdate/<pk>/',views.pcupdate.as_view(),name='pcupdate'),
    path('fdelete/<pk>/',views.fdelete,name='fdelete'),
    path('cdelete/<pk>/',views.cdelete.as_view(),name='cdelete'),
    path('pcdelete/<pk>/',views.pcdelete.as_view(),name='pcdelete'),
    
    
    
]