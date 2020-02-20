from django.shortcuts import render , redirect
from .forms import SigninForm, SignUpForm , SigninForm ,ItemForm
from django.contrib.auth import login, authenticate , logout
from .models import Item


def Home_View(request):
    return render(request, 'home.html')

def List_View(request):
    context={
        'items' : Item.objects.filter(owner = request.user).order_by('-timeadd'),
    }
    return render(request, 'list.html', context)

#Register----------------------------------------------------------------
def SignUp(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(user.password)
            user.save()
            login(request,user)
            return redirect("home-page")
    context = {
    "form" : form
    }
    return render(request,'signup.html', context)



def SignIn(request):
    if request.user.is_authenticated:
        return (redirect ("list"))
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'signin.html', context)

def SignOut(request):
    logout(request)
    return redirect('home-page')

#CRUD--------------------------------

def Create_Item(request):
    if request.user.is_anonymous  :
        return redirect('signin')
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'create_item.html', context)

def Item_Delete(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user.is_anonymous or request.user !=  item.owner:
        return render (request, "unathorized.html")
    item.delete()
    return redirect('list')

def Item_Purchased(request, item_id):
    item = Item.objects.get(id=item_id)
    item.is_purchased = True
    if request.user.is_authenticated:
        item.purchased_by = request.user.username
    else :
        item.purchased_by = "Anonymous"

    item.save()

    return redirect('list')

def Item_Unpurchased(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user.is_anonymous or request.user !=  item.owner:
        return render (request, "unathorized.html")
    item.is_purchased = False
    item.save()
    return redirect('list')
