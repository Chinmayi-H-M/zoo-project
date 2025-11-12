"""
URL configuration for zoo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display_landing, name='landing'),
    path('tiger/', views.display_tiger, name='tiger'),
    path('monkey/',views.display_monkey, name='monkey'),
    path('elephant/',views.display_elephant, name='elephant'),
    path('lion/',views.display_lion, name='lion'),
    path('giraffe/',views.display_giraffe, name='giraffe'),
    path('ostrich/',views.display_ostrich, name='ostrich'),
    path('peacock/',views.display_peacock, name='peacock'),
    path('cheetah/',views.display_cheetah, name='cheetah'),
    path('zebra/',views.display_zebra, name='zebra'),
    path('python/',views.display_python, name='python'),
    path('animals',views.display_data,name='data'),
    path('login/',views.login,name='email'),
    #path('zoo/info',views.zoo_info,name='zoo_info'),
    path('compare/',views.compare,name='compare'),

]
