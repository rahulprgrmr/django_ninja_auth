from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Timestamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Audit(models.Model):
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        abstract = True
