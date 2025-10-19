from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnquiryViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'enquiries', EnquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
