from PIL import Image
from io import BytesIO

from django.http import FileResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from django.contrib.sessions.middleware import SessionMiddleware
from project.decorators import shop_check_decorator

from shop_api.models import Shop

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


@shop_check_decorator
def home_page(request):
    return render(request, 'home.html',)


def login_page(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        user = Shop.authenticate(login=login, password=password)

        if user is not None:
            request.session['shop_id'] = str(user.id)
            return redirect('home_page')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html',)


def register_page(request):
    return render(request, 'register.html',)


def logout(request):
    if 'shop_id' in request.session:
        del request.session['shop_id']
    return redirect('login_page')