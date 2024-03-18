import logging
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


SENTRY_CONFIG = {
    'dsn': "http://0e039f5f6aab49d18f90c2449a206e12@glitchtip.flexidev.ru/2",
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
