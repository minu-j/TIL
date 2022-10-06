from django.shortcuts import redirect, render
from .models import Vote
from .forms import VoteForm

# Create your views here.
def index(request):
    votes = Vote.objects.all()
    context = {
        'votes': votes,
    }
    return render(request, 'votes/index.html', context)


def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('votes:index')
        
    form = VoteForm()
    context = {
        'form': form,
    }
    return render(request, 'votes/create.html', context)