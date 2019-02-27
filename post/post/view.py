from django.http import HttpResponse
import json
 
 
# 定义功能,字符串拼接
def add_args(a, b):
    return a+b
 
# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic={}
        # 判断是否传参
        if request.POST:
            a= request.POST.get('a', 0)
            b = request.POST.get('b', 0)
            # 判断参数中是否含有a和b
            if a and b:
                res = add_args(a, b)
                print(res)
                print(type(res))
                dic['number'] = res
                print(type(dic))
                print(dic)
                dic = json.dumps(dic)

                print(dic)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
 
    else:
        return HttpResponse('方法错误')