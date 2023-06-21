from django.db import models

class Agent(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    varsta = models.IntegerField()
    telefon = models.CharField(max_length=10)

    def __str__(self):
        return self.nume + self.prenume
    
class Apartament(models.Model):
    etaj = models.IntegerField( )
    nrCamere = models.IntegerField()
    pret = models.IntegerField()
    metriPatrati = models.IntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + 'E' + str(self.etaj) + 'N' + str(self.nrCamere)

