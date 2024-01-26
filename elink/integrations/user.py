import decimal
from django.shortcuts import render
from .models import ElinkStellarAccount, ElinkUser, ElinkUserKYC, ElinkPayment

# Create your views here.

def user_for_account(account_id):
    #to get the user account linked to a stellar public key
        
    try:
        stellar_account = ElinkStellarAccount.objects.filter(account=account_id)\
                            or ElinkStellarAccount.objects.filter(memo=account_id)

        if stellar_account.count() == 1:
            return stellar_account.values()[0]

        return None
    except:
        print('Error')
        return None

def save_customer(account, fields):
    try:
        return ElinkStellarAccount.objects.create(
            id=15,
            memo = "1",
            memo_type = "2",
            account = account,
            muxed_account = account,
            secret_key = "14233",
            confirmed = True,
            confirmation_token = "12341423",
            user_id=12345,
        )
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