from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

template = 'Main/index.html'
'''
Variable "context" is data container for "Main/index.html" page.
That data is just for test.
It will be connectd to DB.

이 변수 "context"는 "Main/index.html" 페이지를 위한 데이터 컨테이너입니다.
현재 데이터는 테스트만을 위한 것이며, 추후 DB와 연결시킬 예정입니다.
'''
context = {
    'islogin' : False,
    'id' : "adsf",
    'pw' : "asdf",
    'user_name': "adsf",
}

'''
This function is default page loader.
이 함수는 페이지를 로드해오는 기본 함수입니다.
'''
def index(request):
    context
    return render(request, template, context)