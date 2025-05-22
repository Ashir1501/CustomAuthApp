from django import forms
from .models import Post, Category
class PostModelForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select a Category',
        widget=forms.Select(attrs={'class':'form-control'})
    )
    class Meta:
        model = Post
        fields = ['title','image','category','summary','content','is_draft']
        labels = {
            'is_draft':'Set as Draft'
        }
        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'summary': forms.Textarea(attrs={'class':'form-control', 'style':'height:200px;'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'Set as Draft': forms.CheckboxInput(attrs={'class':'form-control'})
        }
