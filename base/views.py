from django.shortcuts import render

# Create your views here.

def homepage(request):
    
    context = {}
    
    context['title'] = 'Florentino'
    context['description'] = 'Founded in 2007, Florentino Printing has and always been trusted by many for our quality service.'
    context['keywords'] = 'florentino printing, printing, masbate city, printing sevices'
    
    return render(request, 'homepage/index.html', context=context)