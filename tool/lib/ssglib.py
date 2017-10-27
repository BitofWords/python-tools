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


def make_breadcrumb_jsonld(urls, names):
    base = '''<script type="application/ld+json">
{{
    "@context": "http://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement":
    [
        {}
    ]
}}
</script>'''

    item = '''{{
            "@type": "ListItem",
            "position": {},
            "item":
            {{
            "@id": "https:{}",
            "name": "{}"
            }}
        }}'''

    items = []
    for i, (url, name) in enumerate(zip(urls, names)):
        items.append(item.format(i + 1, url, name))
    return base.format(',\n'.join(items))


def make_breadcrumb_list(urls, names, last_name=''):
    base = '''<ol class="breadcrumb">
    {}
</ol>'''

    item = '<li><a href="{}">{}</a></li>'
    items = []
    for url, name in zip(urls, names):
        items.append(item.format(url, name))
    if last_name:
        items.append('<li>{}</li>'.format(last_name))
    return base.format('\n'.join(items))
