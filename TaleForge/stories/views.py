from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Story
from .forms import StoryForm

class StoryListView(ListView):
    model = Story
    template_name = 'stories/home.html'
    context_object_name = 'stories'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(genre=genre)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Story.GENRE_CHOICES
        return context

class StoryDetailView(DetailView):
    model = Story
    template_name = 'stories/story_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = self.get_object()
        context['chapters'] = story.chapter_set.filter(status='APP').order_by('created_at')
        return context

class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    form_class = StoryForm
    template_name = 'stories/story_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Story created successfully!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('story_detail', kwargs={'pk': self.object.pk})

class StoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Story
    form_class = StoryForm
    template_name = 'stories/story_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user and not self.request.user.is_moderator:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Story updated successfully!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('story_detail', kwargs={'pk': self.object.pk})