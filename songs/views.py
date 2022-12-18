from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        Album_id = self.kwargs["pk"]
        Album_obj = get_object_or_404(Album, pk=Album_id)
        songs = Song.objects.filter(album=Album_obj)
        return songs

    def perform_create(self, serializer):
        serializer.save(album_id=self.kwargs.get("pk"))
