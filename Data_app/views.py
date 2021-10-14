from django.shortcuts import render
#rest_framwork
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins,filters
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from django.http import HttpResponse
#end
from rest_framework.decorators import api_view
from django.db.models import Q
import random
import datetime
#user model
import jwt
from Data_app.models import *
#end
from datetime import datetime, timedelta
#serializer 
from Data_app.api.serializers import *
#end
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .pagination import PaginationHandlerMixin
#setting option
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#end
from django.contrib.auth.mixins import LoginRequiredMixin

# DJango built in login 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout
# end
from rest_framework.settings import api_settings
#social Auth 

#user filter
from django.contrib.auth import get_user_model
User = get_user_model()
#end
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView


from django import forms
#list view -> APi
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .forms import *















# def generate_jwt():
#     encoded_jwt = jwt.encode({'key': 'custom_value'}, 'secret', algorithm='HS256').decode('utf-8')
#     token = 'Bearer ' + encoded_jwt
#     return token

# jwt_token = generate_jwt()

    
# class Tag_ddviewr(pagination.PageNumberPagination):
#     page_size = 6
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# #mixpage_cahnnel player niche
# class mixchannel(generics.ListAPIView):
#     queryset               = post_models.objects.all().order_by('?')[:6]
#     serializer_class       = mixchannel
    


# #dtls page
# class ServiceDetailAPIView(generics.RetrieveAPIView):
#     queryset = post_models.objects.all()
#     serializer_class = ClassItemSerializer
#     lookup_field = ('channel_slug')



# #homepageapi
# class channelpost(APIView, PaginationHandlerMixin):
#     pagination_class = Tag_ddviewr

#     def get(self, request, category, *args, **kwargs):
#         authors = catgory_list.objects.filter(cat_slug=category).values('cat_name','cat_slug')
#         if authors:
#             posts = post_models.objects.filter(catgory__cat_slug=category).values('id','channel_name','channel_slug','straming_url','channel_logo','release_date').order_by('-id')

#             for author in list(authors):
#                 response = {
#                 'cat_name': author['cat_name']

#                 }
#             page = self.paginate_queryset(list(posts))
#             response['List'] = page
#             paginated_response = self.get_paginated_response(response)
#             return JsonResponse(paginated_response.data, safe=False)
#         return HttpResponse('No matching data found', status=404)



    
# class Tag_dsdviewr(pagination.PageNumberPagination):
#     page_size = 8
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# #payerpage
# class playerpagecatgory(APIView, PaginationHandlerMixin):
#     pagination_class = Tag_dsdviewr

#     def get(self, request, category, *args, **kwargs):
#         authors = catgory_list.objects.filter(cat_slug=category).values('cat_name','cat_slug')
#         if authors:
#             posts = post_models.objects.filter(catgory__cat_slug=category).values('id','channel_name','channel_slug','straming_url','channel_logo','release_date').order_by('-id')

#             for author in list(authors):
#                 response = {
#                 'cat_name': author['cat_name']

#                 }
#             page = self.paginate_queryset(list(posts))
#             response['List'] = page
#             paginated_response = self.get_paginated_response(response)
#             return JsonResponse(paginated_response.data, safe=False)
#         return HttpResponse('No matching data found', status=404)






# class postchannel(CreateView,LoginRequiredMixin):
#     form_class = daildddyscosst
#     model = post_models
#     template_name = 'uplode_us.html'




# class coverapi(generics.ListAPIView):
#     queryset               = coverimgapi.objects.all().order_by('-id')[:2]
#     serializer_class       = coverapiomg
    


# class nbox_adview(generics.ListAPIView):
#     queryset               = nbox_ad.objects.all()[:1]
#     serializer_class       = nbox_adapi
    





# class msgviewmodel(generics.ListAPIView):
#     queryset               = msgview.objects.all()[:1]
#     serializer_class       = msgseri
   


# class msgviewmodel(generics.ListAPIView):
#     queryset               = msgview.objects.all()[:1]
#     serializer_class       = msgseri
   



# class appsupdatmodel(generics.ListAPIView):
#     queryset               = appsupdate.objects.all()[:1]
#     serializer_class       = appsupdateseri
  
   


# class channel_Data(pagination.PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# class playerpagedata(generics.ListAPIView):
#     queryset = post_models.objects.all().order_by('?')
#     serializer_class       = DRFPostSerializer
#     filter_backends        = [filters.SearchFilter]
#     search_fields          = ['catgory__cat_slug']
#     pagination_class       = channel_Data


# class channels_Data(pagination.PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# class homepagedata(generics.ListAPIView):
#     queryset = post_models.objects.all().order_by('?')
#     serializer_class       = DRFPostSerializer
#     filter_backends        = [filters.SearchFilter]
#     search_fields          = ['catgory__cat_slug']
#     pagination_class       = channels_Data


# class feturedapi(generics.ListAPIView):
#     queryset = feturedchannel.objects.all()
#     serializer_class       = fetapitwo




# class serisevideo(generics.ListAPIView):
#     queryset = webserise.objects.all()
#     serializer_class       = webserisssse




# class websrise(generics.RetrieveAPIView):
#     queryset = webserise.objects.all()
#     serializer_class       = webseriselist
#     lookup_field           = ('id')





# class movielist(generics.ListAPIView):
#     queryset = movies.objects.all()
#     serializer_class       = movielistseri




# class moviedel(generics.RetrieveAPIView):
#     queryset = movies.objects.all()
#     serializer_class       = mdellist
#     lookup_field           = ('id')



# class movielist(generics.ListAPIView):
#     queryset = movies.objects.all()
#     serializer_class       = movielistseri




# class moviedel(generics.RetrieveAPIView):
#     queryset = movies.objects.all()
#     serializer_class       = mdellist
#     lookup_field           = ('id')




class Featured_Channel_view(generics.ListAPIView):
    queryset = Featrued_Channel.objects.all()
    serializer_class       = fetapitwo




class Homepage_cat(generics.ListAPIView):
    queryset = Add_Channel.objects.all()
    serializer_class       = Catgory_find_data
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['catgory__cat_slug']



class Tag_dsdviewr(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

#payerpage
class playerpagecatgory(APIView, PaginationHandlerMixin):
    pagination_class = Tag_dsdviewr

    def get(self, request, category, *args, **kwargs):
        authors = Channel_catgory.objects.filter(cat_slug=category).values('cat_name','cat_slug')
        if authors:
            posts = Add_Channel.objects.filter(catgory__cat_slug=category).values('id','channel_name','straming_url','channel_logo').order_by('-id')

            for author in list(authors):
                response = {
                'cat_name': author['cat_name']

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)



class dtlspage(generics.RetrieveAPIView):
    queryset = Add_Channel.objects.all()
    serializer_class       = details_page_seri
    lookup_field           = ('id')


class player_page_listc(generics.ListAPIView):
    queryset = Add_Channel.objects.all()
    serializer_class       = player_page_list




class Tag_dsdsviewr(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100


class play_page_channel_list(APIView, PaginationHandlerMixin):
    pagination_class = Tag_dsdsviewr

    def get(self, request, category, *args, **kwargs):
        authors = Channel_catgory.objects.filter(cat_slug=category).values('cat_name','cat_slug')
        if authors:
            posts = Add_Channel.objects.filter(catgory__cat_slug=category).values('id','channel_name','straming_url','channel_logo').order_by('-id')

            for author in list(authors):
                response = {
                'cat_name': author['cat_name']

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)













class qa_pagenation(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class seeearcsssh_filter(APIView, PaginationHandlerMixin): 
    pagination_class = qa_pagenation

    def get(self,request,query):
        result = []
        filter_postmodel_q = Add_Channel.objects.filter(Q(channel_name__exact=query) | Q(id__contains=query) | Q(catgory__cat_name__iexact=query)).values('id','channel_name','catgory','channel_logo')
        if filter_postmodel_q:
            for p in filter_postmodel_q:
                result.append(p)

        page = self.paginate_queryset(result)
        paginated_response = self.get_paginated_response(page)
        if len(result) == 0:
            return HttpResponse('No matching data found', status=404)
        return JsonResponse(paginated_response.data, safe=False)


