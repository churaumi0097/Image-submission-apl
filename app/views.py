from django.shortcuts import render
from django.views.generic import (
    TemplateView,ListView,DetailView
)
from django.views.generic.edit import(
    CreateView,DeleteView,UpdateView
)
from .models import Item
from .forms import CreateForm
from django.db.models import Q
from django.contrib import messages
import os
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name = "home.html"


class Index(ListView):
    model = Item
    content_object_name = "items"
    template_name = "index.html"

    def get_queryset(self):
        queryset = Item.objects.order_by("-time")
        query = self.request.GET.get("query")

        if query:
            queryset = queryset.filter(
                Q(title__icontains = query) | Q(content__icontains = query) | Q(time__icontains = query)
            )
        messages.add_message(self.request, messages.INFO, query)
        return queryset

class Detail(DetailView):
    model = Item
    context_object_name = "item"
    template_name = "detail.html"


class Create(CreateView):
    model = Item
    form_class = CreateForm
    template_name = "create.html"
    success_url = reverse_lazy("index")
    

class Delete(DeleteView):
    model = Item
    template_name = "delete.html"
    success_url = reverse_lazy("index")


class Update(UpdateView):
    model = Item
    fields = ["title","content","image","time"]
    template_name = "update.html"
    success_url = reverse_lazy("index")
    