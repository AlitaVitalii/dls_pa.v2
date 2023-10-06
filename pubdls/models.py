from datetime import date

from django.db import models

# Create your models here.


class Regnum(models.Model):
    reg_num = models.CharField(max_length=100, verbose_name='№ документу')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')
    reg_date = models.DateField(verbose_name='Дата документу')
    doc_type = models.CharField(max_length=100, verbose_name='Тип документу')
    rp_number = models.CharField(max_length=100, verbose_name='№ РП ЛЗ')
    drug_name = models.TextField(max_length=1000, verbose_name='Назва ЛЗ, форма випуску')
    serial_num = models.CharField(max_length=100, verbose_name='Серія №')
    manufacture = models.CharField(max_length=255, verbose_name='Назва виробника, країна')
    notes = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Додаткова інформація')

    def __str__(self):
        return self.reg_num
