from django.urls import path
from . import views

urlpatterns=[
    # path("january",views.january),
    # path("february",views.february),

    #Dynamic path segment using placeholder
    path("<month>",views.monthly_challenge)
]