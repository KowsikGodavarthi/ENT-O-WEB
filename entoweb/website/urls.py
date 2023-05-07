from django.urls import path
from . import views
from .views import home, signup, bookings, gallery, registerent, registercust, aboutus, contactus, login, welcome, \
    signup2, logout_view, gallery1, gallery2, gallery3, gallery4, payment, feedback
from django.contrib import admin
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('welcome-to-ent-o-web/', signup2, name='signup2'),
    path('bookings/',bookings, name='bookings'),
    path('gallery/', gallery, name='gallery'),
    path('galleryconcert/', gallery1, name='gallery1'),
    path('gallerystandup/', gallery2, name='gallery2'),
    path('gallerydance/', gallery3, name='gallery3'),
    path('gallerymagic/', gallery4, name='gallery4'),
    path('registerentertainer/', registerent, name='regent'),
    path('registercustomer/', registercust, name='regcus'),
    path('aboutus/', aboutus, name='about'),
    path('contactus/', contactus, name='contactus'),
    path('login/', LoginView.as_view(template_name='Login.html'), name='login'),
    path('welcome/',welcome, name='welcome'),
    path('logout/',logout_view,name='logout'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('payment/',payment,name='payment'),
    path('feedback/',feedback, name='feedback'),

]
admin.site.site_header = 'ENT-O-WEB ADMIN'
admin.site.index_title = 'Features area'
admin.site.site_title = 'ADMINISTRATION'