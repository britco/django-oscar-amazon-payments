from pkg_resources import get_distribution

__version__ = get_distribution('django-oscar-amazon-payments').version

VERSION = __version__

try:
    from api import AmazonPaymentsAPI, AmazonPaymentsAPIError  # noqa
except ImportError:
    pass


