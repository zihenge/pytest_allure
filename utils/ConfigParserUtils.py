from configparser import ConfigParser


# 覆盖父类中默认小写的读取方式
class ConfigParserUtils(ConfigParser):
    """
    set ConfigParser options for case sensitive.
    """

    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr
