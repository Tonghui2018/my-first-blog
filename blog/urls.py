from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^article/(\d+)/',views.viewArticle,name = 'artcle'),
    url(r'^$',views.post_list),
]