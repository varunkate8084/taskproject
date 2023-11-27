from django.db import models

class UserProfile(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    user_status = models.CharField(max_length=20, choices=[('doctor', 'Doctor'), ('patient', 'Patient')])
    password = models.CharField(max_length=100)  # Note: In a real-world scenario, you should use a more secure method for storing passwords
    confirmpassword = models.CharField(max_length=100)
    email = models.EmailField()
    profile = models.ImageField(upload_to='profile_images/')  # 'profile_images/' is the directory where images will be stored

    def __str__(self):
        return f"{self.firstname} {self.lastname}"