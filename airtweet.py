import configparser

_DEFAULT_CONFIG_PATH = 'airtweet.ini'


def _read_config_file(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


class AirTweet(object):
    def __init__(self, config_path=None):
        config_path = config_path or _DEFAULT_CONFIG_PATH
        config = _read_config_file(config_path)
