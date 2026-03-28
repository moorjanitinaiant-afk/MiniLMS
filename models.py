from django.db import models

class Semester(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Unit(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Video(models.Model):
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField(blank=True)

    def get_embed_url(self):
        if "watch?v=" in self.video_url:
            return self.video_url.replace("watch?v=","embed/")
        return self.video_url

    def __str__(self):
        return self.title


class PDF(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title