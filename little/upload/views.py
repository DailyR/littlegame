from django.shortcuts import render



# Create your views here.

def upload(request):
    if request.method == "GET":
        return render(request, 'upload/upload.html')
    elif request.method == "POST":
        v=request.POST.get('user')
        print(v)
        V=request.POST.get('pwd')
        print(v)
        # radio
        v = request.POST.get('gender')
        print(v)
        v = request.POST.getlist('favor')
        print(v)
        v = request.POST.getlist('city')
        print(v)
        obj = request.FILES.get('fafafa')
        print(obj, type(obj), obj.name)
        import os
        file_path = os.path.join('upload', obj.name)
        print(file_path)
        f = open(file_path, mode="wb")
        for i in obj.chunks():
            f.write(i)
        f.close()
        from django.core.files.uploadedfile import InMemoryUploadedFile
        info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
        return render(request, 'upload/show.html', {'info_dict': info_dict})
        '''传输数据到后台，后台传输数据到前台，分别是html->views, views->html'''
        '''upload.html -> views ,  views ->show.html'''
    else:
        # PUT,DELETE,HEAD,OPTION...
        return redirect('/upload/')