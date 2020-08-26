from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


Gender = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)


Favorite_chose = (
    ('Fun','Fun'),
    ('Food','Food'),
    ('Travel','Travel'),
    ('Music','Music'),
    ('Swimming','Swimming'),
    ('Wrestling','Wrestling'),
    ('Tv','Tv'),
    ('Books','Books'),
    ('Football','Football'),
    ('Challenge','Challenge'),
)




class category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name
    

    def get_absolute_url (self):
        return reverse('home')  



class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True,null=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255,null=True, blank=True,)
    facebook_url = models.CharField(max_length=255,null=True, blank=True,)
    twtter_url = models.CharField(max_length=255,null=True, blank=True,)
    instgram_url = models.CharField(max_length=255,null=True, blank=True,)
    phone = models.CharField(blank=True, max_length=15,verbose_name="Phone Number")
    address = models.CharField(max_length=100)
    country = CountryField()
    Gender = models.CharField(max_length=20,choices=Gender) 
    Profile_Cover = models.ImageField(blank=True,null=True, upload_to="images/profile/Profile-Cover")
    Favorite = models.CharField(max_length=20,choices=Favorite_chose)

    def __str__(self):
        return str(self.user)
    def get_absolute_url (self):
        return reverse('home') 



    

    def __str__(self):
        return str(self.user)
         

class Post (models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    auther = models.ForeignKey(User , on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)

    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    like = models.ManyToManyField(User,related_name='bloge_Post')
    
    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title + ' | ' + str(self.auther)
    

    def get_absolute_url (self):
        return reverse('home')  

    

class Comment(models.Model):
    post =  models.ForeignKey(Post,related_name="comments" , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return '%s - %s' % (self.post.title, self.name)
