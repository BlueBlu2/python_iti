from django import forms
from .models import Intake,Track, Trainee

class addTraineeForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    intakeid = forms.ChoiceField(choices=[(intake.id,intake.intakename) for intake in Intake.objects.all()])
    trackid = forms.ChoiceField(choices=[(track.id,track.name) for track in Track.objects.all()])


class addTraineeModel(forms.ModelForm):
    intakeid = forms.ChoiceField(choices=[(intake.id, intake.intakename) for intake in Intake.objects.all()])
    trackid = forms.ChoiceField(choices=[(track.id, track.name) for track in Track.objects.all()])
    class Meta:
        fields='__all__'
        model=Trainee