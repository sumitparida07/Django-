from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('elements/',views.elements, name='elements'),
    path('news/',views.news, name='news'),
    path('contact/',views.contact, name='contact'),
    # path('register/',views.register, name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)