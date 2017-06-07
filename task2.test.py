__author__ = 'dinesh'

from task2 import uri_decoder


print uri_decoder("//user:password@example.org:8000/absolute/URI/with/absolute/path/to/resource.txt?queray1=value1&query2=value2#abc") == \
      ('', 'user', 'password', 'example.org', '8000', '/absolute/URI/with/absolute/path/to/resource.txt', 'queray1=value1&query2=value2', 'abc')
print uri_decoder("https://example.co.org/absolute/URI/with/absolute/path/to/resource.txt") == \
      ('https', '', '', 'example.co.org', '', '/absolute/URI/with/absolute/path/to/resource.txt', '', '')
print uri_decoder("https://example.org/absolute/URI/with/absolute/path/to/resource") == \
      ('https', '', '', 'example.org', '', '/absolute/URI/with/absolute/path/to/resource', '', '')
print uri_decoder("ftp://example.org/resource.txt") == \
      ('ftp', '', '', 'example.org', '', '/resource.txt', '', '')
print uri_decoder("abc://example.com#abc") == \
      ('abc', '', '', 'example.com', '', '', '', 'abc')
print uri_decoder("abc://example.com?queray1=value1&query2=value2") == \
      ('abc', '', '', 'example.com', '', '', 'queray1=value1&query2=value2', '')
print uri_decoder("") == \
      ('', '', '', '', '', '', '', '')
print uri_decoder("abc://dinesh:dinesh@example.com?queray1=value1&query2=value2") == \
      ('abc', 'dinesh', 'dinesh', 'example.com', '', '', 'queray1=value1&query2=value2', '')
print uri_decoder("abc://dinesh@example.com?queray1=value1&query2=value2") == \
      ('abc', 'dinesh', '', 'example.com', '', '', 'queray1=value1&query2=value2', '')
print uri_decoder("http://www.example.com") == \
      ('http', '', '', 'www.example.com', '', '', '', '')