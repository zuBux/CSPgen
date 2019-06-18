import logging
import toml

csp_headers = {}


# generates CSP header for a given resource type
def gen_resource_policy(res):
    src_pol = []
    if (len(res['options']) | len(res['hosts'])) == 0:
        logging.info("no options and hosts detected, switching to 'none'")
        src_pol.append("'none'")
        return src_pol
    else:
        for option in res['options']:
            src_pol.append(_translate_keyword(option))
    if 'hosts' in res:
        if '*' in res['hosts']:
            if 'self' in src_pol:
                src_pol.remove('self')
            src_pol.append('*')
            return src_pol
        else:
            for host in res['hosts']:
                src_pol.append(host)
    return src_pol


def print_policy():
    opts = ""
    for k, v in csp_headers.items():
        if csp_headers[k]:
            opts = opts + k + ' '
            opts = opts + ' '.join(csp_headers[k])
            opts = opts + '; '
    print("\nPlease review the CSP header before using it on production systems\n")
    print("Content-Security-Policy: %s\n" % opts)
    print("\nTo test your CSP without deploying it use:\n")
    print("Content-Security-Policy-Report-Only: %s\n" % opts)
    print("\nFor more information, visit http://content-security-policy.com/\n")
    return


def policy_from_crawl(prof):
    conf = {}
    conf['scripts'] = {}
    opts = []
    hosts = []

    if not prof['js_sources'] and not prof['inline']:
        conf['scripts']['allow'] = 'none'
        return conf
    if prof['js_sources']:
        conf['scripts']['allow'] = 'custom'
        for source in prof['js_sources']:
            if source == 'HOME':
                opts.append('self')
            else:
                hosts.append(source)
    if prof['inline']:
        opts.append('inline')
    conf['scripts']['options'] = opts
    conf['scripts']['hosts'] = hosts

    return toml.dumps(conf)

def write_toml(f_out, conf):
    with open(f_out,'w+') as outfile:
        outfile.write(conf)
    return

# has_all_none checks if 'allow' key has value 'all' or 'none'
def _has_all_none(conf):
    if len(conf) > 1 and conf['allow'] == 'none' or conf['allow'] == 'all':
        return True
    else:
        return False


# translates CSPgen keyword to a corresponding CSP value
def _translate_keyword(val):
    if val == 'inline':
        return "'unsafe-inline'"
    elif val == 'eval':
        return "'unsafe-eval'"
    elif val == 'self':
        return "'self'"
    elif val == 'data':
        return "data:"
    else:
        logging.warning("Unknown option: %s", val)
        return


def add_policy(key, pol):
    if key == 'default':
        csp_headers['default-src'] = pol
    elif key == 'scripts':
        csp_headers['script-src'] = pol
    elif key == 'frame':
        csp_headers['child-src'] = pol
    elif key == 'connect':
        csp_headers['connect-src'] = pol
    else:
        logging.warning("policy cannot be added for resource: %s", key)
    return
