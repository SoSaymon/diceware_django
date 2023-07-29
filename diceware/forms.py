from django import forms


class DiceWareForm(forms.Form):
    word_count = forms.IntegerField(label='Number of words', min_value=3, max_value=10, initial=6, required=True, help_text='Number of words to generate')
    separator = forms.CharField(label='Separator', max_length=1, required=False, help_text='Character to separate words with', initial='-')
    capitalize = forms.BooleanField(label='Capitalize first letter', required=False, help_text='Capitalize first letter of each word', initial=True)

    def clean(self):
        cleaned_data = super().clean()
        word_count = cleaned_data.get('word_count')
        separator = cleaned_data.get('separator')
        capitalize = cleaned_data.get('capitalize')

        if not capitalize and separator == '':
            raise forms.ValidationError('Cannot capitalize first letter without a separator')

        if word_count > 10:
            raise forms.ValidationError('Cannot generate more than 10 words')

        if word_count < 3:
            raise forms.ValidationError('Cannot generate less than 3 words')

        return cleaned_data
