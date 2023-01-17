from django.shortcuts import render
from markdown2 import markdown
from . import util

def md_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()    
    if content == None:
        return None
    else: 
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content == None:
        return render(request, "encyclopedia/notExist.html",{
            'title': title
        })
    else:
        content = markdown(content)
        return render(request, "encyclopedia/entry.html", {
            'content': content, 
            'title': title
            })