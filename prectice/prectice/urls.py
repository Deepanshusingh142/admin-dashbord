"""
URL configuration for prectice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf.urls import handler400
from prectice  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('404',views.error4),
    path('500',views.error5),
    path('add_customer',views.add_customer),
    path('forgot',views.forgot,name="forgot"),
    path('login',views.login,name='login'),#name=''  ye set krna hota hai jb hum action user krte hai action url se view me data pass krta hai
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name="logout"),
    # path('',views.),
            
            
]
handler404 ='prectice.views.error4'
