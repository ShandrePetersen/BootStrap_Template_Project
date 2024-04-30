from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

class IndexView(TemplateView):
    template_name = "MyPortfolio/index.html"


    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('index')
        return render(request, self.template_name, {'form': form})