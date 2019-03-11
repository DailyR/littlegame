
from django.http import HttpResponse
# Create your views here.

# login/views.py
 
from django.shortcuts import render,redirect
from .models import User
from .models import Phone

def index(request):
    phone = Phone.objects.all()
    return render(request,'index.html', {'phone': phone,})

def login(request):

	if request.session.get('is_login',None):
		return redirect('/index')
	if request.method == "POST":

		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		print(username)
		print(password)
		message = "所有字段都必须填写！"
		if username and password:  # 确保用户名和密码都不为空
		    username = username.strip()
		    # 用户名字符合法性验证
		    # 密码长度验证
		    # 更多的其它验证.....
		    try:
		    	user = User.objects.get(name=username)
		    	if user.password == password:
		    		message = "登录成功"
		    		request.session['is_login'] = True
		    		request.session['user_id'] = user.id
		    		print(request.session['user_id'])
		    		request.session['user_name'] = user.name
		    		print(request.session['user_name'])
		    		return redirect('/login/index/')
		    	else:
		        	message = "密码不正确！"
		    except:
		        message = "用户名不存在！"
		return render(request, 'login.html', {"message": message})
	return render(request, 'login.html')
 

def register(request):

    if request.method == "POST":  # 获取数据
        username = request.POST.get('username')

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        print(email)
        sex = request.POST.get('sex')
        print(sex)
        if password1 != password2:  # 判断两次密码是否相同
            message = "两次输入的密码不同！"
            return render(request, 'register.html', locals())
        else:
            same_name_user = User.objects.filter(name=username)
            if same_name_user:  # 用户名唯一
                message = '用户已经存在，请重新选择用户名！'
                return render(request, 'register.html', locals())
            same_email_user = User.objects.filter(email=email)
            if same_email_user:  # 邮箱地址唯一
                message = '该邮箱地址已被注册，请使用别的邮箱！'
                return render(request, 'register.html', locals())

            # 当一切都OK的情况下，创建新用户
            User.objects.create(name=username,password=password1,email=email,sex=sex)
            message = "恭喜您，注册成功！"

            return render(request, 'register.html', locals())
            #return redirect('/login/register/', locals())  # 自动跳转到登录页面

    return render(request, 'register.html', locals())
 
#def logout(request):
#    pass
#    request.session['is_login'] = False
#    return redirect('/login/index')

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/index/")
    request.session.flush()    #清除session的所有信息
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/index/")

def webye(request):  #flatlab例子，所有js，所有css，所有img听我号令

    phone = Phone.objects.all()
    for item in phone:
        print(item)
        print(item._id)
        print(item.device_name)
        print(item.pinpai)
        print(item.ram)
        print(item.cpu)
        print(item.system_version)
        print(item.holder_people)
    return render(request, 'index_table_for_flatlab.html', {'phone': phone,})


def contact(request):
    return HttpResponse("Hello, world. You're at the contact index.")


'''
def login(request):
    return HttpResponse("Hello, world. You're at the login index.")


def logout(request):
    return HttpResponse("Hello, world. You're at the logout index.")


def register(request):
    return HttpResponse("Hello, world. You're at the register index.")

def webye(request):
    return HttpResponse("Hello, world. You're at the webye index.")
'''