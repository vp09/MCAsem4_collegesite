
from django.urls import include

from django.urls import path
from . import views

urlpatterns = [
     path('admin/', admin.site.urls),
    # path('index/',include('views.index')),
]
