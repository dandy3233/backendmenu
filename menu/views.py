from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from .models import Burger
from .serializers import BurgerSerializer

class BurgerListView(APIView):
    def get(self, request):
        # Fetch all burgers from the database
        burgers = Burger.objects.all()

        # Serialize the burger data
        serializer = BurgerSerializer(burgers, many=True)

        # Modify the image field to include the full URL (absolute URL)
        for staff_member in serializer.data:
            # Ensure the image URL is complete (i.e., absolute URL)
            if staff_member['image']:
                staff_member['image'] = request.build_absolute_uri(staff_member['image'])

        # Return the modified response
        return Response(serializer.data)
