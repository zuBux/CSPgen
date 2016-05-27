# CSPgen
CSPgen is a Content Security Policy ([more](http://content-security-policy.com/)) generator written in Python. It uses [TOML](https://github.com/toml-lang/toml) configuration files as input and generates ready-to-use CSP headers. Additionally, CSPgen can parse a target URL and attempt to semi-automatically generate CSP headers (WIP).

# Usage

**CSPgen** has two functionalities:

## CSP conf from URL crawling

`python cspgen.py -u <URL> -o <toml>`

When passing a `URL` as input, CSPgen will attempt to make a request, parse the HTML and look for dynamic resources such as *JS*, *CSS*, image files, Flash objects etc. (currently **only JS has been implemented**). It will then create a configuration file, using the `-o` option, using TOML language. The configuration file can be used to generate Content Security Policy headers (see below)

## CSP headers from TOML conf

`python cspgen.py <file>`

CSPgen reads a TOML configuration file and attempts to create ready-to-use Content Security Policy headers.

# Disclaimer

**CSPgen is currently under heavy development** and is not reliable for production use. Use with caution and always manually review output.
