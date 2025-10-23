from django import forms


class ReiwaForm(forms.Form):
    reiwa_year = forms.IntegerField(
        label="令和何年ですか？",
        min_value=1,
        widget=forms.NumberInput(attrs={"placeholder": "例: 5"}),  # プレースホルダーを追加
    )
    