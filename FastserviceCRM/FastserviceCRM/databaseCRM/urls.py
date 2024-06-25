from django.urls import path, include

from . import views
from .serializes import StatusOrderSerializer
from .views import user_login, index, user_logout, workShop, OrderThis, printReportOrder, StatusOrderGet

urlpatterns = [
    path('login/', user_login, name='login'),
    path('', index, name='index'),
    path('logout/', user_logout, name='logout'),
    path('workshop/', workShop, name='workShop'),
    path('order/<int:OrderID>', OrderThis, name='order'),
    path('order/report/<int:OrderID>', printReportOrder, name='printReport'),
    path('api/get/statusOrder/', StatusOrderGet.as_view(), name='StatusOrderGet')
]