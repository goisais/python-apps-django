from django.shortcuts import render
import random


# トップページ
def index(request):
    return render(request, 'work07/index.html')


# おみくじ
def omikuji(request):
    results = ["大吉", "中吉", "小吉", "凶"]
    result = random.choice(results)
    return render(request, "work07/omikuji.html", {"result": result})


# じゃんけん
def janken(request):
    hands = ["グー", "チョキ", "パー"]
    result = None

    if "hand" in request.GET:
        player = request.GET["hand"]
        cpu = random.choice(hands)
        if player == cpu:
            result = "あいこ"
        elif (
            (player == "グー" and cpu == "チョキ")
            or (player == "チョキ" and cpu == "パー")
            or (player == "パー" and cpu == "グー")
        ):
            result = "あなたの勝ち！"
        else:
            result = "あなたの負け…"
        return render(
            request,
            "work07/janken.html",
            {"player": player, "cpu": cpu, "result": result},
        )

    return render(request, "work07/janken.html")


# Hi & Low
def highlow(request):
    num1 = random.randint(1, 13)
    num2 = random.randint(1, 13)
    result = None

    if "choice" in request.GET:
        choice = request.GET["choice"]
        if choice == "high":
            result = "正解！" if num2 > num1 else "ハズレ…"
        elif choice == "low":
            result = "正解！" if num2 < num1 else "ハズレ…"
        return render(
            request,
            "work07/highlow.html",
            {"num1": num1, "num2": num2, "result": result},
        )

    return render(request, "work07/highlow.html", {"num1": num1})
