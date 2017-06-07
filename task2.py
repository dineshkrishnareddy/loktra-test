__author__ = 'dinesh'

# TASK
# ------------------------------------------------------------------------------------------------------------------
# In Python, write a class or module with a bunch of functions for manipulating a URI. For this exercise, pretend that
# the urllib, urllib2, and urlparse modules don't exist. You can use other standard Python modules, such as re, for this.
# The focus of the class or module you write should be around usage on the web, so you'll want to have things that make
# it easier to update or append a querystring var, get the scheme for a URI, etc., and you may want to include ways to
# figure out the domain for a URL (british-site.co.uk, us-site.com, mailto: yourname@example.com, etc.)
#
# We're looking for correctness (you'll probably want to read the relevant RFCs; make sure you handle edge cases),
# and elegance of your API (does it let you do the things you commonly want to do with URIs in a really straightforward
# way?,) as well as coding style. If you don't know Python already, then this is also an exercise in learning new things
# quickly and well. Your code should be well-commented and documented and conform to the guidelines in the PEP 8 Style
# Guide for Python Code. Include some instructions and examples of usage in your documentation. You may also want to
# write unit tests.


# function to get domain from a uri 
def split_domain(uri, start=0):
    delimiterPosition = len(uri)
    for c in '/?#':
        currentDelimiterPosition = uri.find(c, start)
        if currentDelimiterPosition >= 0:
            delimiterPosition = min(delimiterPosition, currentDelimiterPosition)
    return uri[start:delimiterPosition], uri[delimiterPosition:]


# function to split uri 
def split_uri(uri):
    scheme = ''
    username = password = port = domain = query = fragment = ''
    i = uri.find('://')
    if i > 0:
        scheme, uri = uri[:i].lower(), uri[i+1:]
    if uri[:2] == '//':
        domain, uri = split_domain(uri, 2)
    if '@' in domain:
        username, domain = domain.split('@', 1)
        if ':' in username:
            username, password = username.split(':', 1)
        if ':' in domain:
            domain, port = domain.split(':', 1)
    if '#' in uri:
        uri, fragment = uri.split('#', 1)
    if '?' in uri:
        uri, query = uri.split('?', 1)
    return scheme, username, password, domain, port, uri, query, fragment


# main function to decode uri
def uri_decoder(uri):
    scheme, username, password, domain, port, uri, query, fragment = split_uri(uri)
    return scheme, username, password, domain, port, uri, query, fragment

