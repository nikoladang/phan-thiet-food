"""phanthietfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # url(r'^$ ', 'phan-thiet-food.views.home', name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'phanthietfood.views.index', name='index'),
    url(r'^food/$', 'phanthietfood.views.food', name='food'),
    url(r'^travel/$', 'travel.views.travel', name='travel'),
    url(r'^fun/$', 'phanthietfood.views.fun', name='fun'),
    url(r'^contact/$', 'contact.views.contact', name='contact'),
    # url(r'^accounts/', include('registration.backends.default.urls'))
    url(r'^accounts/', include('registration.backends.simple.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)