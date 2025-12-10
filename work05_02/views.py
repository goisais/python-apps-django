from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.http import HttpResponse
from django.conf import settings
import os


def index(request):
    context = {
        "name": "hukumoto ryosuke"
    }
    try:
        return render(request, "index.html", context)
    except TemplateDoesNotExist:
        # テンプレートが見つからない場合にプロジェクト内の候補パスを探す（デバッグ用フォールバック）
        base = str(getattr(settings, "BASE_DIR", ""))
        candidates = [
            os.path.join(base, "work05_02", "templates", "index.html"),
            os.path.join(
                base, "work05_02", "templates", "work05_02", "index.html"
                ),
            os.path.join(base, "templates", "index.html"),
            os.path.join(base, "templates", "work05_02", "index.html"),
        ]
        for p in candidates:
            try:
                with open(p, encoding="utf-8") as f:
                    return HttpResponse(f.read())
            except FileNotFoundError:
                continue
        return HttpResponse(
            "index.html が見つかりません。"
            "templates フォルダの配置（app/templates/ または project/templates/）と "
            "settings.TEMPLATES の 'DIRS' / INSTALLED_APPS を確認してください。",
            status=404
        )
