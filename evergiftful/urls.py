from django.urls import path
from . import views
from .views import ProductDetail, ProductsByCategoryView, BlogDetail
from .views import custom_login, wishlist_remove
from django.contrib.auth.views import LogoutView





app_name = 'evergiftful'

urlpatterns = [
    path('', views.home, name="home"),
    path('gifts/', views.gifts, name="gifts"),
    
    path('Products/<slug:slug>/', ProductDetail.as_view(), name="product_detail"),
    path('products/<slug:category_slug>/', ProductsByCategoryView.as_view(), name='products_by_category'),
    path('wishlist/', views.wishlist, name="wishlist"),
      path('wishlist/remove/<int:product_id>/', wishlist_remove, name='wishlist_remove'),

 
  


    path('blogs/', views.blogs , name="blog"),
    path('blogs/<slug:slug>/', BlogDetail.as_view(), name="blog_detail"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),


    path('login/', custom_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup')
]
