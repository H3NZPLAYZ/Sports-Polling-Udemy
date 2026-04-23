from django.shortcuts import render
from sports.models import Fixture

# Create your views here.
def fixtures(request):
    fixtures = Fixture.objects.all()
    context = {
        'fixtures': fixtures,
    }

    if request.htmx:
        return render(request, 'sports/fixtures.html#fixture-block', context)

    return render(request, 'sports/fixtures.html', context)