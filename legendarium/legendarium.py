# coding: utf-8

import re
from datetime import datetime

from legendarium.utils import translations

NUMBERS = re.compile(r"[^0-9]")
FORMAT_PREFIX = re.compile(r"%.")


def get_numbers(value):
    """
    Get just numbers in a text.
    """
    if not value:
        return ''

    return NUMBERS.sub("", value)


def parse_date(value):

    try:
        dt = datetime.strptime(value, '%Y-%m-%d')
        return dt.isoformat()[:10]
    except:
        try:
            dt = datetime.strptime(value, '%Y-%m')
            return dt.isoformat()[:7]
        except:
            try:
                dt = datetime.strptime(value, '%Y')
                return dt.isoformat()[:4]
            except:
                raise ValueError(u'Probably not a valid year')


class Legendarium:

    def __init__(self, title, short_title, pubdate, volume='', number='',
                 fpage='', lpage='', elocation='', suppl=''):

        """
        Create a instance of Legendarium

        arguments:
        title -- Full version of the journal title
        short_title -- short version of the journal title
        pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)

        Keyword arguments:
        volume -- issue volume
        number -- issue number
        suppl -- supplement identification
        """

        self._title = title.strip()
        self._short_title = short_title.strip()
        self._pubdate = parse_date(pubdate)
        self._volume = volume.strip() or ''
        self._number = number.strip() or ''
        self._suppl = suppl.strip() or ''
        self._fpage = fpage.strip() or ''
        self._lpage = lpage.strip() or ''
        self._elocation = elocation.strip() or ''

    def __repr__(self):
        return "%s.%s(%s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
            self.__class__.__module__,
            self.__class__.__qualname__,
            self._title,
            self._short_title,
            self._pubdate,
            self._volume,
            self._number,
            self._suppl,
            self._fpage,
            self._lpage,
            self._elocation
        )

    @property
    def title(self):

        return self._title

    @property
    def short_title(self):

        return self._short_title

    @property
    def yearpubdata(self):

        return self._pubdate[0:4]

    @property
    def pubdate(self):

        return self._pubdate

    @property
    def volume(self):

        return self._volume

    @property
    def number(self):

        return self._number

    @property
    def suppl(self):

        return self._suppl

    def issue(self):
        """
        This function returns a string with a short version of the issue identification

        Example 1:
            self.volume: 10
            self.number: 12
            return 10(12)

        Example 2:
            self.volume: 10
            return 10

        Example 3:
            self.number: 12
            return (12)

        Example 4:
            self.volume: 10
            self.number: 12
            self.suppl: 1
            return 10(12) suppl. 1

        """

    @property
    def fpage(self):

        return self._fpage

    @property
    def lpage(self):

        return self._lpage

    @property
    def pages(self):

        pages = [i for i in sorted([self.fpage, self.lpage]) if i]

        if pages:
            return "-".join(pages)

        if self.elocation:
            return self.elocation

        return ''

    @property
    def elocation(self):

        return self._elocation

    @property
    def rawformat(self):

        data = (
            self._title,
            self._short_title,
            self._pubdate,
            self._volume,
            self._number,
            self._suppl,
            self._fpage,
            self._lpage,
            self._elocation
        )

        return ', '.join([i for i in data if i])

    def format(self, fmt_spec=''):

        return self.__format__(fmt_spec)

    def __format__(self, fmt_spec=''):

        FORMAT_PATTERNS = {
            '%T': self.title,
            '%t': self.short_title,
            '%Y': self.yearpubdata,
            '%v': self.volume,
            '%n': self.number,
            '%s': self.suppl,
            '%f': self.fpage,
            '%l': self.lpage,
            '%p': self.pages,
            '%e': self.elocation,
            '%d': self.pubdate
        }

        itens = FORMAT_PREFIX.findall(fmt_spec)

        for item in itens:
            if item in FORMAT_PATTERNS:
                fmt_spec = fmt_spec.replace(item, FORMAT_PATTERNS[item])
            else:
                raise ValueError('Pattern %s not found in %s' % [item, str([i for i in FORMAT_PATTERNS])])

        return fmt_spec


def short_format(title, short_title, pubdate, volume='', number='', suppl=''):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)

    Keyword arguments:
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return (string) Rev.Mal-Estar Subj, 2011 67(9) suppl. 3
    """

    template = ['%t, %Y %v(%n)']

    if suppl:
        template.append('suppl. %s')

    output = Legendarium(title, short_title, pubdate, volume=volume, number=number, fpage='', lpage='', elocation='', suppl=suppl)

    return output.format(' '.join(template))


def descriptive_format(title, short_title, pubdate, volume='', number='', fpage='', lpage='', elocation='', suppl='', language='en'):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)

    Keyword arguments:
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return (string) Rev.Mal-Estar Subj, 2011 67(9) suppl. 3
    """

    template = ['%T, %Y']

    if volume:
        template.append(translations['volume'][language]+': %v')

    if number:
        template.append(translations['number'][language]+': %n')

    if suppl:
        template.append(translations['supplement'][language]+': %s')

    if fpage or lpage:
        template.append(translations['pages'][language]+': %p')

    if elocation:
        template.pop()
        template.append(translations['article number'][language]+': %e')

    output = Legendarium(
        title, short_title, pubdate, volume, number, fpage, lpage, elocation, suppl
    )

    return output.format(', '.join(template))


def descriptive_html_format(title, short_title, pubdate, volume='', number='', fpage='', lpage='', elocation='', suppl='', language='en'):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)

    Keyword arguments:
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return (string) Rev.Mal-Estar Subj, 2011 67(9) suppl. 3
    """
    template = []
    template.append('<div class="biblio_label">')
    template.append('<span class="title">%T</span>')
    template.append('<span class="year">%Y</span>')

    if volume:
        template.append('<span class="prefix volume">'+translations['volume'][language]+':</span> <span class="value volume">%v</span>')

    if number:
        template.append('<span class="prefix number">'+translations['number'][language]+':</span> <span class="value number">%n</span>')

    if suppl:
        template.append('<span class="prefix supplement">'+translations['supplement'][language]+':</span> <span class="value supplement">%s</span>')

    if fpage or lpage:
        template.append('<span class="prefix pages">'+translations['pages'][language]+':</span> <span class="value pages">%p</span>')

    if elocation:
        template.pop()
        template.append('<span class="prefix pages">'+translations['article number'][language]+':</span> <span class="value pages">%e</span>')

    template.append('</div>')

    output = Legendarium(
        title, short_title, pubdate, volume, number, fpage, lpage, elocation, suppl
    )

    return output.format(''.join(template))
