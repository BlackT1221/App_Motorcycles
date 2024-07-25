from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Bike
from .serializers import BikeSerializer
from django.views import View

# Create your views here.

# class BikeListApiView(APIView):
#     # 1. Lista todos los registros
#     def get(self, request, *args, **kwargs):
#         '''
#         List all the bike items for given requested user
#         '''
#         bikes = Bike.objects.all()
#         serializer = BikeSerializer(bikes, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 2. Crea un nuevo registro
#     def post(self, request, *args, **kwargs):
#         '''
#         Create the Bike with given bike data
#         '''
#         data = {
#             'trademark': request.data.get('trademark'),
#             'model': request.data.get('model'),
#             'reference': request.data.get('reference'),
#             'price': request.data.get('price'),
#             'image': request.data.get('image'),
#             'supplier': request.data.get('supplier'),
#         }
#         serializer = BikeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BikeDetailApiView(APIView):
#     # 1. Metodo auxiliar para obtener el objeto con bike_id dado
#     def get_object(self, bike_id):
#         try:
#             return Bike.objects.get(id=bike_id)
#         except Bike.DoesNotExist:
#             return None

#     # 2. Recupera el elemento Bike con Bike_id dado
#     def get(self, request, bike_id, *args, **kwargs):
#         bike_instance = self.get_object(bike_id)
#         if not bike_instance:
#             return Response(
#                 {"res": "Object with bike does not exist"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = BikeSerializer(bike_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     # 3. Actualiza el elemento Bike con bike_id dado, si existe
#     def put(self, request, bike_id, *args, **kwargs):
#         bike_instance = self.get_object(bike_id)
#         if not bike_instance:
#             return Response(
#                 {"res": "Object with bike id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'trademark': request.data.get('trademark'),
#             'model': request.data.get('model'),
#             'reference': request.data.get('reference'),
#             'price': request.data.get('price'),
#             'image': request.data.get('image'),
#             'supplier': request.data.get('supplier'),
#         }
#         serializer = BikeSerializer(
#             instance=bike_instance,
#             data=data,
#             partial=True
#         )

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # 4. Elimina el elemento Bike con bike_id si existe
#     def delete(self, request, bike_id, *args, **kwargs):
#         bike_instance = self.get_object(bike_id)
#         if not bike_instance:
#             return Response(
#                 {"res": "Object with bike id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         bike_instance.delete()
#         return Response(
#             {"res": "Object has been deleted"},
#             status=status.HTTP_200_OK
#         )


class BikeListView(View):
    def get(self, request):
        # Query all bikes from the database
        bikes = Bike.objects.all()
        # Pass the bikes to the template
        context = {
            'bikes': bikes
        }
        # Render the bike list template with the context
        return render(request, 'bikes_api/bike_list.html', context)

class BikeCreateView(View):
    def get(self, request):
        # Render the bike form template with the action 'Create'
        return render(request, 'bikes_api/bike_form.html', {'action': 'Create'})

    def post(self, request):
        # Gather data from the form submission
        data = {
            'trademark': request.POST.get('trademark'),
            'model': request.POST.get('model'),
            'reference': request.POST.get('reference'),
            'price': request.POST.get('price'),
            'image': request.POST.get('image'),
            'supplier': request.POST.get('supplier'),
        }
        
        # Send a POST request to the API to create a new bike
        response = requests.post('http://localhost:8000/api/bikes/', data=data)
        if response.status_code == 201:
            # Redirect to the bike list view if the POST is successful
            return redirect('bike_list_view')
        else:
            # Return a JSON response with the error status if the POST fails
            return JsonResponse(response.json(), status=response.status_code)

class BikeEditView(View):
    def get(self, request, bike_id):
        # Get the bike object by ID or return a 404 error if not found
        bike = get_object_or_404(Bike, id=bike_id)
        # Pass the bike data and action to the template
        context = {
            'bike': bike,
            'action': 'Edit',
            'bike_id': bike_id
        }
        # Render the bike form template with the context
        return render(request, 'bikes_api/bike_form.html', context)

    def post(self, request, bike_id):
        # Gather data from the form submission
        data = {
            'trademark': request.POST.get('trademark'),
            'model': request.POST.get('model'),
            'reference': request.POST.get('reference'),
            'price': request.POST.get('price'),
            'image': request.POST.get('image'),
            'supplier': request.POST.get('supplier'),
        }
        
        # Send a PUT request to the API to update the bike
        response = requests.put(f'http://localhost:8000/api/bikes/{bike_id}/', data=data)
        if response.status_code == 200:
            # Redirect to the bike list view if the PUT is successful
            return redirect('bike_list_view')
        else:
            # Return a JSON response with the error status if the PUT fails
            return JsonResponse(response.json(), status=response.status_code)

class BikeDeleteView(View):
    def delete(self, request, bike_id):
        # Get the bike object by ID or return a 404 error if not found
        bike = get_object_or_404(Bike, id=bike_id)
        # Delete the bike object
        bike.delete()
        # Return a JSON response indicating successful deletion
        return JsonResponse({'message': 'Bike deleted successfully'}, status=204)