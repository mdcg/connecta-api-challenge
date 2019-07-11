from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Post
from api.serializers.posts_serializers import PostSerializer
from api.utils.custom_paginations import Pagination


class PostView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        posts = request.user.posts.all()

        paginator = Pagination()
        result_page = paginator.paginate_queryset(
            posts, request)

        serialized_posts = PostSerializer(result_page, many=True)

        response_data = {
            'status': 'success',
            'data': paginator.get_paginated_response({
                'posts': serialized_posts.data,
            }),
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        post_to_register = PostSerializer(data=request.data)

        if post_to_register.is_valid():
            post = post_to_register.save(user=request.user)

            serialized_post = PostSerializer(post)

            response_data = {
                'status': 'success',
                'data': {
                    'post': serialized_post.data,
                },
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {
            'status': 'fail',
            'data': post_to_register.errors,
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class PostDetailsView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, post_id, format=None):
        try:
            post = Post.objects.get(
                id=post_id,
                user=request.user
            )
        except ObjectDoesNotExist:
            response_data = {
                'status': 'fail',
                'data': None,
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        serialized_post = PostSerializer(post)

        response_data = {
            'status': 'success',
            'data': {
                'post': serialized_post.data,
            },
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, post_id, format=None):
        try:
            post = Post.objects.get(
                id=post_id,
                user=request.user
            )
        except ObjectDoesNotExist:
            response_data = {
                'status': 'fail',
                'data': None,
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        post_informations_to_update = PostSerializer(
            post, data=request.data, partial=True)

        if post_informations_to_update.is_valid():
            post = post_informations_to_update.save()

            serialized_post = PostSerializer(post)

            response_data = {
                'status': 'success',
                'data': {
                    'post': serialized_post.data,
                },
            }
            return Response(response_data, status=status.HTTP_200_OK)

        response_data = {
            'status': 'fail',
            'data': post_informations_to_update.errors,
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, format=None):
        try:
            post = Post.objects.get(
                id=post_id,
                user=request.user
            )
        except ObjectDoesNotExist:
            response_data = {
                'status': 'fail',
                'data': None,
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        serialized_post = PostSerializer(post)

        post.delete()

        response_data = {
            'status': 'success',
            'data': {
                'post': serialized_post.data,
            },
        }
        return Response(response_data, status=status.HTTP_200_OK)
