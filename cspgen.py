from cspgen import parser
from cspgen import gen
import sys
import argparse


def main(argv):
    argparser = argparse.ArgumentParser(description='Content Security Policy generator')
    argparser.add_argument('conf', nargs='+', help='TOML configuration file')
    argparser.add_argument("-u", "--url" help="URL to crawl")
    args = argparser.parse_args()

    if args.url:
        url = args.url
        page = get_page(url)
        assets = get_asset_sources(page)
        
    for fname in args.conf:
        conf = parser.parse_toml(fname)
        if "scripts" in conf:
            scrpts = parser.get_scripts_pol(conf)
            script_pol = gen.gen_scripts_pol(scrpts)
            gen.print_policy()
    return


if __name__ == '__main__':
    main(sys.argv[1:])
