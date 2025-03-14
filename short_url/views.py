from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from short_url.models import ShortUrl
from short_url.serializers import ShortUrlSerializer


class CreateShortUrl(APIView):
    def post(self, request):
        serializer = ShortUrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetOriginalUrl(APIView):
    def get(self, request, short_url):
        try:
            short_url_obj = ShortUrl.objects.get(short_url=short_url)
            return Response({"Location": short_url_obj.full_url}, status=status.HTTP_307_TEMPORARY_REDIRECT)
        except ShortUrl.DoesNotExist:
            return Response({"error": "Нет соответствия"}, status=status.HTTP_404_NOT_FOUND)
