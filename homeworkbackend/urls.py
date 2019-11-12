from django.urls import path

from swengs.homeworkbackend import views

urlpatterns = [
    path('country/', views.country_list),
    path('country/<int:id>', views.country_update),

    path('soldier/', views.soldier_list),
    path('soldier/<int:id>', views.soldier_update)
]