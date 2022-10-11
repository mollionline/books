import json


from django.http import JsonResponse, Http404
from rest_framework.authtoken.admin import User
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from catalog.models import Genre, get_user_model
from catalog.serializers import BookSerializer


class CreateBookAPIView(GenericAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Genre.objects.all()

    def get_object(self, id):
        try:
            return Genre.objects.get(id=id)
        except Genre.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        genre = self.get_object(id=data['genre'][0]['id'])
        print(genre, 'genre')
        # print(data['author'][0]['id'])
        print(data)
        author = User.objects.get(id=data['author'][0]['id'])
        seriaizer = BookSerializer(data=data)

        if seriaizer.is_valid():
            seriaizer.validated_data['genre'] = genre
            try:
                book = seriaizer.save()
                book.author.add(author)
            except Exception as e:
                print(e, 5555555555)
                raise e
            return JsonResponse(seriaizer.data, safe=False)
        response = JsonResponse({'errors': seriaizer.errors})
        response.status_code = 400
        return response
