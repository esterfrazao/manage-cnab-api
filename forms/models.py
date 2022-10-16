from django.db import models


class ModelFileForm(models.Model):
    file = models.FileField(upload_to="files/database/")
