from django.db import models

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=50)
    mileage_in_km = models.IntegerField()
    chassis_no = models.IntegerField()
    color = models.CharField(max_length=50)
    vehicle_model_id = models.ForeignKey('Vehicle_Model', on_delete=models.CASCADE, related_name="model")
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __self__(self):
        return self.license_plate

class Vehicle_Model(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __self__(self):
        return self.brand + ' ' + self.name
    