from django import forms
from depts.models import Department
from students.models import Student


class StudentForm(forms.Form):
    name = forms.CharField(label="Student name", min_length=5)
    img = forms.CharField(label="Student img")
    email = forms.EmailField(label="Student Email:")
    # male or female
    gender = forms.ChoiceField(
        choices=[
            ("m", "Male"),
            ("f", "Female")
        ]
    )
    # department value --->
    dept = forms.ModelChoiceField(Department.objects.all())



class StudentModelForm(forms.ModelForm):
    # create from according the model , just specify fields
    class Meta:
        model = Student
        fields = ["name", "img", "email", "gender", "dept"]





