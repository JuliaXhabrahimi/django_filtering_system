from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Instantiate a DefaultRouter object to create standard RESTful endpoints for the registered models
router = DefaultRouter()
# Register the WorkerViewSet with the 'workers' endpoint
router.register(r'workers', views.WorkerViewSet)
# Register the ConstructionSiteViewSet with the 'construction-sites' endpoint
router.register(r'construction-sites', views.ConstructionSiteViewSet)
# Register the PylonViewSet with the 'pylons' endpoint
router.register(r'pylons', views.PylonViewSet)
# Register the JobViewSet with the 'jobs' endpoint
router.register(r'jobs', views.JobViewSet)

# Define urlpatterns for the app by including the router's generated URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
