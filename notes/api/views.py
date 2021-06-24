from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)


class NoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

class NoteCreateAPIView(CreateAPIView):
    serializer_class = NoteSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]