from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=200)  
    description = models.TextField(null=True, blank=True)

    def __str__ (self):
        return self.name

class Snippet(models.Model):
    title = models.CharField(max_length=200) 
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    code = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return self.title