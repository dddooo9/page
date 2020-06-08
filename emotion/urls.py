from django.urls import path
from .views import happy, sad, tired, angry, everyimg


app_name="emotion"
urlpatterns = [
    path('happy/', happy, name="happy"),
    path('sad/', sad, name="sad"),
    path('tired/', tired, name="tired"),
    path('angry/', angry, name="angry"),
    path('everyimg', everyimg, name="everyimg"),
]