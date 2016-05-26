import toml

def parse_toml(tml_profile):
    with open(tml_profile) as conf:
        config = toml.loads(conf.read())
    return config


# get_scripts_pol returns the scripts policy from the conf dict
def get_scripts_pol(conf):
    return conf['scripts']
