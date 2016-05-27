# CSPgen
CSPgen is a Content Security Policy ([link](http://content-security-policy.com/)) generator written in Python. It uses [TOML](https://github.com/toml-lang/toml) profiles as input and generates ready-to-use CSP headers. Additionally, CSPgen can parse a target URL and attempt to semi-automatically generate CSP profiles and headers (WIP).

# Usage

**CSPgen** has two functionalities:

- Generates Content Security Policy headers from a TOML profile
- Crawls a URL and attempts to automatically generate a Content Security Policy

## CSP from URL crawling

`python cspgen.py -u <URL> -o <toml>`

## CSP from TOML profile

`python cspgen.py <file>`
