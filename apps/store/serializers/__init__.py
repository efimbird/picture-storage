from rest_framework import serializers
from apps.store.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    """
    Serializes a Picture model data to JSON
    """

    class Meta:
        model = Picture
        fields = (
            'id', 'image', 'image_small_url', 'category', 'title', 'description', 'upload_time',
            'is_narrow', 'is_wide'
        )

    image_small_url = serializers.CharField(source='image_small.url', read_only=True)
