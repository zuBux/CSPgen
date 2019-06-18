import mimetypes
import os
import toml
import yaml
from yaml.error import YAMLError


def use_parser(file):
    filename, file_extension = os.path.splitext(file)
    if file_extension in (".toml"):
        return parse_toml(file)
    if file_extension in (".yaml"):
        return parse_yaml(file)
    msg = u"No configuration file given".format(path)
    logging.error(msg)
    raise IOError(msg)


def parse_toml(tml_profile):
    with open(tml_profile) as conf:
        config = toml.loads(conf.read())
    return config


def parse_yaml(path):
    print("yaml parser")
    try:
        with open(path, "r") as file:
            config = yaml.load(file.read(), Loader=yaml.FullLoader)
    except YAMLError as e:
        msg = (
            u"Cannot parse YAML from given path '{0}'. "
            + u"Original exception was:\n{1}: {2}"
        )
    except IOError as e:
        msg = u"File not found: '{0}'".format(path)
        logging.error("Unable to open/read file %s: %s", fname, str(e))
        raise IOError(msg)
    return config


# read_policy reads the resource policy (js,css,img etc.) from the conf dict
def read_policy(conf, cat):
    return conf[cat]
