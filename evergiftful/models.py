from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from autoslug import AutoSlugField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from django.utils import timezone














class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.product.title








""" Categories model settings """
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='media/', blank=True)
    image_alt = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='product_types')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True, related_name='product_types')
    
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
""" End if category model settings """






class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', related_name='wishlists')

    def __str__(self):
        product_names = ", ".join(str(product) for product in self.products.all())
        return f"{self.user.username}'s Wishlist: {product_names}"





class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200, blank=True)
    discount = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='media/')
    image_alt = models.CharField(max_length=200)
    description = RichTextField()
    url = models.URLField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    related_products = models.ManyToManyField('self', blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True,)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, blank=True)
    wishlist = models.ManyToManyField(Wishlist, blank=True)



    
    class Meta:
        ordering = ['-date_created']


    




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("evergiftful:product_detail", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)





class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_post_images/')
    image_alt = models.CharField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    date_created = models.DateTimeField(default=timezone.now)
    related_articles = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.title
    

    
    def get_absolute_url(self):
        return reverse("evergiftful:blog_detail", kwargs={'slug': self.slug})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)





class Contact(models.Model):
    name = models.CharField(max_length=100)
    email =  models.CharField(max_length=200)
    subject =  models.CharField(max_length=200)
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name