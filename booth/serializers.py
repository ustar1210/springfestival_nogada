from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = LogoImage
        fields = [
            "image",
        ]

class BoothListSerializer(serializers.ModelSerializer):

    like_cnt=serializers.IntegerField()
    logo_image = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_logo_image(self, instance):
        logoimage = instance.logoimages.first()
        try :
            logoimage_serializer = ImageSerializer(logoimage)
            return logoimage_serializer.data["image"]
        except:
            return None
    
    def get_is_liked(self, instance):
        #아직 구현 안함
        return None

    class Meta:
        model = Booth
        fields = [
            "id",
            "name",
            "type",
            "operator",
            "logo_image",
            "like_cnt",
            "start_at",
            "end_at",
            "location",
            "is_liked",
        ]

class BoothDetailSerializer(serializers.ModelSerializer):
    
    like_cnt=serializers.IntegerField()
    logo_image = serializers.SerializerMethodField()
    menu_image = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_logo_image(self, instance):
        logoimage = instance.logoimages
        try :
            logoimage_serializer = ImageSerializer(logoimage, many=True)
            outcome = []
            for data in logoimage_serializer.data:
                outcome.append(data["image"])
            return outcome
        except:
            return None
    
    def get_menu_image(self, instance):
        menuimage = instance.menuimages
        try :
            menuimage_serializer = ImageSerializer(menuimage, many=True)
            outcome = []
            for data in menuimage_serializer.data:
                outcome.append(data["image"])
            return outcome
        except:
            return None

    def get_is_liked(self, instance):
        #아직 구현 안함
        return None
    
    class Meta:
        model = Booth
        fields = [
            "id",
            "name",
            "type",
            "operator",
            "logo_image",
            "like_cnt",
            "start_at",
            "end_at",
            "location",
            "description",
            "menu",
            "menu_image",
            "concept",
            "is_liked",
            ]
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["booth", "key"]