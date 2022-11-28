from django.views.generic import TemplateView, DetailView, FormView
from .models import JobList, JobApplication
from .forms import ApplyForm 
from django.contrib import messages


class HomePageView(TemplateView):
    model = JobList
    template_name = 'joblist.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = JobList.objects.all().order_by('-id')
        return context
    
class DetailPageView(DetailView):
    template_name = 'jobdetail.html'
    model = JobList
    
    
class FormPageView(FormView):
    form_class = ApplyForm
    model = JobApplication
    template_name = 'jobform.html'  
    
    success_url = '/'
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Create a new Post
        new_object = JobApplication.objects.create(
            Job_Title = form.cleaned_data['Job_Title'],
            JobType = form.cleaned_data['JobType'],
            Full_Name = form.cleaned_data['Full_Name'],
            PhoneNumber = form.cleaned_data['PhoneNumber'],
            Brief_introduction_about_yourself = form.cleaned_data['Brief_introduction_about_yourself'],
            Resume = form.cleaned_data['Resume'],
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your application was successful')
        return super().form_valid(form)
    