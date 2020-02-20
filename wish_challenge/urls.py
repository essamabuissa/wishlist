"""wish_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wish_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignUp, name='signup'),
    path('signin/', views.SignIn, name='signin'),
    path('home/', views.Home_View, name='home-page'),
    path('signout/', views.SignOut, name='signout'),
    path('wishlist/list', views.List_View, name='list'),
    path('wishlist/create_item', views.Create_Item, name='item-create'),
    path('wishlist/delete_item', views.Create_Item, name='item-create'),
    path('wishlist/<int:item_id>/delete/',views.Item_Delete ,name='item-delete'),
    path('wishlist/<int:item_id>/purchased/',views.Item_Purchased,name='item-purchased'),
    path('wishlist/<int:item_id>/unpurchased/',views.Item_Unpurchased,name='item-unpurchased'),

]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
