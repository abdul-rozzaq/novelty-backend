from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from accounts.permissions import IsAuthenticated
from accounts.auth import TokenAuthentication
from project.models import Book, CarouselItem, Genre
from project.serializers import BookSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_carousel_items(request):
    return Response([x.image.url for x in CarouselItem.objects.all()])


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_genres(request):
    return Response([{'id': x.id, 'name': x.name} for x in Genre.objects.all()])


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_books(request):

    books = Book.objects.all()

    serializer = BookSerializer(books, many=True, context={'request': request})

    return Response(serializer.data)
