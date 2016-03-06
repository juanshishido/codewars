import re


def autocorrect(input):
    you = re.compile('(\\bu\\b)|\\b(yo[u]+)\\b', re.IGNORECASE)
    return you.sub('your sister', input)
