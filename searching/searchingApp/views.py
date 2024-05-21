from django.shortcuts import render
from .models import Goal
from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Goal.objects.filter(
            Q(title__icontains=query) | Q(sub__icontains=query)
        )[:5]  # Limit results to 5
    return render(request, 'searchingApp/base.html', {'query': query, 'results': results})


def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'searchingApp/goal.html', {'goals': goals})