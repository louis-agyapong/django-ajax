from django.shortcuts import render
from .forms import InfoModelForm
from .models import Info


def info_add_view(request):
    """
    Info add view
    """
    form = InfoModelForm(request.POST or None)
    data = {}

    if request.method == "POST":
        print("works")

    context = {
        "form": form,
    }
    return render(request, "infos/main.html", context)
