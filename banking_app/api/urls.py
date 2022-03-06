from django.conf.urls import url 

from .views import (
    BranchesAPIView,
    BranchDetailAPIView,
    BanksAPIView,
    BankDetailAPIView

)

urlpatterns = [
    url(r'^branches/', BranchesAPIView.as_view(),name='branches'),
    url(r'^branch/(?P<pk>[0-9]+)/', BranchDetailAPIView.as_view(),name='branch-detail'),
    url(r'^banks', BanksAPIView.as_view(), name='banks'),
    url(r'^bank/(?P<pk>[0-9]+)/', BankDetailAPIView.as_view(), name='bank-detail'),
    
    
]