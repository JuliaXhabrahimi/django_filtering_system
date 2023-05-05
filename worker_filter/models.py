from django.db import models

# Worker model representing a system user who can be assigned jobs
class Worker(models.Model):
    # Define fields for the Worker model with appropriate data types and constraints
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    user_type = models.CharField(max_length=50)

    # Define the string representation of the Worker model
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# ConstructionSite model representing a construction site with associated pylons
class ConstructionSite(models.Model):
    # Define fields for the ConstructionSite model with appropriate data types and constraints
    name = models.CharField(max_length=100)

    # Define the string representation of the ConstructionSite model
    def __str__(self):
        return self.name

# Pylon model representing a pylon at a construction site
class Pylon(models.Model):
    # Define a foreign key relationship to the ConstructionSite model with a cascade delete behavior
    construction_site = models.ForeignKey(ConstructionSite, on_delete=models.CASCADE)
    # Define fields for the Pylon model with appropriate data types and constraints
    pylon_number = models.IntegerField()
    base_area = models.FloatField()
    tip_surface = models.FloatField()
    total_area = models.FloatField()

    # Define the string representation of the Pylon model
    def __str__(self):
        return f"Pylon {self.pylon_number} at {self.construction_site.name}"

# Job model representing a job assigned to a worker at a pylon
class Job(models.Model):
    # Define the possible job states as constants
    ACTIVE = 'active'
    CANCELLED = 'cancelled'
    PENDING = 'pending'
    FINISHED = 'finished'
    
    # Define a list of tuples with the job states and their display names
    JOB_STATES = [
        (ACTIVE, 'Active'),
        (CANCELLED, 'Cancelled'),
        (PENDING, 'Pending'),
        (FINISHED, 'Finished'),
    ]

    # Define foreign key relationships to the Worker and Pylon models with cascade delete behavior
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='jobs')
    pylon = models.ForeignKey(Pylon, on_delete=models.CASCADE)
    # Define a state field with the JOB_STATES as choices
    state = models.CharField(max_length=10, choices=JOB_STATES)
    start_date = models.DateField()
    # Define an optional end_date field, allowing it to be null and blank
    end_date = models.DateField(null=True, blank=True)
    # Define a boolean field to indicate whether the job involves base work
    is_base_work = models.BooleanField()

    # Define the string representation of the Job model
    def __str__(self):
        return f"Job for {self.worker} at Pylon {self.pylon.pylon_number} - {self.state}"
