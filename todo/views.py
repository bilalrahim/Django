from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = ["foo", "fee", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
# Create your views here.

def index(request):
    return render(request, "todo/index.html", {
        "tasks" : tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("todo:index")) # Redirecting the user to index page.
        else:
            return render(request, "todo/add.html", {
                "form" : form
            })
    return render(request, "todo/add.html", {
        "form" : NewTaskForm()
    })