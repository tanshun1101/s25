from django.utils.deprecation import MiddlewareMixin
from web import models


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """如果用户已登陆， 则request 中赋值"""
        user_id = request.session.get('user_id')

        user_object = models.UserInfo.objects.filter(id=user_id).first()
        request.tracer = user_object
