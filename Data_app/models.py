from typing import ClassVar
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
# from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.urls import reverse



class Channel_catgory(models.Model):
    cat_name           = models.CharField(max_length=255)
    release_date       = models.DateField(auto_now_add = True)
    cat_slug           =   models.SlugField(max_length=200)

    def __str__(self):
        return self.cat_name   


class Add_Channel(models.Model):
    channel_name   = models.CharField(max_length=255)
    catgory        = models.ForeignKey(Channel_catgory,blank=True,on_delete=CASCADE)
    release_date   = models.DateField(auto_now_add = True)
    straming_url =  models.URLField(default='www.test.com')
    channel_logo   = models.FileField(upload_to="channel_logo" ,blank=True)

    def __str__(self):
        return self.channel_name    




class Featrued_Channel(models.Model):
    Date =  models.DateField(auto_now_add = True)
    Featrued_Channel = models.ManyToManyField('Add_Channel')



# class coverimgapi(models.Model):
#     release_date   = models.DateField(auto_now_add = True)
#     channel_logo   = models.FileField(upload_to="coverimg" ,blank=True)




# class nbox_ad(models.Model):
#     release_date   = models.DateField(auto_now_add = True)
#     status = models.BooleanField(default=False)
#     ad_img   = models.FileField(upload_to="coverimg" ,blank=True)


# class msgview(models.Model):
#     release_date   = models.DateField(auto_now_add = True)
#     status = models.BooleanField(default=False)
#     msg = models.TextField(blank=True)
   

#     def __str__(self):
#         return self.msg    


# class appsupdate(models.Model):
#   videourl =   models.URLField(max_length=300)
#   msg = models.TextField(blank=True)
#   updatelinkbutton = models.URLField(max_length=300)






#vod_partNBOX


# class serise_cat(models.Model):
#      Date                 =  models.DateField(auto_now_add = True)
#      scat_name = models.CharField(max_length=255)
     
#      def __str__(self):
#         return self.scat_name

# class websrisevideo(models.Model):
#    Date                =  models.DateField(auto_now_add = True)
#    ep_number          =  models.CharField(max_length=255)
#    series_s_path       =  models.URLField(default='www.test.com')
#    series_slug        =  models.SlugField(max_length=200)
   


#    def __str__(self):
#        return '{} {} '.format(self.ep_number, self.series_slug)

# class webserise(models.Model):
#     Date                 =  models.DateField(auto_now_add = True)
#     serisename          =  models.CharField(max_length=255)
#     series_poster        =  models.FileField(upload_to="seriseimg" ,blank=True)
#     series_list    =      models.ManyToManyField(websrisevideo)
#     serise_cat        = models.ForeignKey(serise_cat,blank=True,on_delete=CASCADE)
#     serise_pubdate        =  models.DateField(auto_now_add = True)
#     def __str__(self):
#         return self.serisename



# class moviecatgory(models.Model):
#      Date                 =  models.DateField(auto_now_add = True)
#      cat_name = models.CharField(max_length=255)
     
#      def __str__(self):
#         return self.cat_name



# class movies(models.Model):
#     Date                 =  models.DateField(auto_now_add = True)
#     movie_pubdate        =  models.DateField()
#     Movie_name           =  models.CharField(max_length=255)
#     movie_catgory        = models.ForeignKey(moviecatgory,blank=True,on_delete=CASCADE)
#     movie_poster         =  models.FileField(upload_to="movieposter" ,blank=True)
#     movie_storage_path   =  models.URLField(default='www.test.com')
   
#     def __str__(self):
#         return self.Movie_name

# class blog_cat(models.Model):
#      Date                 =  models.DateField(auto_now_add = True)
#      cat_name = models.CharField(max_length=255)
     
#      def __str__(self):
#         return self.cat_name


# class blog(models.Model):
#     date =  models.DateField(auto_now_add = True)
#     blog_title = models.CharField(max_length=255)
#     blog_slug = models.SlugField(max_length=200)
#     blog_img =  models.FileField(upload_to="blog_img" ,blank=True)
#     blog_description = models.TextField(blank=True)
#     blog_cat        = models.ForeignKey(blog_cat,blank=True,on_delete=CASCADE)

#     def __str__(self):
#         return self.blog_title



# class trvideo_catg(models.Model):
#      Date                 =  models.DateField(auto_now_add = True)
#      cat_name = models.CharField(max_length=255)
     
#      def __str__(self):
#         return self.cat_name

# class trobleshortvideo(models.Model):
#     date =  models.DateField(auto_now_add = True)
#     video_title = models.CharField(max_length=255)
#     video_img = models.FileField(upload_to="tr_video" ,blank=True)
#     tr_videocat =models.ForeignKey(trvideo_catg,blank=True,on_delete=CASCADE)
#     tr_video_path = models.URLField(default='www.test.com')

#     def __str__(self):
#         return self.video_title
