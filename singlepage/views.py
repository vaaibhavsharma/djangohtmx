from django.shortcuts import render
import time
# Create your views here.
def home(request):
    # Some processing 
    time.sleep(0.5)
    # Processing End
    if request.htmx:
        return render(request, 'singlepage/components/dashboard.html')
    else:
        return render(request, 'singlepage/components/dashboard_full.html')

def forms(request):
    # Some processing 
    time.sleep(0.5)
    # Processing End
    if request.htmx:
        return render(request, 'singlepage/components/forms.html')
    else:
        return render(request, 'singlepage/components/forms_full.html')