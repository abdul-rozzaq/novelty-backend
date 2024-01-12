from django.shortcuts import render

# Create your views here.



from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_genres(request):

    return Response([{'key': x} for x in range(10)])
