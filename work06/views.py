from django.shortcuts import render
from .forms import ReiwaForm


def reiwa_to_seireki(request):
    seireki = None  # 結果用の変数を初期化
    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["reiwa_year"]
            seireki = reiwa_year + 2018
    else:
        form = ReiwaForm()
    return render(
        request, "work_06/index.html", {"form": form, "seireki": seireki}
        )
