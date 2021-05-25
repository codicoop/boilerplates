from django.db import models


class City(models.Model):
    class Meta:
        verbose_name = "població"
        verbose_name_plural = "poblacions"
        ordering = ['name_order', ]

    created = models.DateTimeField("creació", auto_now_add=True)
    code = models.CharField("Codi 10", max_length=10)
    name_order = models.CharField("ordenació alfabètica", max_length=250)
    name = models.CharField("municipi", max_length=250)
    county = models.CharField("comarca", max_length=250)
    county_code = models.CharField("codi comarca", max_length=10)
    province = models.CharField("província", max_length=250)
    province_code = models.CharField("codi província", max_length=10)
    postal_code = models.CharField(
        "codi postal", max_length=5,
        null=True, blank=True)

    def __str__(self):
        return self.name
