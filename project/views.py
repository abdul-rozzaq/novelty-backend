from PIL import Image
from io import BytesIO

from django.http import FileResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from django.contrib.sessions.middleware import SessionMiddleware
from project.decorators import login_required
from project.forms import BookForm

from .models import Book, BookImage, Genre, Shop


@login_required
def home_page(request):
    return render(request, 'tabs/home.html',)


@login_required
def books_page(request):
    context = {
        'genres': Genre.objects.all(),
        'books': Book.objects.filter(shop=request.shop),
        'filter_genre': request.GET.getlist('genre')
    }
    
    if request.method == 'POST':
        
        data = {
            'shop': request.shop, 
            **{key : value for key, value in request.POST.items() if key != 'genres'}, 
            'genres': request.POST.getlist('genres'),
        }

        form = BookForm(data, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('books_page')
        else:
            context['errors'] = [{'field': key, 'value': value.as_text()[1:].strip()} for key, value in form.errors.items()]
                        
    return render(request, 'tabs/books.html', context)


@login_required
def orders_page(request):
    return render(request, 'tabs/orders.html')


@login_required
def comments_page(request):
    return render(request, 'tabs/comments.html')


@login_required
def collections_page(request):
    return render(request, 'tabs/collections.html')


@login_required
def chat_page(request):
    return render(request, 'tabs/chat.html')


def edit_book(request, pk):
    
    context = {
        'book': Book.objects.get(pk=pk),
        'genres': Genre.objects.all(),
    }
    
    return render(request, 'tabs/edit_book.html', context)


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

    return render(request, 'auth/login.html', context)


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
        
    return render(request, 'auth/register.html', context)


def logout(request):
    if 'shop_id' in request.session:
        del request.session['shop_id']
    return redirect('login_page')


def get_image(request, image_id, size):
    size = float(size)

    if size in [1, 0.7, 0.5, 0.3]:
        image = BookImage.objects.get(id=image_id)

        original_image = Image.open(image.image.path)
        resized_image = original_image.resize(
            (int(image.image.width * float(size)), int(image.image.height * float(size))))

        buffer = BytesIO()
        resized_image.save(buffer, format="png")
        buffer.seek(0)

        return FileResponse(buffer, as_attachment=False, filename=f'{image.image.name.split(".")[0]}.png')
    else:
        return HttpResponseNotFound('Image not found')
