import json
from django.shortcuts import render
from .forms import PersonForm
from django.http import JsonResponse
import json
from .models import City
# Create your views here.

def person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "person.html", {"form": form})

def cities(request):
    data = json.loads(request.body)
    cities = City.objects.filter(country__id=data['user_id'])
    print(cities)
    return JsonResponse(list(cities.values("id", "name")), safe=False)
