from django.db import models



class Order(models.Model):

    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tran_id = models.CharField(max_length=50)
    val_id = models.CharField(max_length=75)
    card_type = models.CharField(max_length=150)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(max_length=55, null=True)
    bank_tran_id = models.CharField(max_length=155, null=True)
    status = models.CharField(max_length=55)
    tran_date = models.DateTimeField()
    currency = models.CharField(max_length=50)
    card_issuer = models.CharField(max_length=255)
    card_brand = models.CharField(max_length=50)
    card_issuer_country = models.CharField(max_length=55)
    card_issuer_country_code = models.CharField(max_length=55)
    verify_sign = models.CharField(max_length=155)
    risk_level = models.CharField(max_length=50)
    risk_title = models.CharField(max_length=50)


    def __str__(self):
        return self.name
