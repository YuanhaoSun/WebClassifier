from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

# from nltk.book import *

# Test using other module
from hello import Hellow
hi = Hellow()

from classifier import classification

# texts = [text1, text2, text3, text4, text5, text6, text7, text8, hi]
texts = ['SVM', 'NB', 'SGC', 'kNN']


def home(request):
    return render_to_response('home.html', RequestContext(request, dict(texts=texts)))

def classify(request):
    if request.method == "POST":
        algo = texts[int(request.POST['class_algo'])]
        word = request.POST['word']
        # count = corpus.count(word)
        category = classification(word)

        context = {
            'category' : category,
            'word' : word,
            'algo' : algo,
            }
        return render_to_response('results.html', RequestContext(request, context))
