
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from base.models import Users,ScoreCards
from django.urls import reverse_lazy

from django.shortcuts import redirect




from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



# Create your views here.

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('scorecards')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('scorecards')
        return super(RegisterPage,self).get(*args,**kwargs)

class ScoreCardList(ListView):
    model = ScoreCards
    context_object_name = 'scorecards'
class ScoreCardViews(DetailView):
    model = ScoreCards
    context_object_name = 'scorecards'
    template_name = "base/score_card.html"

    def get_queryset(self):
        return ScoreCards.objects.all().order_by("-id")