from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
a=""

confirmation_token = default_token_generator.make_token(a)
print(confirmation_token)