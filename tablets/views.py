from django.shortcuts import render, get_object_or_404
from .models import Tablets, Brand
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django.urls import reverse, reverse_lazy
from .forms import DeleteTabletForm, CreateBrandForm


def tablets_list(request):
    french_brand = Brand.objects.filter(country='FR')
    french_tablets = Tablets.objects.filter(brand__in=french_brand, release_year__gte=2015)
    others = Tablets.objects.exclude(id__in=french_tablets)
    form = DeleteTabletForm
    return render(request, 'tablets/tablets_list.html', locals())


class TabletsDelete(DeleteView):
    model = Tablets

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Tablets, id=id)

    def get_success_url(self):
        return reverse('tablets')


class BrandCreate(CreateView):
    model = Brand
    form_class = CreateBrandForm
    template_name = 'tablets/newBrand.html'
    success_url = reverse_lazy('tablets')


class TabletUpdate(UpdateView):
    model = Tablets
    template_name = 'tablets/update.html'
    fields = '__all__'
    success_url = reverse_lazy('tablets')


class TabletCreate(CreateView):
    model = Tablets
    template_name = 'tablets/newTablet.html'
    fields = '__all__'
    success_url = reverse_lazy('tablets')


class TabletDetail(DetailView):
    context_object_name = "tablet"
    model = Tablets
    template_name = "tablets/detailTablet.html"
