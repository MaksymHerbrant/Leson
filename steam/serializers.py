from steam.models import Mail, Game, Account
from rest_framework import routers, serializers, viewsets

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = [
            'login', 'password', 'coast', 'description'
        ]
