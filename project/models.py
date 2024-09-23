import uuid
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class CarouselItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="carousel-images/")

    def __str__(self) -> str:
        return str(self.id)


class Region(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class District(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="districts"
    )
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(
        upload_to="shops-image/", default="images/default-shop-image.jpg"
    )
    name = models.CharField(max_length=256)
    login = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def authenticate(login, password):
        try:
            return Shop.objects.get(login=login, password=password)
        except Shop.DoesNotExist:
            return None


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    author = models.CharField(max_length=256)
    isbn = models.CharField(max_length=13)
    genres = models.ManyToManyField(Genre, blank=False)
    count = models.IntegerField()

    def __str__(self):
        return self.name


class BookImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="book-images/")


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.PositiveIntegerField()
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.name} - {self.rating}/5 by {self.user.first_name}"

    
    def stars(self):
        filled = """<img src="/static/svgs/star-filled.svg" alt="" width="20" height="20">""" * self.rating
        empty = """<img src="/static/svgs/star.svg" alt="" width="20" height="20">""" * (5 - self.rating)
        return filled + empty