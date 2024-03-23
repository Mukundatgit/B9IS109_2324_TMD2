
from django.contrib import admin
from django.urls import path , include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shoppingapp.urls')),
    path('', include('account.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]

admin.site.site_header = "Shopping Mall Admin"
admin.site.site_title = "Shopping Admin Portal"
admin.site.index_title = "Welcome to Shopping Mall Portal"
