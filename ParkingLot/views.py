from django.shortcuts import render
from .models import *
'''
Variable "context" is data container for index page.
That data is just for test.
It will be connectd to DB.

이 변수 "context"는 "Main/index.html" 페이지를 위한 데이터 컨테이너입니다.
현재 데이터는 테스트만을 위한 것이며, 추후 DB와 연결시킬 예정입니다.
'''
context = {}

def guest(request):
    template = "ParkingLot/guest.html"
    return render(request, template, context)

def input(request):
    template = "ParkingLot/input.html"
    return render(request, template, context)

'''
This function do logout and refresh the page.
이 함수는 로그아웃하고 페이지를 새로고침합니다.
'''
def logout(request):
    context
    context["islogin"] = False
    template = "ParkingLot/index.html"
    return render(request, template, context)


'''
This function is default page loader.
이 함수는 페이지를 로드해오는 기본 함수입니다.
'''
def index(request):
    template = 'ParkingLot/index.html'
    return render(request,template, context)