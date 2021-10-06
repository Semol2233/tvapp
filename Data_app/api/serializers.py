from rest_framework import serializers
from Data_app.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.reverse import reverse as api_img
from rest_framework.pagination import PageNumberPagination


class cat_name(serializers.ModelSerializer):
    class Meta:
        model = Channel_catgory
        fields = [
            'cat_name',
            'cat_slug'
        ]


class channelpost(serializers.HyperlinkedModelSerializer):
     catgory       = cat_name(read_only=True,many=True, required=False)
    
     class Meta:
        model = Add_Channel
        fields = [
            'id',
            'channel_name',
            'catgory',
            'straming_url',
            'channel_logo',
            'release_date'
          
        ]
  

class fetapi(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Add_Channel
        fields = [
          'channel_name',
          'straming_url',
          'channel_logo'
        ]

class fetapitwo(serializers.HyperlinkedModelSerializer):
     Featrued_Channel   = fetapi(read_only=True,many=True, required=False)
     class Meta:
        model = Featrued_Channel
        fields = [
            'Featrued_Channel',
          
        ]





#homepage
class Catgory_find_data(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Add_Channel
        fields = [
            'id',
            'channel_name',
            'channel_logo',
            'straming_url',
            
        ]




class details_page_seri(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Add_Channel
        fields = [
            'id',
            'channel_name',
            'straming_url',
            'channel_logo'
            
        ]
        lookup_field = 'id'




class player_page_list(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Add_Channel
        fields = [
            'id',
            'channel_name',
            'straming_url',
            'channel_logo',
           
          
        ]
  
# class ClassItemSerializer(serializers.HyperlinkedModelSerializer):
    

#       class Meta:
#           model = post_models
#           fields = [
#             'id',
#             'channel_name',
#             'channel_slug',
#             'straming_url',
#             'channel_logo',
#             'release_date'
#           ]


# class catgory_lisst(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = catgory_list
#         fields = [
#             'cat_name',
#             'cat_slug' 
#         ]

# class mixchannel(serializers.HyperlinkedModelSerializer):
#      catgory   = catgory_lisst(read_only=True)
#      class Meta:
#         model = post_models
#         fields = [
#             'catgory',
#             'channel_name',
#             'channel_slug',
#             'straming_url',
#             'channel_logo',
#             'release_date'
          
#         ]




# class coverapiomg(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = coverimgapi
#         fields = [
#             'channel_logo',
            
#         ]




# class nbox_adapi(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = nbox_ad
#         fields = [
#             'status',
#             'ad_img',

            
#         ]

        

        
# class msgseri(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = msgview
#         fields = [
#             'status',
#             'msg'    
#         ]

        

          
# class appsupdateseri(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = appsupdate
#         fields = [
#             'videourl',
#             'msg',
#             'updatelinkbutton' 
#         ]

        
    


# class DRFPostSerializer(serializers.HyperlinkedModelSerializer):
#      catgory   = catgory_lisst(read_only=True)
#      class Meta:
#         model = post_models
#         fields = [
#           'catgory',
#           'channel_name',
#           'channel_slug',
#           'straming_url',
#           'channel_logo'
#         ]




# class fetapi(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = post_models
#         fields = [
#           'channel_name',
#           'channel_slug',
#           'straming_url',
#           'channel_logo'
#         ]






# class fetapitwo(serializers.HyperlinkedModelSerializer):
#      channelfetured   = fetapi(read_only=True,many=True, required=False)
#      class Meta:
#         model = feturedchannel
#         fields = [
#             'channelfetured',
          
#         ]




# class servideo(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = websrisevideo
#         fields = [
#             'id',
#             'series_s_path',
#             'ep_number'
          
#         ]


# class webserisssse(serializers.HyperlinkedModelSerializer):
    
#      class Meta:
#         model = webserise
#         fields = [
#             'id',
#             'serisename',
#             'series_poster',
          
#         ]





# class webseriselist(serializers.HyperlinkedModelSerializer):
#      series_list   = servideo(read_only=True,many=True, required=False)
#      class Meta:
#         model = webserise
#         fields = [
#             'id',
#             'serisename',
#             'series_poster',
#             'series_list'
            
#         ]
#         lookup_field = 'id'




# class movielistseri(serializers.HyperlinkedModelSerializer):
    
#      class Meta:
#         model = movies
#         fields = [
#             'id',
#             'Movie_name',
#             'movie_poster',
          
#         ]



# class mdellist(serializers.HyperlinkedModelSerializer):
#      class Meta:
#         model = movies
#         fields = [
#             'id',
#             'Movie_name',
#             'movie_poster',
#             'movie_storage_path'
            
#         ]
#         lookup_field = 'id'


