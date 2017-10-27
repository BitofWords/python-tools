import os
import urllib.request


def get_content(url, decode='utf-8'):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode(decode)
        return content


def get_raw_url(url):
    url = url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
    return url


def ghcode(url, start=1, end=0):
    raw_url = get_raw_url(url)
    lines = get_content(raw_url).splitlines()

    if end == 0:
        end = len(lines)
    end = max(0, min(end, len(lines)))

    start -= 1
    start = max(0, min(start, end))

    sliced_lines = lines[start:end]

    ext = os.path.splitext(raw_url)[1]
    sliced_lines.insert(0, '``` ' + ext[1:])
    sliced_lines.append('```')

    return '\n'.join(sliced_lines)
