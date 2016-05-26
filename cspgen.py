from cspgen import parser
from cspgen import gen
from cspgen import crawler
import sys
import argparse


def main(argv):
    argparser = argparse.ArgumentParser(description='Content Security Policy generator')
    argparser.add_argument('conf', nargs='?', help='TOML configuration file')
    argparser.add_argument("-u", "--url", help="URL to crawl")
    args = argparser.parse_args()

    if args.url:
        profile = {}
        url = args.url
        page = crawler.get_page(url)
        profile['js_sources'], profile['inline'] = crawler.get_js_sources(page)
        pol = gen.policy_from_crawl(profile)
        print pol
    if args.conf:
        for fname in args.conf:
            conf = parser.parse_toml(fname)
            if "scripts" in conf:
                scrpts = parser.get_scripts_pol(conf)
                script_pol = gen.scripts_pol(scrpts)
                gen.print_policy()
    return


if __name__ == '__main__':
    main(sys.argv[1:])
