from django.db import models

class UserRegister(models.Model):
    idno = models.AutoField(primary_key=True,unique=True,default=True)
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField(default=True)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Nominations(models.Model):
    no = models.IntegerField()
    party_name = models.CharField(max_length=50)
    party_image = models.ImageField(upload_to='images/')

class ContestantVote(models.Model):
    voter_id = models.IntegerField(unique=True,default=True)
    voter_name = models.CharField(max_length=40)
    selected_party = models.CharField(max_length=50)
    selected_symbol = models.ImageField()
    def __str__(self):
        return self.voter_name

