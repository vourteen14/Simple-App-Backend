from django.urls import path
from .views import NgaranViews

urlpatterns = [
  path('ngaran/', NgaranViews.as_view()),
  path('ngaran/<int:id>', NgaranViews.as_view()),
]
