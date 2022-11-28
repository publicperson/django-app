from django.views.generic import TemplateView, DetailView, ListView
from .models import Personnel
from django.db.models import Q


class HomPageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personnel'] = Personnel.objects.all().order_by('-id')
        return context
    
class DetailPageView(DetailView):
    template_name = 'detail.html'
    model = Personnel
    
class SearchResultsView(ListView):
    model = Personnel
    template_name = 'search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Personnel.objects.filter(Q(FirstName__contains=query) | Q(LastName__contains=query) | Q(Status__contains=query))
        return object_list
        