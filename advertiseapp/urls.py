from django.http import HttpResponse
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('advertising', views.advertise, name = 'advertise'),
    path('aboutus', views.aboutus, name = 'aboutus'),
    path('postad', views.postad, name = 'postad'),
    path('<int:id>post', views.post, name='post'),
    path('<int:id>like', views.like, name='like'),
    path('<int:id>dislike', views.dislike, name='dislike'),
    path('search', views.search, name = 'search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)