from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406413426',
        'name': 'Raihana Nur Azizah',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
