from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=404)
    lname = models.CharField(max_length=404)
    job = models.CharField(max_length=404)
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    title = models.CharField(max_length=404)
    number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=44)
    image = models.ImageField(upload_to='portfolio/')
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=77)
    lname = models.CharField(max_length=77)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    address = models.TextField()
    phone1 = models.CharField(max_length=44)
    phone2 = models.CharField(max_length=44)
    email = models.EmailField()


class HappyClients(models.Model):
    avatar = models.ImageField(upload_to="happies/")
    message = models.TextField(max_length=505)
    name = models.CharField(max_length=44)
    lname = models.CharField(max_length=44)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class WorkExp(models.Model):
    title = models.CharField(max_length=202)
    company = models.CharField(max_length=202)
    address = models.CharField(max_length=202)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=202)
    university = models.CharField(max_length=202)
    place = models.CharField(max_length=202)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    icon = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=202)
    about = models.TextField(max_length=404)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
