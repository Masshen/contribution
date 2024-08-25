from django.db import models

class Medias(models.Model):
    alt = models.fields.CharField(null=True,max_length=255)
    file= models.fields.CharField(null=False,max_length=255)
    thumb=models.fields.CharField(max_length=255)
    type=models.fields.CharField(max_length=255)
    variants=models.JSONField()
    description=models.fields.TextField()

class Apps(models.Model):
    name = models.fields.CharField(null=False,max_length=255)
    poster= models.ForeignKey(Medias,on_delete=models.CASCADE)
    description=models.fields.TextField()

class Languages(models.Model):
    name=models.fields.CharField(null=False,max_length=255)
    acronym=models.fields.CharField(null=True,max_length=20)
    app=models.ForeignKey(Apps,on_delete=models.CASCADE)

class Sequences(models.Model):
    name=models.fields.CharField(null=False,max_length=255)
    poster= models.ForeignKey(Medias,on_delete=models.CASCADE)
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
    poster= models.ForeignKey(Medias,on_delete=models.CASCADE)
    page=models.ForeignKey(Pages,on_delete=models.CASCADE)

class Answers(models.Model):
    text=models.fields.TextField()
    position=models.fields.IntegerField()
    isRight=models.fields.BooleanField()
    image= models.ForeignKey(Medias,on_delete=models.CASCADE,related_name="image")
    video= models.ForeignKey(Medias,on_delete=models.CASCADE,related_name="video")
    audio= models.ForeignKey(Medias,on_delete=models.CASCADE,related_name="audio")
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
