from rest_framework import serializers

class ScrapperSerializer(serializers.Serializer):
   url = serializers.CharField()
   meta_title = serializers.CharField()
   description = serializers.CharField()
   photo_url = serializers.CharField()
   page_text = serializers.CharField()