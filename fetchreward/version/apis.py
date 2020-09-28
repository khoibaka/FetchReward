from django.http import JsonResponse
from rest_framework import generics, permissions
import re
from .helpers import compare, is_software_version

pattern_check = re.compile(r"(\[0-9\]+\[\.\]?)+")

class CompareAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def get(self, *args, **kwargs):
        
        # Error checking for first number
        first = self.request.GET.get('first')
        if not first or not is_software_version(first):
            return JsonResponse({
                'message': 'First input missing or wrong form.'
            }, status= 400)

        # Error checking for second number
        second = self.request.GET.get('second')
        if not second or not is_software_version(second):
            return JsonResponse({
                'message': 'Second input missing or wrong form.'
            }, status= 400)

        return JsonResponse({'result': compare(first, second)}, safe=True)
        