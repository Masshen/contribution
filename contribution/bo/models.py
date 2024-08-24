from django.db import models

class Apps(models.Model):
    name = models.fields.CharField(null=False,max_length=255)
    poster= models.fields.CharField(null=True,max_length=255)
    thumb=models.fields.CharField(max_length=255)
    description=models.fields.TextField()

class Languages(models.Model):
    name=models.fields.CharField(null=False,max_length=255)
    acronym=models.fields.CharField(null=True,max_length=20)
    app=models.ForeignKey(Apps,on_delete=models.CASCADE)

class Sequences(models.Model):
    name=models.fields.CharField(null=False,max_length=255)
    poster= models.fields.CharField(null=True,max_length=255)
    thumb=models.fields.CharField(max_length=255)
    language=models.ForeignKey(Languages,on_delete=models.CASCADE)
    template=models.fields.CharField(null=True,max_length=255)

class Pages(models.Model):
    name=models.fields.CharField(null=False,max_length=255)
    description=models.fields.TextField()
    template=models.fields.CharField(null=True,max_length=255)
    sequence=models.ForeignKey(Sequences,on_delete=models.CASCADE)

class Questions(models.Model):
    description=models.fields.TextField()
    position=models.fields.IntegerField()
    poster= models.fields.CharField(null=True,max_length=255)
    thumb=models.fields.CharField(max_length=255)
    page=models.ForeignKey(Pages,on_delete=models.CASCADE)

class Answers(models.Model):
    text=models.fields.TextField()
    position=models.fields.IntegerField()
    isRight=models.fields.BooleanField()
    image= models.fields.CharField(null=True,max_length=255)
    video= models.fields.CharField(null=True,max_length=255)
    audio= models.fields.CharField(null=True,max_length=255)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
