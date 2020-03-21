from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic import DayArchiveView, TodayArchiveView
from django.views.generic import FormView
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render

from .models import Product
from .forms import ProductSearchForm

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

from .crawlapps import amazon


#--- ListView
class ProductLV(ListView):
    model = Product
    template_name = 'crawl/product_all.html'
    context_object_name = 'products'
    paginate_by = 20


#--- DetailView
class ProductDV(DetailView):
    model = Product


#--- FormView
class CrawlFormView(LoginRequiredMixin, FormView):
    form_class = ProductSearchForm
    template_name = 'crawl/product_search.html'

    def form_valid(self, form):
        categoryNumber = form.cleaned_data['category_number']
        productNumber = int(form.cleaned_data['product_number'])

        prods = amazon.crawlproduct(categoryNumber, productNumber)

        print(type(prods))
        print(prods.iloc[0]['rank'])
        print(prods.iloc[0]['title'])

        for i in range(productNumber):
            prod = Product()
            prod.ranking = prods.iloc[i]['rank']
            prod.title = prods.iloc[i]['title']
            prod.price = prods.iloc[i]['price']
            prod.sat_count = prods.iloc[i]['review']
            prod.score = prods.iloc[i]['score']
            prod.image = prods.iloc[i]['image']
            prod.save()

        context = {}
        context['form'] = form
        context['category_code'] = categoryNumber
        context['product_n'] = productNumber

        return render(self.request, self.template_name, context)   # No Redirection
