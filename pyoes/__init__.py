# -*- coding: utf-8 -*-

# pyramid is an optional extra, so it is only imported when actually used.


def main(global_config, **settings):  # pragma: no cover
    from pyoes.pyramid import main

    return main(global_config, **settings)


def includeme(config):
    from pyoes.pyramid import includeme

    return includeme(config)
