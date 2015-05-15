from django.db import models

class tCompany(models.Model):
    cName = models.CharField(max_length=200)
    cAdress = models.CharField(max_length=200)
    def __unicode__(self):
        return self.cName

class tUser(models.Model):
    cName = models.CharField(max_length=200)
    cSignCode = models.IntegerField()
    def __unicode__(self):
        return self.cName

class tWaybill(models.Model):
    cCompToID = models.ForeignKey(tCompany, null=True, blank=True, related_name='cCompToID')
    cCompFromID = models.ForeignKey(tCompany, null=True, blank=True, related_name='cCompFromID')
    cToID = models.ForeignKey(tUser, null=True, blank=True, related_name='cToID')
    cFromID = models.ForeignKey(tUser, null=True, blank=True, related_name='cFromID')
    cDate = models.CharField(max_length=200)
    cTotal = models.IntegerField()
    def __unicode__(self):
        return self.cDate

class tGoods(models.Model):
    cName = models.CharField(max_length=200)
    cQty = models.IntegerField()
    cPrice = models.IntegerField()
    cWaybillID = models.ForeignKey(tWaybill, null=True, blank=True)
    def __unicode__(self):
        return self.cName