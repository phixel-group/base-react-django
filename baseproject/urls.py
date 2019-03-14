"""baseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from sys import path
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.views.i18n import javascript_catalog
from django.contrib.auth.views import logout
from django.contrib.staticfiles.urls import static
from django.conf import settings



from Base.views import index

js_info_dict = {
    #domain is default
    'packages': ('Base',),
}
urlpatterns = [

    #url(r'^registro/', AddUsuario.as_view(), name='registro'),
    #url(r'^salir$', logout, name="salir", kwargs={'next_page': 'login:login'})
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += i18n_patterns(
    url(_(r'^admin/'), admin.site.urls),
    url(_(r'^'), index, name="index"),
    url(r'^i18n/',include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog')
)
