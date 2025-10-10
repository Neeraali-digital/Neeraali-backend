from rest_framework import viewsets
from .models import Enquiry
from .serializers import EnquirySerializer

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all().order_by('-created_at')
    serializer_class = EnquirySerializer
