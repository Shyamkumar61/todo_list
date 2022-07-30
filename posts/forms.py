from django import forms

class Todo_listForm(forms.Form):

    STATUS = (
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        ('Pending', 'Pending')
    )
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=STATUS)




