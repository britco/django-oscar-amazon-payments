VERSION = "0.2"

try:
    from api import AmazonPaymentsAPI, AmazonPaymentsAPIError  # noqa
except ImportError:
    pass


