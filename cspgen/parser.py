import toml


def parse_toml(tml_profile):
    with open(tml_profile) as conf:
        config = toml.loads(conf.read())
    return config


# read_policy reads the resource policy (js,css,img etc.) from the conf dict
def read_policy(conf, cat):
    return conf[cat]
