from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime


# Create your views here.

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        slack_name = request.GET.get('slack_name', None)
        track = request.GET.get('track', None)
        current_utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

       
        current_day = datetime.utcnow().strftime('%A')

        return Response({
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': current_utc_time,
            'track':track,
            'github_file_url':'https://github.com/Georgeisi/hngtask1/blob/main/api/views.py',
            'github_repo_url': 'https://github.com/Georgeisi/hngtask1/tree/main',
            'Status_code': '200'
        })
    






