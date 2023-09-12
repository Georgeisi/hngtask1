from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from .models import Person
from .seriallizers import PersonSerializer
from rest_framework import status
# from drf_spectacular.utils import extend_schema


# Create your views here.

# @api_view(['GET'])
# def home(request):
#     if request.method == 'GET':
#         slack_name = request.GET.get('slack_name', None)
#         track = request.GET.get('track', None)
#         current_utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

       
#         current_day = datetime.utcnow().strftime('%A')

#         return Response({
#             'slack_name': slack_name,
#             'current_day': current_day,
#             'utc_time': current_utc_time,
#             'track':track,
#             'github_file_url':'https://github.com/Georgeisi/hngtask1/blob/main/api/views.py',
#             'github_repo_url': 'https://github.com/Georgeisi/hngtask1/tree/main',
#             'Status_code': '200'
#         })
    



# @extend_schema(responses=PersonSerializer)
@api_view(['GET', 'POST'])
def get_user(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @extend_schema(responses=PersonSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):
    try:
        person = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return Response({'message': 'this person doesnt exist on the db'})

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    



