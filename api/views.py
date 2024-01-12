from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from accounts.permissions import IsAuthenticated
from accounts.auth import TokenAuthentication
from project.models import CarouselItem


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_carousel_items(request):
    return Response([x.image.url for x in CarouselItem.objects.all()])
