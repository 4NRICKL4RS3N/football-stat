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

class AttaqueStatSerializer(serializers.Serializer):
    equipe = serializers.CharField()
    competition = serializers.CharField()
    tirs_pm = serializers.DecimalField(6, 2)
    tirs_ca_pm = serializers.DecimalField(6, 2)
    dribbles_pm = serializers.DecimalField(6, 2)
    fautes_subies_pm = serializers.DecimalField(6, 2)
    note = serializers.DecimalField(6, 2)

class DefenseStatSerializer(serializers.Serializer):
    equipe = serializers.CharField()
    competition = serializers.CharField()
    tirs_pm = serializers.DecimalField(6, 2)
    tacles_pm = serializers.DecimalField(6, 2)
    interceptions_pm = serializers.DecimalField(6, 2)
    fautes_pm = serializers.DecimalField(6, 2)
    hors_jeux_pm = serializers.DecimalField(6, 2)
    note = serializers.DecimalField(6, 2)