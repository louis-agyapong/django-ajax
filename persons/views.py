from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .forms import PersonCreationForm
from .models import City, Person


def person_create_view(request):
    """
    Person create view
    """
    form = PersonCreationForm()
    if request.method == "POST":
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("person_add")
    return render(request, "persons/home.html", {"form": form})

def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})


def load_cities(request):
    """
    Load cities
    """
    country_id = request.GET.get("country_id")
    cities = City.objects.filter(country_id=country_id)
    # return render(request, "persons/city_list.html", {"cities": cities})
    print(list(cities.values('id', 'name')))
    return JsonResponse(list(cities.values('id', 'name')), safe=False)
