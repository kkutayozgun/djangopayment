from django.shortcuts import render
from django.views.generic import View
from django.utils.crypto import get_random_string
import base64
from hashlib import sha1
from django.views.decorators.csrf import csrf_exempt

oid = "10001"
clientid = "700655000300"
storetype = "3d_pay_hosting"
islemtipi = "Auth"
currency = 949
okurl = "http://127.0.0.1:8000/payment/ok/"
failurl = "http://127.0.0.1:8000/payment/fail/"
callbackurl = "http://127.0.0.1:8000/payment/callback/"
storekey = "TRPS1234"

class PaymentView(View):
    template_name = "payment.html"

    def get(self, request):
        amount = 1.5
        rndstr = get_random_string(length=20,allowed_chars="ABCDEFGHJKLMNOPRSTUVYZ".lower())
        plaintext = f"{clientid}{oid}{amount}{okurl}{failurl}{islemtipi}{rndstr}{callbackurl}{storekey}"
        hashcode = base64.b64encode(sha1(str.encode(plaintext)).digest())
        
        context = {
            "oid": oid,
            "clientid": clientid,
            "storetype":storetype,
            "islemtipi": islemtipi,
            "currency": currency,
            "okurl": okurl,
            "failurl": failurl,
            "callbackurl": callbackurl,
            "storekey": storekey,
            "amount": amount,
            "rndstr": rndstr,
            "plaintext": plaintext,
            "hashcode": hashcode,
        }


        return render(request, self.template_name, context)

@csrf_exempt
def payment_ok(request):
    template_name = "payment_ok.html"
    print(request)
    return render(request, template_name)

@csrf_exempt
def payment_fail(request):
    template_name = "payment_fail.html"
    print(request)
    print(request.body)
    print(request.body.decode('utf-8'))
    return render(request, template_name)

@csrf_exempt
def payment_callback(request):
    template_name = "payment_callback.html"
    print(request.body)
    return render(request, template_name)

# class PaymentOnayView(View):
#     template_name = "payment_ok.html"

#     def get(self, request):
#         print(request)
#         return render(request, self.template_name)

# class PaymentFailView(View):
#     template_name = "payment_fail.html"

#     def get(self, request):
#         print(request)
#         return render(request, self.template_name)

# class PaymentCallbackView(View):
#     template_name = "payment_callback.html"

#     def get(self, request):
#         print(request)
#         return render(request, self.template_name)