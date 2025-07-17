from django import forms
from .models import CATEGORY_CHOICES, TITLE_CHOICES, AGE_GROUP_CHOICES

class CombinedRegistrationForm(forms.Form):
    # Step 1: Church
    church_name = forms.CharField(label="Church Name", max_length=100)
    church_district = forms.CharField(label="Church District", max_length=100)

    # Step 2: Attendee
    attendee_name = forms.CharField(label="Full Name", max_length=100)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Category")
    detail = forms.ChoiceField(label="Title/Age", required=True)

    # Step 4: Billing
    amount_paid = forms.DecimalField(label="Amount Paid", decimal_places=2, max_digits=10)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        data = self.data or self.initial
        category = data.get('category', '')

        # Set appropriate choices dynamically based on category
        if category == 'adult':
            self.fields['detail'].choices = TITLE_CHOICES
        elif category == 'child':
            self.fields['detail'].choices = AGE_GROUP_CHOICES
        else:
            self.fields['detail'].choices = []



