from django.shortcuts import redirect


# 中间件
class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        urls = [
            '/login/login/',
            '/login/ajaxlogin/'
        ]
        # 如果已经登陆（可以获取id），或者传送的是以上两个地址，则允许传输
        if request.session.get('id') or request.path_info in urls:
            response = self.get_response(request)
            return response
        else:
            # 未登录则传送回登陆地址
            return redirect('/login/login/')
