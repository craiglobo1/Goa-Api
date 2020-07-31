from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('owner', OwnerView)
router.register('buisness', BuisnessView)
router.register('taxes', TaxesView)
router.register('application', ApplicationView)
# router.register('getAll', getAllList)

urlpatterns = [
    path('', include(router.urls), name="api-overview"),
    path('all/<str:id>', AllList.as_view()),
]
