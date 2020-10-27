from django.shortcuts import render
from django.http import JsonResponse

from .forms import InfoModelForm
from .models import Info


def info_add_view(request):
    """
    Info add view
    """
    form = InfoModelForm(request.POST or None)
    data = {}

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            agree = form.cleaned_data["agree"]

            data['name'] = name
            data['email'] = email
            data['message'] = message
            data['agree'] = agree

            form.save()

            return JsonResponse(data, safe=False)

    context = {
        "form": form,
    }
    return render(request, "infos/main.html", context)
