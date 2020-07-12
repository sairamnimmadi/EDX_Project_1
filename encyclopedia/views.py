from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from . import util
from django.urls import reverse
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    text = util.get_entry(title)
    if(text == None):
        return render(request, 'encyclopedia/error.html', {'text': "Page not found (404)", 'title': title, 'method': "GET", 'error': "true"})
    return render(request, 'encyclopedia/title.html', {'text': text, 'title': title, 'method': "POST", 'error': ""})


def add_page(request):
    if request.method == "POST":
        new_title = request.POST.get('title').capitalize()
        all_entires = util.list_entries()
        content = request.POST.get('markdown-content')
        if(new_title in all_entires):
            return render(request, 'encyclopedia/error.html', {'text': "Page Already Exists", 'title': new_title, 'method': "POST", 'error': "false"})
        else:
            util.save_entry(new_title, content)
            return redirect("wiki/"+new_title)
    return render(request, 'encyclopedia/createpage.html')


def edit(request, edit_title):
    text = util.get_entry(edit_title)
    if request.method == "POST":
        content = request.POST.get('markdown-content')
        util.save_entry(edit_title, content)
        # In urls name to redirect to use in reverse function
        return HttpResponseRedirect(reverse('title', args=[edit_title]))
    return render(request, 'encyclopedia/edit.html', {"title": edit_title, "content": text})


def rand(request):
    num_range = len(util.list_entries())
    num = random.randint(0, 100000000)
    num = num % num_range
    return HttpResponseRedirect(reverse('title', args=[util.list_entries()[num]]))


def search(request):
    if request.method == "POST":
        query = request.POST.get('q')
        entries = util.list_entries()
        finlis = []
        for entry in entries:
            if query.lower() in entry.lower():
                finlis.append(entry)
        return render(request, "encyclopedia/search.html", {
            "entries": finlis
        })
