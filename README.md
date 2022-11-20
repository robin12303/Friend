# 참고사항

* **urls.py의 name에 대해**

    ```django html
    urlpatterns = [
        path('', views.index, name='main_index'),
        path('logout', views.logout, name='main_logout'),
    ]
    ```
    (이 부분)

    각 __app__ 의 __urls.py__ 를 보시면 name 이

    > (소문자 app이름)_(views.py의 함수명)

    으로 해 둔 것을 보실 수 있습니다.  
    이것은 html에서
    ```django html
    <form action = {% url '~~' %}>
    </form>
    ```
    을 사용하기 위한 방법으로, 원래는  
    > {% url '(app이름):(name)' %}

    의 형태로 사용 가능하지만,  
    의도대로 동작하지 않고 버그가 생겨서  
    모든 app의 urls.py 에 있는 name 을 겹치지 않게 하도록 하였습니다.