from datetime import datetime

from django.shortcuts import render
from diceware.forms import DiceWareForm
from .utils.diceware.diceware import generate


def index(request):
    """
    Render the index page
    :param request:  The request
    :return:  The rendered index page
    """
    year = datetime.now().year

    context = {
        'year': str(year),
        'form': DiceWareForm,
        'error': None,
        'passphrase': None,
        'cookies': {'word_count': None, 'separator': None, 'capitalize': None}
    }

    if request.method == 'POST':
        form = DiceWareForm(request.POST)
        if form.is_valid():
            word_count = form.cleaned_data.get('word_count')
            separator = form.cleaned_data.get('separator')
            capitalize = form.cleaned_data.get('capitalize')

            try:
                word_count = int(word_count)
            except ValueError:
                context['error'] = 'Word count must be an integer'

                return render(request, 'index.html', context)

            try:
                capitalize = bool(capitalize)
            except ValueError:
                context['error'] = 'Capitalize must be a boolean'

                return render(request, 'index.html', context)

            try:
                passphrase = generate(word_count, separator, capitalize)
            except ValueError as error:
                context['error'] = error.args[0]

                return render(request, 'index.html', context)

            context['passphrase'] = passphrase

            response = render(request, 'index.html', context)
            response.set_cookie('word_count', word_count, max_age=60 * 60 * 24 * 365, samesite='Strict', secure=True)
            response.set_cookie('separator', separator, max_age=60 * 60 * 24 * 365, samesite='Strict', secure=True)
            response.set_cookie('capitalize', capitalize, max_age=60 * 60 * 24 * 365, samesite='Strict', secure=True)

            return response

    return render(request, 'index.html', context)
