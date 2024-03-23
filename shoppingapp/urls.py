from django.urls import path
from shoppingapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "shoppingapp"


urlpatterns = [

    path('', views.home_view, name='home'),
    path('shops/', views.shop_list_View, name='store-list'),
    path('shop/create/', views.create_shop_View, name='create-shop'),
    path('shop/<int:id>/', views.single_shop_view, name='single-shop'),
    path('result/', views.search_result_view, name='search_result'),
    path('dashboard/employer/shop/edit/<int:id>', views.shop_edit_view, name='edit-shop'),
    path('dashboard/employer/delete/<int:id>/', views.delete_shop_view, name='delete'),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)