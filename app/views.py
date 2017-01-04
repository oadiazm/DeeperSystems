# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from .models import Candidate
from .serializers import CandidateSerializerVersion1


class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows candidates to be viewed or edited.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializerVersion1
