from django.urls import path
from .apis import CompareAPI

urlpatterns = [
    path('compare', CompareAPI.as_view())
]
