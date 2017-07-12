# coding: utf-8
import re
import locale

from datetime import datetime

from legendarium.utils import translations

NUMBERS = re.compile(r"[^0-9]")
FORMAT_PREFIX = re.compile(r"%.")
SPACES = re.compile(r" +")


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
                raise ValueError(u'Probably not a valid date')


class CitationFormatter:

    def __init__(self, title='', short_title='', pubdate='', volume='', number='',
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

        self._title = title.strip() if title else ''
        self._short_title = short_title.strip() if short_title else ''
        self._pubdate = parse_date(pubdate)
        self._volume = str(volume).strip() if volume else ''
        self._number = str(number).strip() if number else ''
        self._suppl = str(suppl).strip() if suppl else ''
        self._fpage = str(fpage).strip() if fpage else ''
        self._lpage = str(lpage).strip() if lpage else ''
        self._elocation = str(elocation).strip() if elocation else ''

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
    def descriptive_dmy_date(self):

        if len(self._pubdate) == 10:
            dt = datetime.strptime(self._pubdate, '%Y-%m-%d')
            dt = dt.strftime('%d %b %Y').upper()

        if len(self._pubdate) == 7:
            dt = datetime.strptime(self._pubdate, '%Y-%m')
            dt = dt.strftime('%b %Y').upper()

        if len(self._pubdate) == 4:
            dt = self._pubdate

        return dt

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

        if self._suppl == '0':
            return ''

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
            '%D': self.descriptive_dmy_date,
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

        return fmt_spec.strip()


def very_short_format(pubdate='', volume='', number='', suppl='', language='en'):
    """
    Return a very short version of a bibliografic legend, according to the given
    parameters. Normaly used to identify the Issue Label.

    Keyword arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return: (string)
    67(9) suppl. 3 - 2011
    """

    template = ['%Y,']

    vn = ''
    if volume:
        vn += '%v'

    if number:
        vn += '(%n)'

    template.append(vn)

    if suppl:
        template.append(translations['suppl'][language]+'. %s')

    output = CitationFormatter(
        title='',
        short_title='',
        pubdate=pubdate,
        volume=volume,
        number=number,
        fpage='',
        lpage='',
        elocation='',
        suppl=suppl
    )

    return output.format(' '.join(template))


def short_format(title='', short_title='', pubdate='', volume='', number='', suppl=''):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    Keyword arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return (string) Rev.Mal-Estar Subj, 2011 67(9) suppl. 3
    """

    template = ['%t, %Y']

    vn = ''
    if volume:
        vn += '%v'

    if number:
        vn += '(%n)'

    template.append(vn)

    if suppl:
        template.append('suppl %s')

    output = CitationFormatter(
        title=title,
        short_title=short_title,
        pubdate=pubdate,
        volume=volume,
        number=number,
        fpage='',
        lpage='',
        elocation='',
        suppl=suppl
    )

    return output.format(' '.join(template))


def descriptive_format(title='', short_title='', pubdate='', volume='', number='', fpage='', lpage='', elocation='', suppl='', language='en'):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    Keyword arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return: (string)
    Revista Mal-Estar Subjetivo, 2011, volume: 67, number: 9, supplement: 3, pages: 154-200
    """

    template = ['%T']

    if volume:
        template.append(translations['volume'][language]+': %v')

    if number:
        template.append(translations['issue'][language]+': %n')

    if suppl:
        if suppl == '0':
            template[-1] += ' '+translations['supplement'][language]
        else:
            template[-1] += ' '+translations['supplement'][language]+' %s'

    if fpage or lpage:
        template.append(translations['pages'][language]+': %p')

    if elocation:
        if (fpage or lpage):
            template.pop()
        template.append(translations['article number'][language]+': %e')

    template.append(translations['published'][language]+': %D')

    output = CitationFormatter(
        title=title,
        short_title=short_title,
        pubdate=pubdate,
        volume=volume,
        number=number,
        fpage=fpage,
        lpage=lpage,
        elocation=elocation,
        suppl=suppl
    )

    return output.format(', '.join(template))


def descriptive_html_format(title='', short_title='', pubdate='', volume='', number='', fpage='', lpage='', elocation='', suppl='', language='en'):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    Keyword arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification
    fpage -- document first page
    lpage -- document last page
    elocation -- document elocation id

    return:
    <div class="biblio_label">
      <span class="title">Revista Mal-Estar Subjetivo</span>
      <span class="year">2011</span>
      <span class="prefix volume">volume:</span>
      <span class="value volume">67</span>
      <span class="prefix number">number:</span>
      <span class="value number">9</span
      <span class="prefix supplement">supplement:</span>
      <span class="value supplement">3</span
      <span class="prefix pages">article number:</span>
      <span class="value pages">e00120416</span>
    </div>
    """

    template = []
    template.append('<div class="biblio_label">')
    template.append('<span class="title">%T</span>')

    if volume:
        template.append('<span class="prefix volume">'+translations['volume'][language]+':</span> <span class="value volume">%v</span>')

    if number:
        template.append('<span class="prefix number">'+translations['issue'][language]+':</span> <span class="value number">%n</span>')

    if suppl:
        template.append('<span class="prefix supplement">'+translations['supplement'][language]+'</span> <span class="value supplement">%s</span>')

    if fpage or lpage:
        template.append('<span class="prefix pages">'+translations['pages'][language]+':</span> <span class="value pages">%p</span>')

    if elocation:
        if (fpage or lpage):
            template.pop()
        template.append('<span class="prefix pages">'+translations['article number'][language]+':</span> <span class="value pages">%e</span>')

    template.append('<span class="prefix published">'+translations['published'][language]+':</span> <span class="value published">%D</span>')
    template.append('</div>')

    output = CitationFormatter(
        title=title,
        short_title=short_title,
        pubdate=pubdate,
        volume=volume,
        number=number,
        fpage=fpage,
        lpage=lpage,
        elocation=elocation,
        suppl=suppl
    )

    return output.format(''.join(template))


def descriptive_short_format(title='', short_title='', pubdate='', volume='', number='', suppl='', language='en'):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    Keyword arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return: (string)
    Revista Mal-Estar Subjetivo, 2011, Volume: 67, Number: 9, Supplement: 3
    """

    template = ['%T']

    if volume:
        template.append(translations['volume'][language]+': %v')

    if number:
        template.append(translations['issue'][language]+': %n')

    if suppl:
        if suppl == '0':
            template[-1] += ' '+translations['supplement'][language]
        else:
            template[-1] += ' '+translations['supplement'][language]+' %s'

    template.append(translations['published'][language]+': %D')

    output = CitationFormatter(
        title=title,
        short_title=short_title,
        pubdate=pubdate,
        volume=volume,
        number=number,
        fpage='',
        lpage='',
        elocation='',
        suppl=suppl
    )

    return output.format(', '.join(template))


def descriptive_html_short_format(title='', short_title='', pubdate='', volume='', number='', suppl='', language='en'):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    Keyword arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return:
    <div class="biblio_label">
      <span class="title">Revista Mal-Estar Subjetivo</span>
      <span class="year">2011</span>
      <span class="prefix volume">volume:</span>
      <span class="value volume">67</span>
      <span class="prefix number">number:</span>
      <span class="value number">9</span
      <span class="prefix supplement">supplement:</span>
      <span class="value supplement">3</span
    </div>
    """

    template = []
    template.append('<div class="biblio_label">')
    template.append('<span class="title">%T</span>')

    if volume:
        template.append('<span class="prefix volume">'+translations['volume'][language]+':</span> <span class="value volume">%v</span>')

    if number:
        template.append('<span class="prefix number">'+translations['issue'][language]+':</span> <span class="value number">%n</span>')

    if suppl:
        template.append('<span class="prefix supplement">'+translations['supplement'][language]+'</span> <span class="value supplement">%s</span>')
    template.append('<span class="prefix published">'+translations['published'][language]+':</span> <span class="value published">%D</span>')
    template.append('</div>')

    output = CitationFormatter(
        title=title,
        short_title=short_title,
        pubdate=pubdate,
        volume=volume,
        number=number,
        fpage='',
        lpage='',
        elocation='',
        suppl=suppl
    )

    return output.format(''.join(template))


def descriptive_very_short_format(pubdate='', volume='', number='', suppl='', language='en'):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    Keyword arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return: (string)
    2011, Volume: 67, Number: 9, Supplement: 3
    """

    template = ['%Y']

    if volume:
        template.append(translations['volume'][language]+': %v')

    if number:
        template.append(translations['issue'][language]+': %n')

    if suppl:
        if suppl == '0':
            template[-1] += ' '+translations['supplement'][language]
        else:
            template[-1] += ' '+translations['supplement'][language]+' %s'

    output = CitationFormatter(
        title='',
        short_title='',
        pubdate=pubdate,
        volume=volume,
        number=number,
        fpage='',
        lpage='',
        elocation='',
        suppl=suppl
    )

    return output.format(', '.join(template))


def descriptive_html_very_short_format(pubdate='', volume='', number='', suppl='', language='en'):
    """
    Return a short version of a bibliografic legend, according to the given
    parameters.

    Keyword arguments:
    title -- Full version of the journal title
    short_title -- short version of the journal title
    pubdata -- a valid ISO date YYYY-MM-DD (no hour, minutes and seconds accepted)
    volume -- issue volume
    number -- issue number
    suppl -- supplement identification

    return:
    <div class="biblio_label">
      <span class="title">Revista Mal-Estar Subjetivo</span>
      <span class="year">2011</span>
      <span class="prefix volume">volume:</span>
      <span class="value volume">67</span>
      <span class="prefix number">number:</span>
      <span class="value number">9</span
      <span class="prefix supplement">supplement:</span>
      <span class="value supplement">3</span
    </div>
    """

    template = []
    template.append('<div class="biblio_label">')
    template.append('<span class="year">%Y</span>')
    if volume:
        template.append('<span class="prefix volume">'+translations['volume'][language]+':</span> <span class="value volume">%v</span>')

    if number:
        template.append('<span class="prefix number">'+translations['issue'][language]+':</span> <span class="value number">%n</span>')

    if suppl:
        template.append('<span class="prefix supplement">'+translations['supplement'][language]+'</span> <span class="value supplement">%s</span>')

    template.append('</div>')

    output = CitationFormatter(
        title='',
        short_title='',
        pubdate=pubdate,
        volume=volume,
        number=number,
        fpage='',
        lpage='',
        elocation='',
        suppl=suppl
    )

    return output.format(''.join(template))
