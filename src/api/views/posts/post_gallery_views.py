from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Post
from api.serializers.posts_serializers import PostListSerializer
from api.utils.custom_paginations import Pagination


class GalleryView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        posts = Post.objects.all()

        paginator = Pagination()
        result_page = paginator.paginate_queryset(
            posts, request)

        serialized_posts = PostListSerializer(result_page, many=True)

        response_data = {
            'status': 'success',
            'data': paginator.get_paginated_response({
                'posts': serialized_posts.data,
            }),
        }
        return Response(response_data, status=status.HTTP_200_OK)