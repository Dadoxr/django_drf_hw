from django.db import models

class Payment(models.Model):
    pid = models.TextField(verbose_name='ID платежа')

    def __str__(self)
        return self.payment
    
    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

