from .models import Candidate
from rest_framework.serializers import HyperlinkedModelSerializer


class CandidateSerializerVersion1(HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = (
            'url',
            'name',
            'job_position',
            'email',
            'hours_per_week',
            'where_found_us',
            'country',
            'english_level',
            'comments',
        )
