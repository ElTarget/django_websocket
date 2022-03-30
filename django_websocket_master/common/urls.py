from django.urls import path
from views import ( index_handler)

urlpatterns = [
    # 前台用户信息管理及登录登出
    # path('login/', login_handler, name='login'),
    # path('logout/', logout_handler, name='logout'),
    path('index/', index_handler, name='index')]