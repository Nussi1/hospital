from django.contrib import admin
from django.urls import path, include
from hospital.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer-create/', add_customer, name='customer-create'),
    path('appointment-create/', add_app, name='app-create'),
    path('', index, name='index')
    # path('', include('hospital.urls')),

    # path('photo_detail/<int:id>', photo_detail, name='photo_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
