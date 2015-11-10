from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Game
from .models import Move
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import GameForm
from .forms import MoveForm
from .forms import PostForm
from .forms import SearchProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home_page(request):
    if request.user.is_authenticated():
        return redirect('chesswave.views.dashboard')
    return render(request, 'chesswave/home_page.html', {})


def docs(request):
    return render(request, 'chesswave/docs.html', {})    
    
    
def contacts(request):
    return render(request, 'chesswave/contacts.html', {})
    
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('chesswave.views.dashboard')        
    else:
        form = UserCreationForm 
    return render(request, 'registration/register.html',  {'form': form})    
        

@login_required    
def dashboard(request):
    return render(request, 'chesswave/dashboard.html', {})
    

def profile(request, player):
    games = Game.objects.filter(white=player) | Game.objects.filter(black=player)
    games.order_by('created_date') 
    return render(request, 'chesswave/profile.html', {'games': games, 'player': player})


@login_required    
def game_list(request):
    games = Game.objects.filter().order_by('created_date')
    return render(request, 'chesswave/game_list.html', {'games': games})
    

@login_required    
def game_list_user(request, player):
    # games = Game.objects.filter(white=player).order_by('created_date')
    games = Game.objects.filter(white=player) | Game.objects.filter(black=player)
    games.order_by('created_date') 
    return render(request, 'chesswave/game_list_user.html', {'games': games, 'player': player})
    

@login_required            
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    moves = Move.objects.filter(game=game).order_by('created_date')
    return render(request, 'chesswave/game_detail.html', {'game': game, 'moves': moves})       


@login_required
def game_new(request, white, black):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated():
                post.author = request.user
                post.white = white
                post.black = black             
            post.save()
            return redirect('chesswave.views.game_detail', pk=post.pk)
    else:
        form = GameForm()
        form.white = white        
        form.black = black              
    return render(request, 'chesswave/game_new.html', {'form': form, 'white': white, 'black': black})
    
    
#@login_required
#def game_new(request):
#    if request.method == "POST":
#        form = GameForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            if request.user.is_authenticated():
#                post.author = request.user
#            post.save()
#            return redirect('chesswave.views.game_detail', pk=post.pk)
#    else:
#        form = GameForm()
#    return render(request, 'chesswave/game_new.html', {'form': form})    
    

@login_required
def game_play(request, pk):
    game = get_object_or_404(Game, pk=pk)
    post = Move.objects.filter(game=game) 
    moves = Move.objects.filter(game=game).order_by('created_date')         
    if request.method == "POST":
        form = MoveForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.game = game
            post.save()
            return redirect('chesswave.views.game_detail', pk=game.pk)            
    else:
        form = MoveForm()
    return render(request, 'chesswave/game_play.html', {'game': game, 'form': form, 'moves': moves})
    

@login_required
def game_draft_list(request):
    games = Visa.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'chesswave/game_draft_list.html', {'games': games}) 
    

@login_required
def game_publish(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.publish()
    return redirect('chesswave.views.game_list')
    

@login_required
def game_remove(request, pk):
    game = get_object_or_404(Game, pk=pk)
    game.delete()
    return redirect('chesswave.views.game_list')
    
                    
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'chesswave/post_list.html', {'posts': posts})
  
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'chesswave/post_detail.html', {'post': post})
    

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('chesswave.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'chesswave/post_edit.html', {'form': form})



@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('chesswave.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'chesswave/post_edit.html', {'form': form}) 


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'chesswave/post_draft_list.html', {'posts': posts})

 
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('chesswave.views.post_detail', pk=pk) 

 
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('chesswave.views.post_list') 


#@login_required    
#def search_profile(request):
#    # games = Game.objects.filter().order_by('created_date')
#    players = User.objects.all()      
#    return render(request, 'chesswave/search_profile.html', {'players': players})
    

@login_required
def search_profile(request, searchresults=''):
    players = User.objects.all()               
    if request.method == "POST":
        form = SearchProfileForm(request.POST)
        if form.is_valid():
            searchquery = form.cleaned_data['searchquery']
            searchresults = User.objects.filter(username=searchquery)
            # return redirect('chesswave.views.search_profile', player=searchquery)
            # return redirect('search_profile', searchresults=searchresults)                        
    else:
        form = SearchProfileForm()
    return render(request, 'chesswave/search_profile.html', {'form': form, 'players': players, 'searchresults': searchresults}) 


@login_required            
def search_profile_results(request, player):
    # games = Game.objects.filter(white=player) | Game.objects.filter(black=player)
    # searchresults = User.objects.all()          
    searchresults = User.objects.filter(username=player)
    print(searchresults)
    return render(request, 'chesswave/search_profile_results.html', {'searchresults': searchresults})
    
    
#@login_required
#def search_profile_results(request, player):         
#    if request.method == "POST":
#        form = SearchProfileForm(request.POST)
#        if form.is_valid():
#            searchquery = form.cleaned_data['searchquery']
#            searchresults = User.objects.filter(username=searchquery)
#            return redirect('chesswave.views.search_profile_results', player=searchquery)            
#    else:
#        form = SearchProfileForm()
#    return render(request, 'chesswave/search_profile_results.html', {'player': player})    
