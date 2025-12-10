from django.shortcuts import render, redirect
from .models import MoodRecord
from django.db.models import Sum
from django.views.decorators.http import require_POST


# index view consolidated later; single 'index' defined below.


def select_mood(request):
    if request.method == "POST":
        mood = request.POST["mood"]
        mood_amount = {"happy": 300, "neutral": 200, "sad": 100}
        amount = mood_amount.get(mood, 0)
        MoodRecord.objects.create(mood=mood, amount=amount)
        return redirect("result", mood=mood, amount=amount)
    return render(request, "bankapp/select.html")


def result(request, mood, amount):
    return render(
        request, "bankapp/result.html", {"mood": mood, "amount": amount}
        )


def history(request):
    records = MoodRecord.objects.all().order_by("-created_at")
    total = MoodRecord.objects.aggregate(Sum("amount"))["amount__sum"] or 0
    return render(
        request, "bankapp/history.html", {"records": records, "total": total}
        )


@require_POST
def reset_history(request):
    """履歴をすべて削除して履歴ページへリダイレクトする。POSTのみ許可。"""
    # 全件削除
    MoodRecord.objects.all().delete()
    return redirect("history")


def index(request):
    if request.method == "POST":
        mood = request.POST.get("mood")
        if mood:
            mood_amount = {"happy": 300, "neutral": 200, "sad": 100}
            amount = mood_amount.get(mood, 0)

            MoodRecord.objects.create(mood=mood, amount=amount)

            return redirect("result", mood=mood, amount=amount)

    return render(request, "bankapp/index.html")


def top(request):
    return render(request, "top.html")