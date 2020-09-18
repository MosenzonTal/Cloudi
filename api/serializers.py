from rest_framework import serializers
from cloudinis.models import ActivatedPolicy, Violation


class ActivatedPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivatedPolicy
        fields = ('id', 'organization', 'policy', 'affectedResource', 'metadata', 'actionItem', 'resourceTagToNotify')


class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = ('id', 'connectedPolicy', 'resource_id', 'date', 'isChecked', 'isFixed', 'fixedDate')
