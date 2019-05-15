from django.db import models
from django.urls import reverse# to get the urls

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    # slug field to store the url path requested
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    # order by name and add verbose_name and plural(labels)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

  #to return a representation of the model
    def __str__(self):
        return '{}'.format(self.name)

     #   get url function for categories(pass the slug field)
    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    # add foreign key to category on delete cascade
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)#add time stamp
    updated = models.DateTimeField(auto_now=True)#update time stamp
    price=models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

        # to return a representation of the model
    def __str__(self):
        return '{}'.format(self.name)
    # to get product urls(pass the slug field)
    def get_url(self):
        return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])
