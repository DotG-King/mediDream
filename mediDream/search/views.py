from django.shortcuts import render
from .forms import UploadForm
from list.models import search,pillInfo
from django.contrib.auth.models import User
from .predict import img_clf

# Create your views here.

# def search_view(request) :
#     return HttpResponse('검색 페이지 입니다.')

def index(request):
    return render(request,'search/index.html', {})

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            predict=search()
            predict.mediDream_id=User.objects.get(username=request.user.username)
            predict.img=request.FILES['img']
            predict_result=img_clf(predict.img)
            predict.pill=pillInfo.objects.get(id=predict_result)
            predict.save()
            pill=pillInfo.objects.all().filter(id=predict_result)
            return render(request, 'list/info.html', {'pill':pill})

    else:
        form = UploadForm()
    return render(request,'search/upload.html',{ 'form': form })