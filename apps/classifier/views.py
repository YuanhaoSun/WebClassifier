from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from nltk.book import *

# Test using other module
from hello import Hellow
hi = Hellow()

texts = [text1, text2, text3, text4, text5, text6, text7, text8, hi]

def home(request):
    return render_to_response('home.html', RequestContext(request, dict(texts=texts)))

def classify(request):
    if request.method == "POST":
        corpus = texts[int(request.POST['corpus'])]
        word = request.POST['word']
        count = corpus.count(word)

        context = {
            'count' : count,
            'word' : word,
            'corpus' : corpus,
            }
        return render_to_response('results.html', RequestContext(request, context))
