# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import RoomBookingViewSet
# from . import views

# router = DefaultRouter()
# router.register(r'bookings', RoomBookingViewSet)

# urlpatterns = [
#     path('api/bookings/', views.list_bookings, name='list_bookings'),
#     path('api/bookings/', views.create_booking, name='create_booking'),
#     path('api/bookings/<str:room_name>/', views.retrieve_booking, name='retrieve_booking'),
#     path('api/bookings/<int:id>/', views.update_booking, name='update_booking'),
#     path('api/bookings/<int:id>/', views.delete_booking, name='delete_booking'),
#     path('api/bookings/', views.create_booking, name='create_booking'),
# ]


# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('api/booked_dates/<str:room_name>/', views.get_booked_dates, name='get_booked_dates'),
# # ]


from django.urls import path
from . import views

urlpatterns = [
    # Assuming 'room_name' is a string parameter
    path('api/bookings/<str:room_name>/', views.retrieve_booking, name='retrieve_booking'),
]
