# coding:utf-8
from rest_framework import serializers
from .models import UserFav
from rest_framework.validators import UniqueTogetherValidator


# Author:Nan ji dong

class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=("user", "goods"),
                message="已经收藏"
            )
        ]
        fields = ("user", "goods", "id")