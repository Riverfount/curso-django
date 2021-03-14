from pypro.core.apps import CoreConfig


def tests_app_name():
    assert CoreConfig.name == 'core'
