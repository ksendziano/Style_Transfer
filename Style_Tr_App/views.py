from django.http import HttpResponse
from django.shortcuts import render
from .models import Style_Tr
import os
from .forms import ImageForm
from .import Style_Transfer_Modul


def show_main_page(request):
    form = ImageForm()
    return render(request, 'Style_Transfer/Main_Page.html', {'form': form}) #'Style_Transfer/Main_Page.html'много раз дублируется - в константы.


def transfer(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = Style_Tr(img_content=request.FILES.get('img_content'),
                              img_style=request.FILES.get('img_style'))
            form.save()
            Style_Transfer_Modul.transfer_function(images.img_content.path,
                                                   images.img_content.path, 10)
            return render(request, 'Style_Transfer/Main_Page.html', {'form': form})
    else:
        form = ImageForm()
    return render(request, 'Style_Transfer/Main_Page.html', {'form': form})# возвращаешь одно и то же, можно сделать это 1 раз в конце функции.


def download_img(request):
    file_path = './media/images/stylized-image.png'
    file = open(file_path, 'rb')
    response = HttpResponse(file.read(), content_type='Image')
    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    return response
