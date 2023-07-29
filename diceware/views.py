from django.shortcuts import render
from diceware.forms import DiceWareForm
from .utils.diceware.diceware import generate


def index(request):
    """
    Render the index page
    :param request:  The request
    :return:  The rendered index page
    """
    if request.method == 'POST':
        form = DiceWareForm(request.POST)
        if form.is_valid():
            word_count = form.cleaned_data.get('word_count')
            separator = form.cleaned_data.get('separator')
            capitalize = form.cleaned_data.get('capitalize')

            try:
                passphrase = generate(word_count, separator, capitalize)
            except ValueError as error:
                context = {
                    'form': DiceWareForm,
                    'error': error,
                    'passphrase': None,
                }
                return render(request, 'index.html', context)

            context = {
                'form': DiceWareForm,
                'error': None,
                'passphrase': passphrase,
            }

            return render(request, 'index.html', context)

    context = {
        'form': DiceWareForm,
        'error': None,
        'passphrase': None,
    }

    return render(request, 'index.html', context)
