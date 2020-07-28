from django.db import models


class Style_Tr(models.Model):
    img_content = models.ImageField(upload_to='images/',
                                    null=True, blank=True)
    img_style = models.ImageField(upload_to='images/',
                                  null=True, blank=True)

    def __str__(self):
        return "Style Transfer Form"
