from django.urls import path
from .views import BikeCreateView, BikeEditView, BikeDeleteView, BikeListView

urlpatterns = [
    # path('bikes/', BikeListApiView.as_view(), name='bike_list_api'),
    # path('bikes/<int:bike_id>/', BikeDetailApiView.as_view(), name='bike_detail_api'),
    
    # URL pattern for viewing the list of bikes
    path('bikes/view/', BikeListView.as_view(), name='bike_list_view'),

    # URL pattern for creating a new bike
    path('new/', BikeCreateView.as_view(), name='bike_create'),

    # URL pattern for editing an existing bike, specified by bike_id
    path('<int:bike_id>/edit/', BikeEditView.as_view(), name='bike_edit'),

    # URL pattern for deleting an existing bike, specified by bike_id
    path('<int:bike_id>/delete/', BikeDeleteView.as_view(), name='bike_delete'),
]
