import decimal
from django.shortcuts import render
from .models import ElinkStellarAccount, ElinkUser, ElinkUserKYC, ElinkPayment

# Create your views here.

def user_for_account(account_id):
    #to get the user account linked to a stellar public key
    
    try:
        stellar_account = ElinkStellarAccount.objects.get(account=account_id)\
        or\
        ElinkStellarAccount.objects.get(memo=account_id)
        
        return ElinkUser.objects.get(id=stellar_account.user.id)
    except:
        return None

def fields_for_type(type):
    return {
        "bank_account_number": {
            "description": "bank account number of the customer",
            "type": "string"
        },
        "bank_number": {
            "description": "routing number of the customer",
            "type": "string"
        },
        "email_address": {
            "description": "email address of the customer",
            "type": "string"
        },
        "first_name": {
            "description": "first name of the customer",
            "type": "string",
        },
        "last_name": {
            "description": "last name of the customer",
            "type": "string"
        },
        "photo_id_back": {
            "description": "Image of back of user's photo ID or passport",
            "optional": True,
            "type": "binary"
        },
        "photo_id_front": {
            "description": "Image of front of user's photo ID or passport",
            "optional": True,
            "type": "binary"
        }
    }