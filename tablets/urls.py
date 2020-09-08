from django.urls import path
from .views import tablets_list, TabletsDelete, BrandCreate, TabletUpdate, TabletCreate, TabletDetail

urlpatterns = [
    path('tablets/', tablets_list, name='tablets'),
    path('tablets/newbrand', BrandCreate.as_view(), name='new'),
    path('tablets/newtablet', TabletCreate.as_view(), name='newTablet'),
    path('tablets/update/<int:pk>', TabletUpdate.as_view(), name='updateTablet'),
    path('tablets/<int:pk>', TabletDetail.as_view(), name='detailTablet'),
    path('tablets/delete/<int:id>/', TabletsDelete.as_view(), name='delete'),
]

