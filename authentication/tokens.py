import six as six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, phone,code, timestamp):
        return (
                six.text_type(phone) + six.text_type(timestamp) +six.text_type(code)
        )


account_activation_token = TokenGenerator()
Reg_Token = TokenGenerator()
