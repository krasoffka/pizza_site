"""pizzashopproject URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from pizzashopapp import views

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    url(r'^pizzashop/sign-in/$', auth_views.login,
        {'template_name': 'pizzashop/sign_in.html'},
        name='pizzashop-sign-in'),

    url(r'^pizzashop/sign-out', auth_views.logout,
        {'next_page': '/'},
        name='pizzashop-sign-out'),

    url(r'^pizzashop/$', views.pizzashop_home, name='pizzashop-home'),

    url(r'^pizzashop/sign-up', views.pizzashop_sign_up, name='pizzashop-sign-up'),

    url(r'^pizzashop/account/$', views.pizzashop_account, name='pizzashop-account'),
    url(r'^pizzashop/pizza/$', views.pizzashop_pizza, name='pizzashop-pizza'),
    url(r'^pizzashop/pizza/add/$', views.pizzashop_add_pizza, name='pizzashop-add-pizza'),
    url(r'^pizzashop/pizza/edit/(?P<pizza_id>\d+)/$', views.pizzashop_edit_pizza, name='pizzashop-edit-pizza'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
