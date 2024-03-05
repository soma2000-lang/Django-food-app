from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from accounts.models import UserProfile
from .context_processors import get_cart_counter, get_cart_amounts
from menu.models import Category, FoodItem
from django.db.models import Prefetch
from .models import Cart
from django.contrib.auth.decorators import login_required
# we use this to  Q object filters whether the question starts with ‘what’
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``
from django.contrib.gis.db.models.functions import Distance
from datetime import date, datetime
from orders.forms import OrderForm
def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
    vendor_count = vendors.count()
    context = {
        'vendors': vendors,
        'vendor_count': vendor_count,
    }
    return render(request, 'marketplace/listings.html', context)
