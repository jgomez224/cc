# myapi/serializers.py
from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('name','location','vehicle','human')

# You just created a new serializer for your model including
# the Character class fields: name, location, vehicle and human
# The code above will create a new serialised object (JSON) with the given fields.
# The serializer will allow data transformation, from database data to JSON format.