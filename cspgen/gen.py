import logging

csp_headers = {}


def gen_scripts_pol(conf):
    src_pol = []
    try:
        allow = conf['allow']
    except KeyError:
        logging.error("no script-src policies could be defined")

    if _has_all_none(conf):
        logging.warning("'%s' option detected, all other script options\
        will be ignored", allow)
        src_pol.append(_gen_src_policy(allow))
        csp_headers['script-src'] = src_pol
        return csp_headers
    else:
        for option in conf['options']:
            src_pol.append(_gen_src_policy(option))
    if 'hosts' in conf:
        for host in conf['hosts']:
            src_pol.append(host)
    csp_headers['script-src'] = src_pol
    return csp_headers


# has_all_none checks if 'allow' key has value 'all' or 'none'
def _has_all_none(conf):
    if len(conf) > 1 and conf['allow'] == 'none' or conf['allow'] == 'all':
        return True
    else:
        return False


# translates CSPgen keyword to a corresponding CSP value
def _gen_src_policy(val):
    if val == 'none':
        return "'none'"
    elif val == 'all':
        return "*"
    elif val == 'inline':
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


def print_policy():
    opts = ' '.join(csp_headers['script-src'])
    print "Content-Security-Policy: %s" % opts
    return
