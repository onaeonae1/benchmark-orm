from django.http import JsonResponse
from app.models import User
from django.db import connection
from django.db.models import Count


# ORM API
def orm_api(request):
    user_list = list(
        User.objects.values("email")
        .annotate(email_count=Count("email"))
        .order_by("-email_count")
    )
    return JsonResponse(user_list, safe=False)


def raw_sql_api(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT row_to_json(t) FROM (
                SELECT email, COUNT(*) as email_count 
                FROM app_user 
                GROUP BY email 
                ORDER BY email_count DESC
            ) t;
        """
        )
        result = cursor.fetchall()
    return JsonResponse(result, safe=False)
