# django_websocket

#### Description
    计划实现一个 Django 实现 websoket 通信
django_websocket 
####
    consumers.py: 相当于 django 的视图.    
    routing.py: 相当于 django 的 urls.py.   
    websocket 中的 url 和执行函数的对应关系。   
    根据映射关系，当websocket的请求进来的时候，根据用户的请求来触发我们的consumers.py里的方法。