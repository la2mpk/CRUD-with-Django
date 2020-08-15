from django.urls import path
from . import views

app_name = 'geeks'
urlpatterns = [
    path('', views.create_view, name='create'),
    path('retrieve/', views.list_view, name='list'),
    path('details/<int:id>', views.details_view, name='details'),
    path('update/<int:id>', views.update_view, name='update'),
    path('delete/<int:id>', views.delete_view, name='delete')
]
