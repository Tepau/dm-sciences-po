from django.shortcuts import render, get_object_or_404
from .models import Tablets, Brand
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django.urls import reverse, reverse_lazy
from .forms import DeleteTabletForm, CreateBrandForm


def tablets_list(request):
    """
        Function to display tablet's lists
        french_tablets ==> All French-brand tablets released between 2015 and 2020
        others ==> All others tablets
    """
    french_brand = Brand.objects.filter(country='FR')  # Select all french brands
    french_tablets = Tablets.objects.filter(brand__in=french_brand, release_year__gte=2015)
    others = Tablets.objects.exclude(id__in=french_tablets)
    form = DeleteTabletForm
    return render(request, 'tablets/tabletsList.html', locals())


class TabletsDelete(DeleteView):
    """
    Class to delete a tablet
    """

    model = Tablets

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Tablets, id=id)

    def get_success_url(self):
        return reverse('tablets')


class BrandCreate(CreateView):
    """
        Class to create a new brand
    """
    model = Brand
    form_class = CreateBrandForm
    template_name = 'tablets/newBrand.html'
    success_url = reverse_lazy('tablets')


class TabletUpdate(UpdateView):
    """
    Class to update tablet's information
    """
    model = Tablets
    template_name = 'tablets/update.html'
    fields = '__all__'
    success_url = reverse_lazy('tablets')


class TabletCreate(CreateView):
    """
    Class to create a new tablet
    """

    model = Tablets
    template_name = 'tablets/newTablet.html'
    fields = '__all__'
    success_url = reverse_lazy('tablets')


class TabletDetail(DetailView):
    """
    Class to display the details of a tablet
    """

    context_object_name = "tablet"
    model = Tablets
    template_name = "tablets/detailTablet.html"
