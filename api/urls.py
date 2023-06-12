from django.urls.conf import path
from .views import UserView,StoreVeiw,SalesVeiw,ReceiptsVeiw
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('user/',UserView.as_view(),name='user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('store/',StoreVeiw.as_view(),name='store'),
    path('sales/',SalesVeiw.as_view(),name='sales'),
    path('receipts/',ReceiptsVeiw.as_view(),name='receipts')
]
