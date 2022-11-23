from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import UploadForm

# Create your views here.

# def search_view(request) :
#     return HttpResponse('검색 페이지 입니다.')

def index(request):
    return render(request,'search/index.html', {})

def image_list(request):
    return render(request,'search/list.html', {})

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = UploadForm()
    return render(request,'search/upload.html',{
        'form': form
    })