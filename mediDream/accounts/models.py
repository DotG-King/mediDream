from django.db import models

# Create your models here.

class MEMBERS(models.Model):
    m_id = models.CharField(db_column = 'M_ID', primary_key = True, max_length = 250)
    m_password = models.CharField(db_column = 'M_PASSWORD', max_length = 250)
    m_name = models.CharField(db_column = 'M_NAME', max_length = 250)

    # class Meta:
    #     managed = False
    #     db_table = 'members'