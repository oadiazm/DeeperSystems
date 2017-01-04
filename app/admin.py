from django.contrib import admin
from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    model = Candidate
    list_display = (
        'name',
        'job_position',
        'email',
        'hours_per_week',
        'where_found_us',
        'country',
        'english_level',
    )


admin.site.register(Candidate, CandidateAdmin)
