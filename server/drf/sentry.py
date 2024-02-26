import logging
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


SENTRY_CONFIG = {
    'dsn': "http://09f66d8b3b964992a5b3f3a6d6cfd4fb@94.228.112.174/3",
    'integrations': [
         DjangoIntegration(),
         LoggingIntegration(
             level=logging.INFO,  # Capture info and above as breadcrumbs
             event_level=logging.ERROR  # Send errors as events
         ),
         LoggingIntegration(
             level=logging.INFO,  # Capture info and above as breadcrumbs
             event_level=logging.WARNING  # Send errors as events
         )
    ],
    'traces_sample_rate': 1.0,
    'send_default_pii': True,
    'environment': 'production'
}


def sentry_start(sentry_config=None):
    if sentry_config is None:
        sentry_config = SENTRY_CONFIG
    print(sentry_config)
    try:
        jaja = sentry_sdk.init(sentry_config)
        print(jaja)
        return jaja
    except Exception as e:
        print(str(e))
        return str(e)
