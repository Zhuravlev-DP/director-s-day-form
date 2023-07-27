from django import forms
from questions.models import Division, Enterprise, Question


class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['title', ]
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'})
        }


class EnterpriseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['division'].empty_label = 'Выберите ваш дивизион'

    class Meta:
        model = Enterprise
        fields = ['title', 'division']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'division': forms.Select(attrs={'class': 'form-control'})
        }


class AddQuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['enterprise'].required = False
        self.fields['enterprise'].empty_label = 'другое'

    class Meta:
        model = Question
        fields = ['enterprise', 'email', 'text']
        widgets = {
            'enterprise': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
