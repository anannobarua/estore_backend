from django.db import models

from django.urls import reverse
# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=250, db_index=True)
    
    slug = models.SlugField(max_length=250, unique=True) # url stuf
    
# define matadata
    class Meta:
        verbose_name_plural ='categories'
        
# category (1),category (1) # shirt # shoes

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        
        return reverse('list-category', args=[self.slug])


class Product(models.Model):
    
    #foreign key
    category = models.name = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE, null=True)
    
    title = models.CharField(max_length=250)
    
    brand = models.CharField(max_length=250, default='un-brabded')
    
    description = models.TextField(blank=True)
    
    slug = models.SlugField(max_length=255) # unique products or url
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    image = models.ImageField(upload_to='images/', null=True) 
    
    # define matadata
    class Meta:
        verbose_name_plural ='products'
        
# product (1),product (2) # shirt # shoes

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        
        return reverse("product-info", args=[self.slug])
    


