from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteListCreate.as_view(), name='note-list'),
    path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name='delete-note'),
    path('players/', views.PlayerList.as_view(), name='player-list'),
    path('players/delete/<int:pk>/', views.PlayerList.as_view(), name='delete-player'),
    path('players/info/<int:pk>/', views.PlayerDetail.as_view(), name='player-info'),
]