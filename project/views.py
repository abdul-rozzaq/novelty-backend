from PIL import Image
from io import BytesIO

from django.http import FileResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from django.contrib.sessions.middleware import SessionMiddleware
from project.decorators import shop_check_decorator

from .models import Book, Shop


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
    context = {'errors' : []}
        
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')

        shop = Shop.authenticate(login=login, password=password)

        if shop is not None:
            request.session['shop_id'] = str(shop.id)
            return redirect('home_page')
        
        else:
            context['errors'].append('Parol xato yoki bunday do\'kon mavjud emas')

    return render(request, 'login.html', context)


def register_page(request):
    context = {'errors' : []}
    
    if request.method == 'POST':
        name = request.POST.get('name')
        login = request.POST.get('login')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        
        if  None not in [name, login, password1, password2] and not Shop.objects.filter(login=login).exists() and password1 == password2 and len(password1.strip()) >= 8:
                
            shop = Shop.objects.create(name=name, login=login, password=password1)
            
            request.session['shop_id'] = str(shop.id)
            return redirect('home_page')
        
        if password1 != password2:
            context['errors'].append('Parollar bir xil emas')
                
        if len(password1.strip()) < 8:
            context['errors'].append('Parol 8 belgi uzunligida bo\'lishi kerak')
        
        if Shop.objects.filter(login=login).exists():
            context['errors'].append(f'Login "{login}" allaqachon foydalanilgan')
        
    return render(request, 'register.html', context)


def logout(request):
    if 'shop_id' in request.session:
        del request.session['shop_id']
    return redirect('login_page')