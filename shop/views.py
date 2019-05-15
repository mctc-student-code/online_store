from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category,Product
#The form
from django.contrib.auth.models import Group,User
from .forms import SignUpForm
#sign in view
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate, logout

# from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Category View
def allProdCat(request, c_slug=None):
    c_page=None
    products=None
    if c_slug != None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.filter(category = c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request,'shop/category.html',{'category':c_page,'products':products})


# product view
def ProdCatDetail(request, c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'shop/product.html',{'product':product})


# sign up
def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})


# sign in
def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:allProdCat')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/signin.html', {'form':form })


# signout
def signoutView(request):
    logout(request)
    return redirect('signin')