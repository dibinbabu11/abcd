from django.shortcuts import redirect, render
from django .http import HttpResponse
from .models import movie
from . forms import movie_form
# Create your views here.

def index(request):
    movies=movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movies=movie.objects.get(id=movie_id)

    return render(request,'detail.html',{'movies':movies})


def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movies=movie(name=name,desc=desc,year=year,img=img)
        movies.save()


    
    return render(request,'add.html')

def update(request,id):
    movies=movie.objects.get(id=id) 
    form=movie_form(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'movies':movies})
def delete(request,id):
    if request.method=="POST":
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render (request,'delete.html')
    