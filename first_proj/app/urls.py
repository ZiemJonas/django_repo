from django.conf.urls import url
from app import views


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^formpage/', views.form_name_view, name='formpage')
]
