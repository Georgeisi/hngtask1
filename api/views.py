from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime


# Create your views here.

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        # Get the current UTC time
        current_utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        # Get the current day
        current_day = datetime.utcnow().strftime('%A')

        return Response({
            'slack_name': 'George',
            'current_day': current_day,
            'utc_time': current_utc_time,
            'Status_code': '200'
        })




