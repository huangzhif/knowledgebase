from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.knowledges_title,name='know_title'),
    url(r'(?P<knowledge_id>\d)/$',views.knowledges_details,name='knowledges_details')
]