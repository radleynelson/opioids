
from django.db import models

class BatchStatistics(models.Model):
    stddev = models.FloatField(db_column='stdDev', blank=True, null=True)  # Field name made lowercase.
    mean = models.FloatField(blank=True, null=True)
    meadian = models.FloatField(blank=True, null=True)
    mode = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    quartile1 = models.FloatField(blank=True, null=True)
    quartile3 = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    iqr = models.FloatField(db_column='IQR', blank=True, null=True)  # Field name made lowercase.
    upperbound = models.FloatField(db_column='upperBound', blank=True, null=True)  # Field name made lowercase.
    rank_coefficient = models.FloatField(blank=True, null=True)
    lastupdated = models.DateTimeField(db_column='lastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'batch_statistics'
        get_latest_by = 'lastupdated'



class Opioids(models.Model):
    drugname = models.CharField(db_column='DrugName', max_length=50)  # Field name made lowercase.
    isopioid = models.IntegerField(db_column='IsOpioid')  # Field name made lowercase.
    total_prescriptions = models.IntegerField(blank=True, null=True)
    risk_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opioids'


class Overdoses(models.Model):
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.
    deaths = models.IntegerField(db_column='Deaths')  # Field name made lowercase.
    percent = models.FloatField(db_column='Percent')  # Field name made lowercase.
    abbrev = models.CharField(db_column='Abbrev', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'overdoses'


class Prescribers(models.Model):
    doctorid = models.IntegerField(db_column='DoctorID')  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=50)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=50)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50)  # Field name made lowercase.
    overdoses = models.ForeignKey(Overdoses, models.DO_NOTHING, blank=True, null=True)
    credentials = models.CharField(db_column='Credentials', max_length=50, blank=True, null=True)  # Field name made lowercase.
    specialties = models.ForeignKey('Specialties', models.DO_NOTHING, blank=True, null=True)
    opioid_prescriber = models.IntegerField(db_column='Opioid_Prescriber')  # Field name made lowercase.
    totalprescriptions = models.IntegerField(db_column='TotalPrescriptions')  # Field name made lowercase.
    numberofopioidsprescribed = models.IntegerField(db_column='NumberOfOpioidsPrescribed', blank=True, null=True)  # Field name made lowercase.
    risk_rank = models.FloatField(db_column='Risk_Rank', blank=True, null=True)  # Field name made lowercase.
    isoutlier = models.BooleanField(db_column='IsOutlier', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prescribers'


class Specialties(models.Model):
    specialty = models.CharField(db_column='Specialty', max_length=100)  # Field name made lowercase.
    specialty_category = models.ForeignKey('SpecialtyCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'specialties'


class SpecialtyCategory(models.Model):
    category = models.CharField(db_column='Category', max_length=50)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specialty_category'



class Triple(models.Model):
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.
    prescribers = models.ForeignKey(Prescribers, models.DO_NOTHING, blank=True, null=True)
    opioids = models.ForeignKey(Opioids, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'triple'
