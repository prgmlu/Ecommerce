from django.db import models

# Create your models here.

class Category(models.Model):
    """Model definition for Category."""

    name = models.TextField(primary_key = True, unique=True)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Product(models.Model):
    """Model definition for Product."""

    name = models.TextField()
    img = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img1 = models.ImageField( upload_to='uploads/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    img2 = models.ImageField( upload_to='uploads/', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    img3 = models.ImageField( upload_to='uploads/', height_field=None, width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

