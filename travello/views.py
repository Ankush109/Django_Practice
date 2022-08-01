from django.shortcuts import render
from .models import dest
# Create your views here.
def index (request):
    #passing the objects to the template
    dest1=dest()
    dest1.name="ankush"
    dest1.desc="this is ankush"
    return render(request,"index.html",{'dest1':dest1})
    
    