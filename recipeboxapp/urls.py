from django.contrib import admin
from django.urls import path
from recipeboxapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('searchresult/', views.searchresult, name='searchresult'),
    path('singlepost/', views.singlepost, name='singlepost'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('show/', views.show, name='show'),
    path('update/<int:id>', views.update),
    path('edit/<int:id>', views.edit),
    path('add/', views.addimage, name='add'),
    path('show_images/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),

]
