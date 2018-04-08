"""blog URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from home.views import home_view,about_view
from django.conf.urls.static import static
from django.conf import settings
from post.views import post_index

#viewler kullaniciya servis edilir ve bunlarin servis edilmesi icin url ler gerekir.
#sitemin anasayfasina da url tanimlamaliyim yoksa default olarak gelen django sayfasinda kalir.
#viewleri views.py de tanimlayip burada isleyecegim

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',post_index,name='home'),
    url(r'^about/',about_view,name='about'),
    #neden burda post tanimlarken $ koymadik? posttan sonra bitirirdi url i cunku


    url(r'^',include('post.urls')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
