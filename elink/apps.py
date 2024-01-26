from django.apps import AppConfig

class AnchorConfig(AppConfig):
    name = "elink"

    def ready(self):
        from polaris.integrations import register_integrations
        
        from .integrations import (
            toml_contents,
            info,
            AnchorCustomer,
            AnchorDeposit,
            AnchorDepositSep6,
            AnchorWithdraw,
            AnchorWithdrawSep6,
            AnchorRails,
            AnchorCrossBorderPayment,
        )

        register_integrations(
            toml=toml_contents,
            customer=AnchorCustomer(),
            sep6_info=info,
            deposit=AnchorDepositSep6(),
            withdrawal=AnchorWithdrawSep6(),
            rails=AnchorRails(),
            sep31_receiver=AnchorCrossBorderPayment(),
        )