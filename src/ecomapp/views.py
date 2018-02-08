from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
# from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.db.models import Q
from .forms import ProductForm
from .models import Product
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator


class ProdIndexView(generic.ListView):

    model = Product
    template_name = 'index.html'
    context_object_name = 'products'


class ProdDetailView(generic.DetailView):

    model = Product
    context_object_name = 'product'
    template_name = 'prod_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProdDetailView,self).get_context_data(**kwargs)
        print(context.values())
        return context

class ProdDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('ecomapp:index')


class ProdCreateView(generic.CreateView):

    model = Product
    form_class = ProductForm
    template_name = 'create_prod.html'
    success_url = reverse_lazy("ecomapp:index")

    def post(self, request, *args, **kwargs):
        form = self.get_form(ProductForm)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user.get_username()
            f.save()
            return self.form_valid(form)
        else:
            return HttpResponse("try again")

class ProdUpdateView(generic.UpdateView):

    model = Product
    form_class = ProductForm
    template_name = 'create_prod.html'
    success_url = reverse_lazy("ecomapp:index")

def search_prod(request):

    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    prods = Product.objects.filter(name__contains=search_text)
    return render_to_response('ajax_search.html',{'products':prods})


def search_prod_new(request):

    template = 'prod_detail.html'
    if request.method == "POST":
        query = request.POST['q']
        if query:
            results = Product.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
            if results:
                return render(request,'prod_detail.html', {'products': results})
    return render(request, template)

def search_sighs_3rdOne(request):
    try:
        q = request.GET['q']
        posts = Product.objects.filter(name__icontains=q)
        return render_to_response('prod_detail.html', {'posts':posts, 'q':q})
    except KeyError:
        return render_to_response('prod_detail.html')