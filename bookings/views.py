# from rest_framework import viewsets
# from .models import RoomBooking
# from .serializers import RoomBookingSerializer

# class RoomBookingViewSet(viewsets.ModelViewSet):
#     queryset = RoomBooking.objects.all()
#     serializer_class = RoomBookingSerializer

# # views.py
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # from .models import RoomBooking
# # from .serializers import RoomBookingSerializer

# @api_view(['GET'])
# def list_bookings(request):
#     """List all bookings."""
#     bookings = RoomBooking.objects.all()
#     serializer = RoomBookingSerializer(bookings, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_booking(request):
#     """Create a new booking."""
#     serializer = RoomBookingSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import RoomBooking
# from .serializers import RoomBookingSerializer

# @api_view(['GET'])
# def retrieve_booking(request, room_name):
#     """Retrieve all bookings for a specific room."""
#     bookings = RoomBooking.objects.filter(room_name=room_name)
#     if not bookings:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     # Serialize all the bookings for the specified room
#     serializer = RoomBookingSerializer(bookings, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_booking(request):
#     """Create a new booking."""
#     if request.method == 'POST':
#         serializer = RoomBookingSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['PUT'])
# def update_booking(request, id):
#     """Update a booking."""
#     try:
#         booking = RoomBooking.objects.get(id=id)
#     except RoomBooking.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = RoomBookingSerializer(booking, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_booking(request, id):
#     """Delete a booking."""
#     try:
#         booking = RoomBooking.objects.get(id=id)
#     except RoomBooking.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     booking.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RoomBooking
from .serializers import RoomBookingSerializer

@api_view(['GET'])
def retrieve_booking(request, room_name):
    """Retrieve all bookings for a specific room."""
    try:
        # Filter the bookings based on the room_name
        bookings = RoomBooking.objects.filter(room_name=room_name)
        if not bookings:
            return Response(status=404, data={'message': 'No bookings found for this room'})

        # Serialize the bookings
        serializer = RoomBookingSerializer(bookings, many=True)
        return Response(serializer.data)

    except RoomBooking.DoesNotExist:
        return Response(status=404, data={'message': 'Room not found'})
