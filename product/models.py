from django.db import models
from catalog.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model): 
    name = models.CharField(max_length=255, unique=True) 
    slug = models.SlugField(max_length=255, unique=True, 
                            help_text='Unique value for product page URL, created from name.') 
    author = models.CharField(max_length=50) 
    price = models.DecimalField(max_digits=9,decimal_places=0) 
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    is_active = models.BooleanField(default=True) 
    is_bestseller = models.BooleanField(default=False) 
    is_featured = models.BooleanField(default=False) 
    quantity = models.IntegerField() 
    description = models.TextField() 
    meta_keywords = models.CharField(max_length=255, 
                                     help_text='Comma-delimited set of SEO keywords for meta tag') 
    meta_description = models.CharField(max_length=255, 
                                        help_text='Content for description meta tag') 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    categories = models.ManyToManyField(Category) 
    
    class Meta: 
        db_table = 'products' 
        ordering = ['-created_at'] 

    def __str__(self): 
        return self.name 
    
    def get_absolute_url(self): 
        return reverse('catalog_product', args=((), { 'product_slug': self.slug })) 
    
    # def sale_price(self): 
    #     if self.old_price > self.price: 
    #         return self.price 
    #     else: 
    #         return None