import datetime

from .models import UserActivity


class UpdateLastActivityMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            user, created = UserActivity.objects.get_or_create(user=request.user)
            user.last_request = datetime.datetime.now()
            user.save()
