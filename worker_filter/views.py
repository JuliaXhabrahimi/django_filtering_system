from django.http import HttpResponse
from rest_framework import viewsets, filters
from .models import Worker, ConstructionSite, Pylon, Job
from .serializers import WorkerSerializer, ConstructionSiteSerializer, PylonSerializer, JobSerializer
from django.db.models import Q

# Home view function to display a welcome message when accessing the root URL
def home(request):
    return HttpResponse("Welcome to the Construction Site Filtering System")

# Custom filter backend to filter workers based on their job status (busy or not_busy)
class JobStatusFilterBackend(filters.BaseFilterBackend):
    # Overrides filter_queryset method to apply the custom filtering logic
    def filter_queryset(self, request, queryset, view):
        # Get the job_status parameter from the request query parameters
        job_status = request.query_params.get('job_status', None)

        # If job_status is provided, apply the corresponding filter
        if job_status is not None:
            if job_status == 'busy':
                # Filter workers with active or pending jobs
                queryset = queryset.filter(job__state__in=['active', 'pending']).distinct()
            elif job_status == 'not_busy':
                # Filter workers without active or pending jobs
                queryset = queryset.exclude(job__state__in=['active', 'pending']).distinct()

        # Return the filtered queryset
        return queryset

# Custom filter backend to filter workers based on their work location(base or tip)
class WorkLocationFilterBackend(filters.BaseFilterBackend):
    # Overrides filter_queryset method to apply the custom filtering logic
    def filter_queryset(self, request, queryset, view):
        # Get the work_location parameter from the request query parameters
        work_location = request.query_params.get('work_location', None)

        # If work_location is provided, apply the corresponding filter
        if work_location is not None:
            if work_location == 'base':
                # Filter workers with jobs at the base of a pylon
                queryset = queryset.filter(job__is_base_work=True).distinct()
            elif work_location == 'tip':
                # Filter workers with jobs at the tip of a pylon
                queryset = queryset.filter(job__is_base_work=False).distinct()

        # Return the filtered queryset
        return queryset

# Custom filter backend to filter workers based on the date range of their jobs
class DateRangeFilterBackend(filters.BaseFilterBackend):
    # Overrides filter_queryset method to apply the custom filtering logic
    def filter_queryset(self, request, queryset, view):
        # Get the start_date and end_date parameters from the request query parameters
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        # If both start_date and end_date are provided, apply the date range filter
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(job__start_date__range=[start_date, end_date]).distinct()

        # Return the filtered queryset
        return queryset

# Custom filter backend to filter workers based on their job history
class JobHistoryFilterBackend(filters.BaseFilterBackend):
    # Overrides filter_queryset method to apply the custom filtering logic
    def filter_queryset(self, request, queryset, view):
        # Get the job_history parameter from the request query parameters
        job_history = request.query_params.get('job_history', None)

        # If job_history is provided, apply the corresponding filter
        if job_history is not None:
            if job_history == 'never_worked':
                # Filter workers who have never worked
                queryset = queryset.filter(job__isnull=True).distinct()
            elif job_history == 'worked':
                                # Filter workers who have worked at least once
                queryset = queryset.filter(job__isnull=False).distinct()

        # Return the filtered queryset
        return queryset

# WorkerViewSet to handle worker related API endpoints
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    # Register custom filter backends along with built-in search and ordering filters
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, JobStatusFilterBackend, WorkLocationFilterBackend, DateRangeFilterBackend, JobHistoryFilterBackend]
    search_fields = ['first_name', 'last_name', 'user_type']
    ordering_fields = ['first_name', 'last_name', 'user_type']

# ConstructionSiteViewSet to handle construction site related API endpoints
class ConstructionSiteViewSet(viewsets.ModelViewSet):
    queryset = ConstructionSite.objects.all()
    serializer_class = ConstructionSiteSerializer

# PylonViewSet to handle pylon related API endpoints
class PylonViewSet(viewsets.ModelViewSet):
    queryset = Pylon.objects.all()
    serializer_class = PylonSerializer

# JobViewSet to handle job related API endpoints
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

