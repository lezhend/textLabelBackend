"""data_labelling_platform URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

import account_manager.views
import file_manager.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fir/label/account/add_account[/]$', account_manager.views.AddAccountView.as_view()),
    url(r'^fir/label/account/add_originalFile[/]$', file_manager.views.AddOriginalFileView.as_view()),
]

urlpatterns += [
    url(r'^fir/label/auth[/]', include('rest_framework.urls'))
]
