from django.shortcuts import render, redirect, get_object_or_404
from recipeboxapp.models import Member, Item, ImageModel
from recipeboxapp.form import Recipeform, ImageUploadForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            members = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'member': members})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def searchresult(request):
    return render(request, 'searchresult.html')


def singlepost(request):
    return render(request, 'singlepost.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        members = Member(firstname=request.POST['firstname'],
                         lastname=request.POST['lastname'], email=request.POST['email'],
                         username=request.POST['username'], password=request.POST['password'])

        members.save()
        return redirect('/')
    else:
        return render(request, 'signup.html')


def edit(request, pk):
    get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = Recipeform(request.POST, instance=Member)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = Recipeform(instance=Member)
    return render(request, 'edit.html', {'form': form})


def add(request):
    if request.method == "POST":
        form = Recipeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Recipeform()
    return render(request, 'add.html', {'form': form})


def show(request):
    products = Item.objects.all()
    return render(request, 'show.html', {'recipe': Item})


def update(request, id):
    recipe = Item.objects.get(id=id)
    form = Recipeform(request.POST, instance=Member)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'Recipe': Member})


def addimage(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/image')
    else:
        form = ImageUploadForm()
    return render(request, 'add.html', {'form': form})


def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_images.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')
