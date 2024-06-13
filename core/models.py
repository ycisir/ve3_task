from django.db import models

class UploadedCSV(models.Model):
    csv_file = models.FileField(upload_to='uploads/')