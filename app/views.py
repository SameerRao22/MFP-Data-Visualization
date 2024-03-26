from django.http import HttpResponse, response, Http404
from .forms import UploadForm
from django.shortcuts import render
from .functions import handle_uploaded_file, convert
import os

def form(request):
    flag = False
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            convert('app/data/file.csv')
            flag = True
        else:
            flag = False
    form = UploadForm()
    return render(request, "fitness.html", {"form":form, "upload":flag})

def data(request):
    file_path = 'app/data/file.csv'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/csv')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
