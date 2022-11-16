from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category, Product, SavingsProduct
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def index(request):
    category_list = Category.objects.order_by('-id')
    product_list = Product.objects.order_by('-date_posted')
    savings_products_list = SavingsProduct.objects.order_by('-date_posted')
    paginator = Paginator(category_list, 3) # 3 categories in each page
    paginator2 = Paginator(product_list, 8) # 3 categories in each page
    paginator3 = Paginator(savings_products_list, 8) # 3 categories in each page
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
        products = paginator2.page(page)
        savings_products = paginator3.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        categories = paginator.page(1)
        products = paginator2.page(1)
        savings_products = paginator3.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        categories = paginator.page(paginator.num_pages)
        products = paginator2.page(paginator.num_pages)
        savings_products = paginator3.page(paginator.num_pages)
        
    
    context = {
        'categories': categories,
        'page': page,
        'products': products,
        'savings_products': savings_products
    }
    return render(request, 'delight/index.html', context)

@login_required
def about_us(request):
    return render(request, 'delight/about_us.html')


@login_required
def contact_us(request):
    return render(request, 'delight/contact_us.html')


@login_required
def store(request):
    category_list = Category.objects.order_by('-id')
    product_list = Product.objects.order_by('-date_posted')
    savings_products_list = SavingsProduct.objects.order_by('-date_posted')
    paginator = Paginator(category_list, 5) # 3 categories in each page
    paginator2 = Paginator(product_list, 12) # 3 categories in each page
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
        products = paginator2.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        categories = paginator.page(1)
        products = paginator2.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        categories = paginator.page(paginator.num_pages)
        products = paginator2.page(paginator.num_pages)
        
    # products = Product.objects.all()
    # categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'delight/store.html', context)


@login_required
def product(request, product_id):
    product = Product.objects.get(id=product_id)
    products = Product.objects.filter(category=product.category)
    context = {'product': product, 'products': products}
    return render(request, 'delight/product.html', context)


@login_required
def category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.product.all()
    context = {'category': category, 'products': products}
    return render(request, 'delight/category.html', context)



@login_required
def savings_product(request, product_id):
    product = SavingsProduct.objects.get(id=product_id)
    products = SavingsProduct.objects.filter(category=product.category)
    context = {'product': product, 'products': products}
    return render(request, 'delight/savings_product.html', context)


class SearchResultsView(ListView):
    model = Product
    template_name = 'delight/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
        Q(name__icontains=query) 
        )
        return object_list


@login_required
def mobile_search(request):
    return render(request, 'delight/mobile_search.html')