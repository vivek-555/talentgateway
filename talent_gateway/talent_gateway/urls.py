"""talent_gateway URL Configuration

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
from talent_portal import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.JobListView.as_view(), name="job_listing"),
    url(r'^job/(?P<job_id>\d+)$', views.job_detail, name='job_detail'),
    url(r'^job/apply$', views.job_apply, name='job_apply'),
    url(r'^home/$', views.homepage, name="home"),
    url(r'^dataentry/$', views.data_entry_page, name="data-entry"),
    url(r'^dataentry/userlist/data/$', views.OrderListJson.as_view(), name="userList"),
    url(r'^dataentry/userlist/$', views.user_list_page, name="userListPage"),
    url(r'^dataentry/filter/create$', views.save_filter, name="saveFilter"),
    url(r'^dataentry/filter/$', views.get_filters, name="filter_list"),
    url(r'^dataentry/upload/$', views.updload_records, name="updload_records"),
    url(r'^task/status/(?P<task_id>[\w\-]+)/$', views.get_task_status, name="task_status"),
    url(r'^user/$', views.user_view, name="user-view"),
    url(r'^user/edit/(?P<id>[\w\-]+)/$', views.edit_record, name="edit-user"),
    url(r'^user/save/$', views.save_record, name="save-user"),
    url(r'^unauthorized/', views.unauthorized, name="unauthorized"),
    url(r'^download/(?P<path>.*)$', views.download, name="download-rar")
]
