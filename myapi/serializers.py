from rest_framework import serializers

class GeneralStatSerializer(serializers.Serializer):
    equipe = serializers.CharField()
    competition = serializers.CharField()
    buts = serializers.IntegerField()
    tirs_pm = serializers.DecimalField(6, 2)
    carton_j = serializers.IntegerField()
    carton_r = serializers.IntegerField()
    possession = serializers.DecimalField(6, 2)
    passes_reussies = serializers.DecimalField(6, 2)
    aeriens_gagnes = serializers.DecimalField(6, 2)
    note = serializers.DecimalField(6, 2)