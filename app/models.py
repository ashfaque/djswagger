from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class SwaggerTest(models.Model):

    test_txt = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'swagger_test'
