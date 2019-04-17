from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http.response import JsonResponse
from .models import *

# Create your views here.


@csrf_exempt
def get_openid(request):
    js_code = request.POST.get('js_code')
    appid = "wxf9787b2035d7af14"
    secret = "68c1e24b48ceb6c21cff8dea895627ba"
    grant_type = "authorization_code"
    url = "https://api.weixin.qq.com/sns/jscode2session?appid=" + appid + "&secret=" + secret + "&js_code=" + js_code + "&grant_type=" + grant_type
    r = requests.get(url)
    openid = r.text.split(',')[1].split(':')[1].split('"')[1]
    session_key = r.text.split(',')[0].split(':')[1].split('"')[1]
    return JsonResponse({'openid':openid,'session_key':session_key})


@csrf_exempt
def test(request):
    return HttpResponse('Hello World')


@csrf_exempt
def create_user(request):
    openid = request.POST.get('openid')
    if(user_information.objects.filter(openid = openid)):
        return JsonResponse({'result':'您已创建过账户'})
    else:
        try:
            info = user_information()
            info.openid = request.POST.get('openid')
            info.nickname = request.POST.get('nickName')
            info.gender = request.POST.get('gender')
            info.city = request.POST.get('city')
            info.province = request.POST.get('province')
            info.country = request.POST.get('country')
            info.portrait = request.POST.get('portrait')
            info.save()
            return JsonResponse({'result':'账户创建成功！'})
        except:
            return JsonResponse({'result':'程序有bug，请联系刘启东'})


