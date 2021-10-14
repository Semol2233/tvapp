from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Data_app import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('df', Featured_Channel_view.as_view()),
    path('featrue_channel/', Homepage_cat.as_view()),
    path('channel/<category>/', playerpagecatgory.as_view()),
    path('play/<id>', dtlspage.as_view()),
    path('play_page_list/', player_page_listc.as_view()),
    path('play_page_channel_filter/<category>', play_page_channel_list.as_view()),
    path('search/<query>', seeearcsssh_filter.as_view()),
    path('catlist', cat_listsa.as_view()),






    # path('d/<channel_slug>', ServiceDetailAPIView.as_view()),
    # path('mix', mixchannel.as_view()),
    # path('add', postchannel.as_view(),name='fhdf'), 
    # path('cover', coverapi.as_view(),name='ee'),
    # path('ad', nbox_adview.as_view(),name='ad'),
    # path('msg', msgviewmodel.as_view(),name='awd'),
    # path('up', appsupdatmodel.as_view(),name='update'),

    # path('home', playerpagedata.as_view(),name='ch'),
    # path('dtls', homepagedata.as_view(),name='ch'),
    # path('fet', feturedapi.as_view(),name='fet'),
    # path('slist',serisevideo.as_view()),
    # path('sdel/<id>',websrise.as_view()),
    # path('mlist',movielist.as_view()),
    # path('mdel/<id>',moviedel.as_view()),
  
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#mix url - its player niche prthom akta mix channel hbe 
#d/ player page dtls pagfe
#cat catagory ghulo get kora

