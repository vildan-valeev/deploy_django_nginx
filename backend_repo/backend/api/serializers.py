from rest_framework.serializers import ModelSerializer

from .models import Foo


# -----------------------
class FooSerializer(ModelSerializer):
    """ """

    class Meta:
        model = Foo
        fields = '__all__'
