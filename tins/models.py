from django.db import models
import random
# Create your models here.
class Tins(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True)

    def serialize(self):
        return {
            "id":self.id,
            "content": self.content,
            "likes": random.randint(0,200)
        }

