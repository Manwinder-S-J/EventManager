from django.urls import path
from .views import upcoming_events, create_event, edit_event, delete_event, toggle_registration, unregister_user


urlpatterns = [
    path('upcoming/', upcoming_events, name='upcoming_events'),
    path('create/', create_event, name='create_event'),
    path('edit/<int:event_id>/', edit_event, name='edit_event'),
    path('delete/<int:event_id>/', delete_event, name='delete_event'),
    path('toggle_registration/<int:event_id>/', toggle_registration, name='toggle_registration'),
    path('unregister_user/<int:event_id>/<int:user_id>/', unregister_user, name='unregister_user'),
]
