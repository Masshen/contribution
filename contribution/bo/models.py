from django.db import models

class Medias(models.Model):
    alt = models.fields.CharField(null=True,max_length=255)
    file= models.fields.CharField(null=False,max_length=255)
    thumb=models.fields.CharField(null=True,max_length=255)
    type=models.fields.CharField(null=True,max_length=255)
    variants=models.JSONField(null=True)
    description=models.fields.TextField(null=True)

class Apps(models.Model):
    name = models.fields.CharField(null=False,max_length=255)
    poster= models.ForeignKey(Medias,on_delete=models.CASCADE,null=True)
    description=models.fields.TextField(null=True)

class Languages(models.Model):
    name=models.fields.CharField(null=False,max_length=255)
    acronym=models.fields.CharField(null=True,max_length=20)
    app=models.ForeignKey(Apps,on_delete=models.CASCADE)

class Sequences(models.Model):
    name=models.fields.CharField(null=False,max_length=255)
    poster= models.ForeignKey(Medias,on_delete=models.CASCADE,null=True)
    language=models.ForeignKey(Languages,on_delete=models.CASCADE)
    template=models.fields.CharField(null=True,max_length=255,null=True)

class Pages(models.Model):
    name=models.fields.CharField(null=False,max_length=255)
    description=models.fields.TextField(null=True)
    template=models.fields.CharField(null=True,max_length=255)
    sequence=models.ForeignKey(Sequences,on_delete=models.CASCADE)

class Questions(models.Model):
    description=models.fields.TextField(null=True)
    position=models.fields.IntegerField(null=True)
    poster= models.ForeignKey(Medias,on_delete=models.CASCADE,null=True)
    page=models.ForeignKey(Pages,on_delete=models.CASCADE)

class Answers(models.Model):
    text=models.fields.TextField()
    position=models.fields.IntegerField(null=True)
    isRight=models.fields.BooleanField(null=True)
    image= models.ForeignKey(Medias,on_delete=models.CASCADE,related_name="image",null=True)
    video= models.ForeignKey(Medias,on_delete=models.CASCADE,related_name="video",null=True)
    audio= models.ForeignKey(Medias,on_delete=models.CASCADE,related_name="audio",null=True)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
