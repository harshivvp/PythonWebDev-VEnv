from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.http import is_safe_url
from django.views import generic

from .forms import ProductForm, UserForm
from .filters import ProductFilter
from .models import Product
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import REDIRECT_FIELD_NAME
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


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
        if not request.user.is_authenticated:
            return HttpResponseRedirect("login.html")
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

class LogOutView(generic.RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)

class LoginView(generic.FormView):




    success_url = 'ecomapp:index'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    def form_valid(self, form):
        login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


def search(request):
    template_name = 'search_temp.html'
    prod_list = Product.objects.all()
    filter = ProductFilter(request.GET, queryset=prod_list)
    return render(request,template_name, {'filter': filter})


def search2(request):
    template_name = 'search_temp2.html'
    prod_list = Product.objects.all()
    filter = ProductFilter(request.GET, queryset=prod_list)
    return render(request,template_name, {'filter': filter})


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                prods = Product.objects.filter(user=request.user)
                return render(request, 'index.html', {'products': prods})
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

# def search_prod(request):
#
#     if request.method == "POST":
#         search_text = request.POST['search_text']
#     else:
#         search_text = ''
#
#     prods = Product.objects.filter(name__contains=search_text)
#     return render_to_response('ajax_search.html',{'products':prods})
#
#
# def search_prod_new(request):
#
#     template = 'prod_detail.html'
#     if request.method == "POST":
#         query = request.POST['q']
#         if query:
#             results = Product.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
#             if results:
#                 return render(request,'prod_detail.html', {'products': results})
#     return render(request, template)

# def search_sighs_3rdOne(request):
#     query = request.GET.get('q', None)
#     qs = Product.objects.all()
#     if query is not None:
#         qs = qs.filter(Q(category__icontains=query) |
#                        Q(desc__icontains=query) |
#                        Q(name__icontains=query) |
#                        Q(price__icontains=query)
#                        )
#
#     context = {
#         'products': qs,
#     }
#     template = 'index.html'
#     return render(request, template, context)