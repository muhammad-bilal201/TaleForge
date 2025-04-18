from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm, ProfileUpdateForm

# Custom logout view
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully! Please log in.')
        return super().form_valid(form)

class ProfileView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'profile_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['stories'] = user.story_set.all()  # Get all stories by this user
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_edit.html'
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        # Handle avatar deletion if checkbox is checked
        if self.request.POST.get('avatar-clear') == 'on':
            form.instance.avatar.delete(save=False)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
class LogoutView(View):
    def custom_logout(request):
        if request.method == 'POST':
            logout(request)
            messages.success(request, 'You have been logged out successfully.')
            return redirect('login')
        return redirect('home') 