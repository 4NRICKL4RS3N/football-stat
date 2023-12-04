from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection 

from .serializers import GeneralStatSerializer

class StatView(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM v_defense_general;")
            rows = cursor.fetchall()
        
        data = [{'equipe': row[0], 'competition': row[1], 'buts': row[2], 'tirs_pm': row[3], 'carton_j': row[4], 'carton_r': row[5], 'possession': row[6], 'passes_reussies': row[7], 'aeriens_gagnes': row[8], 'note': row[9]} for row in rows]
        serializer = GeneralStatSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)