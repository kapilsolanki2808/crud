from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/',views.create),
    path('retrive/',views.retrive,name = "retrive"),
    path('view/detail/<selected_id>/',views.view_details, name = "view_details"),
    path('update/<int:id>/', views.update), 
    path('delete/<int:id>/',views.delete, name = 'delete'),
    path('sure/delete/<int:id>/',views.sure_delete, name = 'sure_delete'),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
