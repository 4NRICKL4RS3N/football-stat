from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection 

from .serializers import *

class GeneralGeneralView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM v_general_general;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'buts': row[2], 'tirs_pm': row[3], 'carton_j': row[4], 'carton_r': row[5], 'possession': row[6], 'passes_reussies': row[7], 'aeriens_gagnes': row[8], 'note': row[9]} for row in rows]
        serializer = GeneralStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

class GeneralDomicilView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM v_general_domicile;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'buts': row[2], 'tirs_pm': row[3], 'carton_j': row[4], 'carton_r': row[5], 'possession': row[6], 'passes_reussies': row[7], 'aeriens_gagnes': row[8], 'note': row[9]} for row in rows]
        serializer = GeneralStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

class GeneralExterieurView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM v_general_exterieur;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'buts': row[2], 'tirs_pm': row[3], 'carton_j': row[4], 'carton_r': row[5], 'possession': row[6], 'passes_reussies': row[7], 'aeriens_gagnes': row[8], 'note': row[9]} for row in rows]
        serializer = GeneralStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

class DefenseGeneralView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM V_DEFENSE_GENERAL;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'tirs_pm': row[2], 'tacles_pm': row[3], 'interceptions_pm': row[4], 'fautes_pm': row[5], 'hors_jeux_pm': row[6], 'note': row[7]} for row in rows]
        serializer = DefenseStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

class DefenseDomicilView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM v_defense_domicile;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'tirs_pm': row[2], 'tacles_pm': row[3], 'interceptions_pm': row[4], 'fautes_pm': row[5], 'hors_jeux_pm': row[6], 'note': row[7]} for row in rows]
        serializer = DefenseStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

class DefenseExterieurView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM v_defense_exterieur;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'tirs_pm': row[2], 'tacles_pm': row[3], 'interceptions_pm': row[4], 'fautes_pm': row[5], 'hors_jeux_pm': row[6], 'note': row[7]} for row in rows]
        serializer = DefenseStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

class AttaqueGeneralView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM V_ATTAQUE_GENERAL;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'tirs_pm': row[2], 'tirs_ca_pm': row[3], 'dribbles_pm': row[4], 'fautes_subies_pm': row[5], 'note': row[6]} for row in rows]
        serializer = AttaqueStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

class AttaqueDomicilView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM v_attaque_domicile;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'tirs_pm': row[2], 'tirs_ca_pm': row[3], 'dribbles_pm': row[4], 'fautes_subies_pm': row[5], 'note': row[6]} for row in rows]
        serializer = AttaqueStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

class AttaqueExterieurView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM v_attaque_exterieur;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'tirs_pm': row[2], 'tirs_ca_pm': row[3], 'dribbles_pm': row[4], 'fautes_subies_pm': row[5], 'note': row[6]} for row in rows]
        serializer = AttaqueStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)