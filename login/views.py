# login/views.py
 
from django.shortcuts import render,redirect
from .models import User

def index(request):
    pass
    return render(request,'index.html')

def login(request):
	print("111111111111111111111111111111")
	if request.session.get('is_login',None):
		return redirect('/login/index')
	if request.method == "POST":
		print("111111111111111111111111111111")
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
		    	print("22222222222222222222222222222222")
		    	user = User.objects.get(name=username)
		    	if user.password == password:
		    		message = "登录成功"
		    		print("3333333333333333333333333333333")
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
        print("22222222222222222")
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
            print("3333333333333333333333333333333")
            return render(request, 'register.html', locals())
            #return redirect('/login/register/', locals())  # 自动跳转到登录页面
    if request.method =="GET":
    	print("111111111111111111111111")
    print("4444444444444444444444444")
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
