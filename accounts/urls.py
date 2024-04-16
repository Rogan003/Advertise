from django.http import HttpResponse
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register, name = 'register'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('<str:username>', views.profile, name = 'profile'), #mozda i nije najbolje, ali ajde eo i nesto sa neta r'^(?P<username>\w+)\$'
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)