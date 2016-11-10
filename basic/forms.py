from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField()

    def clean_message(self):
        '''
        CUSTOM VALIDATION RULE
        Django’s form system automatically looks for any method whose name starts with clean_
        and ends with the name of a field. If any such method exists, it’s called during validation.
        Specifically, the clean_message() method will be called after the default validation logic for a given field
        (in this case, the validation logic for a required CharField).
        :return:
        '''
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
