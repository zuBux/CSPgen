from cspgen import parser
from cspgen import gen
from cspgen import crawler
import sys
import logging
import argparse


def main(args):
    if args.url:
        profile = {}
        url = args.url
        page = crawler.get_page(url)
        profile['js_sources'], profile['inline'] = crawler.get_js_sources(page)
        pol = gen.policy_from_crawl(profile)
        if args.output:
            gen.write_toml(args.output, pol)
        else:
            print pol
    if args.conf:
        try:
            conf = parser.parse_toml(args.conf)
        except Exception, e:
            logging.error("Unable to open/read file %s: %s", fname, str(e))
            return
        for k in conf.keys():
            cat = parser.read_policy(conf, k)
            policy = gen.gen_resource_policy(cat)
            gen.add_policy(k, policy)
        gen.print_policy()
    return


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Content Security Policy generator')
    argparser.add_argument('conf', nargs='?', type=str, help='TOML configuration file')
    argparser.add_argument("-u", "--url", help="URL to crawl")
    argparser.add_argument("-o", "--output", help="File to write CSP")
    args = argparser.parse_args()
    main(args)
