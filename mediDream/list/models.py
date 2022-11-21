from django.db import models

# Create your models here.

class Search_History(models.Model):
    h_id = models.OneToOneField('accounts.Members', models.DO_NOTHING, db_column='H_ID', primary_key = True, to_field = 'm_id')
    h_date = models.DateField(db_column = 'H_DATE')
    h_druginfo = models.ForeignKey('druginfo', models.DO_NOTHING, db_column = 'H_DRUGINFO', to_field = 'd_info')

    # class Meta:
    #     managed = False
    #     db_table = 'search_history'

class DRUGINFO(models.Model):
    d_drugname = models.CharField(db_column = 'd_drugname', primary_key = True, max_length = 250)
    d_effect = models.CharField(db_column = 'd_effect', max_length = 250)
    d_usage = models.CharField(db_column = 'd_usage', max_length = 250)
    d_volume = models.CharField(db_column = 'd_volume', max_length = 250)
    d_info = models.CharField(db_column = ' d_info', unique = True, max_length = 250)
    
    # class Meta:
    #     managed = False
    #     db_table = 'druginfo'