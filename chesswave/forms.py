from django import forms
from django.forms import ModelForm, TextInput
from .models import Game
from .models import Move
from .models import Post
from django.contrib.auth.models import User 
   
                
class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('white', 'black',)
        widgets = {
                    'white': forms.HiddenInput(),
                    'black': forms.HiddenInput()
                }                    
    
            
class MoveForm(forms.ModelForm):

    class Meta:
        model = Move
        fields = ('move',)
        widgets = {
                    'move': forms.TextInput(attrs={'size': 10})
                }   
    
        
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',) 
        

class SearchProfileForm(forms.Form):
    searchquery = forms.CharField(label='Player', max_length=100)             
        
        
#class GameForm(forms.ModelForm):

#    class Meta:
#        model = Game
#        fields = ('white', 'black',)
        

#class GameForm(forms.ModelForm):

#    class Meta:
#        model = Game
#        fields = ('white', 'black',)
#        
#    def __init__(self, *args, **kwargs):        
#        super(GameForm, self).__init__(*args, **kwargs)
#        self.fields['white'].queryset = queryset=User.objects.all()        
        

#class PictureForm(forms.ModelForm):
#    class Meta:
#        model = Picture

#    def __init__(self, user, *args, **kwargs):
#        super(PictureForm, self).__init__(*args, **kwargs)
#        self.fields['Whiteboard'].queryset = Whiteboard.objects.filter(user=user)


#class GameForm(forms.Form):
#    model = Game
#    white = forms.ModelChoiceField(queryset=User.objects.all())
#    black = forms.ModelChoiceField(queryset=User.objects.all())             
