from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import F
from stories.models import Story
from .models import Chapter, Vote
from .forms import ChapterForm

class ChapterCreateView(LoginRequiredMixin, CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'chapters/chapter_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        self.story = get_object_or_404(Story, pk=kwargs['story_pk'])
        if 'parent_pk' in kwargs:
            self.parent = get_object_or_404(Chapter, pk=kwargs['parent_pk'])
        else:
            self.parent = None
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = self.story
        context['parent'] = self.parent
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.story = self.story
        if self.parent:
            form.instance.parent = self.parent
        messages.success(self.request, 'Chapter submitted for approval!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('story_detail', kwargs={'pk': self.story.pk})

class ChapterDetailView(DetailView):
    model = Chapter
    template_name = 'chapters/chapter_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chapter = self.get_object()
        context['branches'] = chapter.get_children().filter(status='APP')
        context['has_voted'] = False
        if self.request.user.is_authenticated:
            context['has_voted'] = Vote.objects.filter(
                user=self.request.user, 
                chapter=chapter
            ).exists()
        return context

def vote_chapter(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    
    chapter = get_object_or_404(Chapter, pk=pk)
    vote_type = request.POST.get('vote_type') == 'up'
    
    # Check if user already voted
    existing_vote = Vote.objects.filter(user=request.user, chapter=chapter).first()
    
    if existing_vote:
        if existing_vote.vote_type != vote_type:
            # Change vote
            chapter.votes += 2 if vote_type else -2
            existing_vote.vote_type = vote_type
            existing_vote.save()
            messages.success(request, 'Your vote has been updated!')
        else:
            # Remove vote
            chapter.votes -= 1 if vote_type else -1
            existing_vote.delete()
            messages.success(request, 'Your vote has been removed!')
    else:
        # New vote
        Vote.objects.create(user=request.user, chapter=chapter, vote_type=vote_type)
        chapter.votes += 1 if vote_type else -1
        messages.success(request, 'Your vote has been recorded!')
    
    chapter.save()
    return redirect('chapter_detail', pk=chapter.pk)