from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from marketplace.models import Cart, Tax
from marketplace.context_processors import get_cart_amounts
from menu.models import FoodItem
from .forms import OrderForm
from .models import Order, OrderedFood, Payment
import simplejson as json
from .utils import generate_order_number, order_total_by_vendor
from accounts.utils import send_notification
from django.contrib.auth.decorators import login_required
import razorpay
from resturant.settings import RZP_KEY_ID, RZP_KEY_SECRET
from django.contrib.sites.shortcuts import get_current_site

client = razorpay.Client(auth=(RZP_KEY_ID, RZP_KEY_SECRET))
