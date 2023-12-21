from django.shortcuts import render
from .models import RowMachine

# Create your views here.
def index(request):
    row_machines = RowMachine.objects.all()
    return render(request, 'rowtrack/index.html', {'row_machines': row_machines})

def rowMachine(request, slug):
    row_machine = RowMachine.objects.get(slug=slug)
    return render(request, 'rowtrack/machine.html', {'row_machine': row_machine})