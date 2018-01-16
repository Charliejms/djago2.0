from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View

from users.api.serializers import UserSerializers

from rest_framework.renderers import JSONRenderer


class SampleAPI(View):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        serializer_users = serializer.data
        rendered = JSONRenderer()
        json_user = rendered.render(serializer_users)
        return HttpResponse(json_user)
