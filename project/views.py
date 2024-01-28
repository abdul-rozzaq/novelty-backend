from PIL import Image
from io import BytesIO

from django.http import FileResponse

from .models import Book


def get_image(request, book_id, size):

    size = float(size)
    book = Book.objects.get(id=book_id)

    original_image = Image.open(book.image.path)
    resized_image = original_image.resize(
        (int(book.image.width * float(size)), int(book.image.height * float(size))))

    buffer = BytesIO()
    resized_image.save(buffer, format="png")
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename=f'{book.image.name.split(".")[0]}.png')
