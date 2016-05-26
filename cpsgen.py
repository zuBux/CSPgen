from cspgen import parser
from cspgen import gen
import sys
import argparse


def main(argv):
    url = argv[0]

    argparser = argparse.ArgumentParser(description='Content Security Policy generator')
    argparser.add_argument('conf', nargs='+', help='TOML configuration file')
    args = argparser.parse_args()
    for fname in args.conf:
        conf = parser.parse_toml(fname)
        if "scripts" in conf:
            scrpts = parser.get_scripts_pol(conf)
            script_pol = gen.gen_scripts_pol(scrpts)
            gen.print_policy()
    return


if __name__ == '__main__':
    main(sys.argv[1:])
