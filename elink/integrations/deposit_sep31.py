from typing import Dict, List
from polaris.integrations import SEP31ReceiverIntegration
from polaris.sep10.token import SEP10Token
from polaris.models import Asset, Transaction
from rest_framework.request import Request
from .user import user_for_account, user_for_id, verify_bank_account
# from .rails import calculate_fee, memo_for_transaction

class AnchorCrossBorderPayment(SEP31ReceiverIntegration):
    def info(
        request: Request,
        asset: Asset,
        lang: str,
        *args: Dict,
        **kwargs: List
    ):
        return {
            "sep12": {
                "sender": {
                    "types": {
                        "sep31-sender": {
                            "description": "the basic type for sending customers"
                        }
                    }
                },
                "receiver": {
                    "types": {
                        "sep31-receiver": {
                            "description": "the basic type for receiving customers"
                        }
                    }
                },
            },
            "fields": {
                "transaction": {
                    "routing_number": {
                        "description": "routing number of the destination bank account"
                    },
                    "account_number": {
                        "description": "bank account number of the destination"
                    },
                },
            },
        }

    def process_post_request(
        self,
        token: SEP10Token,
        request: Request,
        params: Dict,
        transaction: Transaction,
        *args: List,
        **kwargs: Dict,
    ):
        sending_user = user_for_id(params.get("sender_id"))
        receiving_user = user_for_id(params.get("receiver_id"))

        # KYC approved?
        if sending_user == None:
            return {"error": "customer_info_needed", "type": "sep31-sender"}
        if receiving_user == None:
            return {"error": "customer_info_needed", "type": "sep31-receiver"}

        # Transaction check
        transaction_fields = params.get("fields", {}).get("transaction")
        if not transaction_fields:
            return {
                "error": "transaction_info_needed",
                "fields": {
                    "transaction": {
                        "routing_number": {
                            "description": "routing number of the destination bank account"
                        },
                        "account_number": {
                            "description": "bank account number of the destination"
                        },
                    }
                }
            }

        try:
            verify_bank_account(
                transaction_fields.get("routing_number"),
                transaction_fields.get("account_number")
            )
        except ValueError:
            return {"error": "invalid routing or account number"}
        # sending_user.add_transaction(transaction)
        # receiving_user.add_transaction(transaction)