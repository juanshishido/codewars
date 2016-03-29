import re


def strip_comments(string, markers):
    lines = string.split('\n')
    markers = ''.join(markers)
    comments = []
    for line in lines:
        matches = re.findall(r'['+markers+']', line)
        if matches:
            comment = line.split(matches[0])[0].strip()
            comments.append(comment)
        else:
            comments.append(line.strip())
    return '\n'.join(comments)
