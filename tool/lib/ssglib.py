import json
import os
import urllib.request
from collections import OrderedDict


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


def get_jsonld(dict_list):
    jsonld = '<script type="application/ld+json">\n'
    jsonld += '['
    jsonld += ',\n'.join([json.dumps(d, indent=4, ensure_ascii=False) for d in dict_list])
    jsonld += ']\n'
    jsonld += '</script>'
    return jsonld


def get_article_jsonld_dict(title='', date_published='', date_modified='', description=''):
    jsonld_dict = OrderedDict()
    jsonld_dict['@context'] = 'http://schema.org'
    jsonld_dict['@type'] = 'Article'
    if title:
        jsonld_dict['headline'] = title
    if date_published:
        jsonld_dict['datePublished'] = date_published
    if date_modified:
        jsonld_dict['dateModified'] = date_modified
    if description:
        jsonld_dict['description'] = description
    return jsonld_dict


def get_breadcrumb_jsonld_dict(urls, names):
    items = []
    for i, (url, name) in enumerate(zip(urls, names)):
        item = OrderedDict()
        item['@type'] = 'ListItem'
        item['position'] = i + 1
        item['item'] = {'@id': 'https:' + url, 'name': name}
        items.append(item)
    jsonld_dict = OrderedDict()
    jsonld_dict['@context'] = 'http://schema.org'
    jsonld_dict['@type'] = 'BreadcrumbList'
    jsonld_dict['itemListElement'] = items
    return jsonld_dict


def get_breadcrumb_list(urls, names, last_name=''):
    base = '''<ol id="breadcrumb">
    {}
</ol>'''

    item = '<li><a href="{}">{}</a></li>'
    items = []
    for url, name in zip(urls, names):
        items.append(item.format(url, name))
    if last_name:
        items.append('<li>{}</li>'.format(last_name))
    return base.format('\n'.join(items))
