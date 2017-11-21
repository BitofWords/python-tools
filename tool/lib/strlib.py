import unicodedata


def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count


def trim_text_with_east_asian_width_count(text, max_count):
    count = 0
    for i, c in enumerate(text):
        if unicodedata.east_asian_width(c) in ['F', 'W', 'A']:
            count += 2
        elif unicodedata.east_asian_width(c) in ['H', 'Na', 'N']:
            count += 1
        if count > max_count:
            return text[:i]
    return text
