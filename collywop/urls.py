"""collywop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^adm/', include('adm.urls', namespace='adm')),
    url(r'^invoice/', include('invoice.urls', namespace='invoice')),
    url(r'^po/', include('po.urls', namespace='po')),
    url(r'^quote/', include('quote.urls', namespace='quote')),
    url(r'^vendor/', include('vendor.urls', namespace='vendor')),
    url(r'^status/', include('status.urls', namespace='status')),
    url(r'^w/', include('warehouse.urls', namespace='w')),
    url(r'^intacct/', include('intacct.urls', namespace='intacct')),
    url(r'', include('home.urls', namespace='home')),
]
