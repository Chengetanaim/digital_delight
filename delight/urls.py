from django.urls import path
from . import views
from .views import SearchResultsView

app_name = 'delight'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
    path('store/', views.store, name='store'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('savings-product/<int:product_id>/', views.savings_product, name='savings_product'),
    path('search-results/', SearchResultsView.as_view(), name='search_results'),
    path('mobile-search/', views.mobile_search, name='mobile_search'),
]