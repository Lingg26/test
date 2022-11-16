from rest_framework import serializers
from tutorials.models import tutorial
class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model= tutorial
        fields=('id','title','slug','createdAt')