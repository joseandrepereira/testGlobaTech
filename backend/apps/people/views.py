from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Person
from .serializers import PersonSerializer
from .services import PersonService

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(cpf__icontains=search_query)
            )
        return queryset

    @action(detail=True, methods=['get'])
    def calculate_ideal_weight(self, request, pk=None):
        person = self.get_object()
        ideal_weight = PersonService.calculate_ideal_weight(person)
        return Response({'ideal_weight': ideal_weight})