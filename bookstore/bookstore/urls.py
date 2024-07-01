
from django.contrib import admin
from django.urls import path
from BookStoreApp.views import index, book_detail
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'book'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('suplement/<id>/', book_detail, name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()