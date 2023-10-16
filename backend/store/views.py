from django.shortcuts import render, HttpResponse
from .models import Product, Transactions
from .serializers import ProductSerializer, TransactionSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from backend import settings
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.


def index(request):
    return HttpResponse('Hello wrold')


@csrf_exempt
def products(request):
    match request.method:
        case "GET":
            allData = Product.objects.all()
            products_serializer = ProductSerializer(allData, many=True)
            return JsonResponse(products_serializer.data, safe=False)


@csrf_exempt
def transactions(request):
    match request.method:
        case "GET":
            allTransactions = Transactions.objects.all()
            transactions_serializer = TransactionSerializer(
                allTransactions, many=True)
            return JsonResponse(transactions_serializer.data, safe=False)
        case "POST":
            transaction_data = JSONParser().parse(request)
            transactions_serializer = TransactionSerializer(
                data=transaction_data)
            if (transactions_serializer.is_valid()):
                transactions_serializer.save()
                return JsonResponse("Transaction is added to the database", safe=False)
            return JsonResponse('Failed to add', safe=False)


@require_POST
@csrf_exempt
def create_payment_method(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    if request.method == 'POST':
        product_data = JSONParser().parse(request)
        session = stripe.checkout.Session.create(
            metadata={
                "product_id": product_data['id']
            },
            payment_method_types=['card'],
            line_items=[
                {

                    "price_data": {
                        "product_data": {
                            "name": product_data['title'],
                            "images": [product_data['image']],
                        },
                        "unit_amount": int(product_data['price']*100),
                        "currency":"inr",
                    },
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=settings.REDIRECT_URL + \
            '/success/?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.REDIRECT_URL + '/cancel'
        )
        return JsonResponse({'url': session.url}, safe=False)


def payment_successfull(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    transaction_data = {
        "product_id": session["metadata"]["product_id"],
        "transaction_amount": session["amount_total"]/100,
        "payment_status": session["payment_status"] == "paid",
        "transaction_id": checkout_session_id
    }
    transactions_serializer = TransactionSerializer(data=transaction_data)
    if (transactions_serializer.is_valid()):
        transactions_serializer.save()
    context = {
        'data': session
    }
    if (transactions_serializer.is_valid()):
        return render(request, 'success.html',  context)
    else:
        return render(request, 'error.html')


def payment_cancel(request):
    return render(request, 'cancel.html')
