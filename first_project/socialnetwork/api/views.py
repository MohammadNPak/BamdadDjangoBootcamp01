from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from socialnetwork.api.serializer import LikeSerializer
from accounts.models import UserProfile

# class LikesView(APIView):
#     queryset = UserProfile.objects.all()
#     def get(self,request,format=None):
#         user = UserProfile.objects.all()
#         a = LikeSerializer(data=user)
#         a.is_valid()
#         return Response(a.data)

#     def post(self,request,format=None):
#         pass



# @api_view(['GET','POST'])
# def like_view(request):
#     return Response({"message": "Hello, world!"})

