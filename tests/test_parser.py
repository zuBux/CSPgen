from cspgen import parser
from nose2.tests._common import TestCase
from nose2.tools.decorators import with_setup, with_teardown
import os


def setup():
    dummy_data = '''
    [scripts]
    allow = "custom"
    options = ["self"]
    hosts = ["https://google.com"]
    '''
    with open("test.toml", 'w+') as dummy:
        dummy.write(dummy_data)
    return


def teardown():
    os.remove("test.toml")
    return


@with_setup(setup)
@with_teardown(teardown)
def test_parse_toml():
    print("Running test_parse_toml")
    conf = parser.parse_toml("test.toml")
    assert 'scripts' in conf
    assert conf['scripts']['allow'] == "custom"
    assert conf['scripts']['options'][0] == "self"
    assert conf['scripts']['hosts'][0] == "https://google.com"


@with_setup(setup)
@with_teardown(teardown)
def test_get_scripts_pol():
    print("Running test_get_scripts_pol")
    conf = parser.parse_toml("test.toml")
    scripts = parser.get_scripts_pol(conf)
    assert scripts['allow'] == "custom"
    assert scripts['options'][0] == "self"
    assert scripts['hosts'][0] == "https://google.com"
