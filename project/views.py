from PIL import Image
from io import BytesIO

from django.http import FileResponse, HttpResponseNotFound

from .models import Book


def get_image(request, book_id, size):
    size = float(size)
    
    if size in [1, 0.7, 0.5, 0.3]:
        book = Book.objects.get(id=book_id)

        original_image = Image.open(book.image.path)
        resized_image = original_image.resize(
            (int(book.image.width * float(size)), int(book.image.height * float(size))))

        buffer = BytesIO()
        resized_image.save(buffer, format="png")
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=False, filename=f'{book.image.name.split(".")[0]}.png')
    else: 
        return HttpResponseNotFound('Image not found')
