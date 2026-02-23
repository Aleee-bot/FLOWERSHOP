from django.shortcuts import render
from django.views import View
from .models import Flower
# Create your views here.

class Home(View):
    def get(self, request):
        flowers = Flower.objects.all()
        return render(request, 'home.html', {'flowers': flowers})

