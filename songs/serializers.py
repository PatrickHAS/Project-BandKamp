from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    # album_id = serializers.SerializerMethodField()

    # def get_album_id(self, obj: Song):
    #     return obj.album.name

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "duration",
            "album_id",
        ]

    read_only_fields = ["album_id"]

    def create(self, validated_data: dict) -> Song:
        return Song.objects.create(**validated_data)
