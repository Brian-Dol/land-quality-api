from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Land(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    size_in_acres = models.DecimalField(max_digits=10, decimal_places=2)
    soil_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.location} - {self.size_in_acres} acres"

class LandQualityAssessment(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
    date_assessed = models.DateField(auto_now_add=True)
    ph_level = models.DecimalField(max_digits=5, decimal_places=2)
    moisture_content = models.DecimalField(max_digits=5, decimal_places=2)
    nutrient_levels = models.CharField(max_length=255)
    quality_score = models.IntegerField()

    def __str__(self):
        return f"Assessment for {self.land} on {self.date_assessed}"
