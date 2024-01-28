from django.shortcuts import render, get_object_or_404, redirect
from .models import *

from django.views.generic import DetailView, ListView
from django.contrib.auth import login

from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm, ContactForm

from django.contrib import messages


from django.http import JsonResponse
from django.views.decorators.cache import cache_page





@cache_page(24 * 60 * 60)
def home(request):
    blogs = BlogPost.objects.all()
    product = Product.objects.all()
    categories = Category.objects.all()

    #All Men's GIfts
    men_category = Category.objects.get(name='Men')
    women_category = Category.objects.get(name='Women')
    kids_category = Category.objects.get(name='Kids')

    men_products = Product.objects.filter(category=men_category)
    women_products = Product.objects.filter(category=women_category)
    kids_products = Product.objects.filter(category=kids_category)



    context = {
        'blogs':blogs,
        'products': product,
        'categories': categories,

        'men_categories':men_category,
        'women_categories':women_category,
        'kids_categories':women_category,

        'men_products':men_products,
        'women_products':women_products,
        'kids_products':kids_products,
    }
    return render(request, 'evergiftful/index.html', context)





def gifts(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'evergiftful/gifts.html', context)




class ProductsByCategoryView(ListView):
    model = Product
    template_name = 'evergiftful/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()  # Change here to get all categories
        context['blogs'] = BlogPost.objects.all()
        return context








class ProductDetail(DetailView):
    model = Product
    template_name = 'evergiftful/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the current product
        product = self.get_object()

        # Filter related images for the current product
        related_images = ProductImage.objects.filter(product=product)

        # Get related products for the current product
        related_products = product.related_products.all()

        context['related_images'] = related_images
        context['related_products'] = related_products

        # Check if the user is authenticated
        user = self.request.user
        context['user_authenticated'] = user.is_authenticated

        # Check if the product is in the user's wishlist
        if user.is_authenticated:
            context['product_in_wishlist'] = Wishlist.objects.filter(user=user, products__id=product.id).exists()

        return context

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            product_id = request.POST.get('product_id')

            if product_id:
                product = Product.objects.get(id=product_id)
                wishlist, created = Wishlist.objects.get_or_create(user=request.user)
                wishlist.products.add(product)

                return JsonResponse({'message': 'Product added to wishlist successfully'})

        return JsonResponse({'message': 'Failed to add product to wishlist'})





def blogs(request):
    blog = BlogPost.objects.all()

    context = {
        'blogs':blog,
    }
    return render(request, 'evergiftful/blogs.html', context)



class BlogDetail(DetailView):
    model = BlogPost
    template_name = 'evergiftful/blogpost_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add related articles to the context
        context['related_articles'] = self.object.related_articles.all()

        return context

    



def about(request):
    return render(request, 'evergiftful/about.html')











def wishlist(request):
    if request.user.is_authenticated:
        user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist_products = user_wishlist.products.all()
    else:
        wishlist_products = []

    context = {
        'wishlist': wishlist_products,
    }

    return render(request, 'evergiftful/wishlist.html', context)




def wishlist_remove(request, product_id):
    if request.method == 'POST' and request.user.is_authenticated:
        user_wishlist = get_object_or_404(Wishlist, user=request.user)
        product = get_object_or_404(Product, id=product_id)  # Replace Product with your actual model
        user_wishlist.products.remove(product)

    return redirect('evergiftful:wishlist')






def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the previous page or home if 'next' is not present
                return redirect(request.GET.get('next', 'evergiftful:home'))
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('giftideas:home')  # Redirect to the home page after successful signup
    else:
        form = SignUpForm()

    return render(request, 'account/signup.html', {'form': form})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you within 3 business days.')
            return redirect('evergiftful:contact')

    else:
        form = ContactForm()

    return render(request, 'evergiftful/contact.html', {'form': form})