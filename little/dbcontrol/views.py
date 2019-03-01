from django.shortcuts import render
from django.http import HttpResponse
from .models import Link
# Create your views here.
def show_data(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
	a = Link.objects.all()
	print(a)
	if request.method == "GET":
		print(request)
		btn_name=request.GET.get('btn_name')
		print(btn_name)
		link_name=request.GET.get('link_name')
		print(link_name)
	if request.method == "POST":
		btn_name=request.POST.get('btn_name')
		print(btn_name)
		link_name=request.POST.get('link_name')
		print(link_name)
		#print(Link.objects.filter(btn_name=btn_name))
		if Link.objects.filter(btn_name=btn_name):#用btn_namer
			print("111111111111111111111")
			print("该数据已存在！")
			
		else:
			print("222222222222222222222")
			Link.objects.create(btn_name=btn_name,link_name=link_name)
		#Link.objects.create(btn_name=btn_name,link_name=link_name)
		#Link.objects.filter(link_name__contains=link_name).delete()
		#Link.objects.filter(btn_name__exact=btn_name).delete()
		#Link.objects.filter(btn_name=btn_name).update(link_name=link_name)
	link_dict ={}
	for item in a:
		print(item)
		print(item._id)
		print(item.btn_name)
		print(item.link_name)
		link_dict[item._id]={"btn_name":item.btn_name,"link_name":item.link_name}
	print(link_dict)
	return render(request,"dbcontrol/show.html",{"link_dict":link_dict})

def create_data(request):
	Link.objects.get_or_create(btn_name="QQ",link_name="http://www.qq.com")

	return HttpResponse("Hello, world. You're at the create_data index.")