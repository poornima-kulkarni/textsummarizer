from django.shortcuts import render
from .utils import extractive_summary

def index(request):
    summary_list = []
    if request.method == "POST":
        input_text = request.POST.get("input_text")
        if input_text:
            summary_list = extractive_summary(input_text, num_sentences=3)
    return render(request, "index.html", {"summary_list": summary_list})
