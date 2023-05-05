from django.contrib import admin
from .models import Worker, ConstructionSite, Pylon, Job

# Register the Worker model with the Django admin site
admin.site.register(Worker)

# Register the ConstructionSite model with the Django admin site
admin.site.register(ConstructionSite)

# Register the Pylon model with the Django admin site
admin.site.register(Pylon)

# Register the Job model with the Django admin site
admin.site.register(Job)
