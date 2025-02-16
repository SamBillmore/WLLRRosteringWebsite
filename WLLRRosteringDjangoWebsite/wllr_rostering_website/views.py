from django.shortcuts import render


def main(request):
    return render(request, "wllr_rostering_website/main.html")
