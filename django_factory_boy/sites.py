from django.contrib.sites.models import Site

import factory

__all__ = (
    'SiteF',
)


class SiteF(factory.Factory):
    FACTORY_FOR = Site

    name = factory.Sequence(lambda n: "site%s" % n)
    domain = factory.Sequence(lambda n: "site%s.com" % n)
