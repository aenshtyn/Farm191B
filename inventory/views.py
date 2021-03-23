from django.shortcuts import render

# Create your views here.
def home(request):
    cows = Cow.all_cows()
    return render(request,'inventory.html', 'cows',  cows)
