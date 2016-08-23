# coding: utf-8

from __future__ import print_function

import re


class Legendarium(object):

    def __init__(self, acron_title='', year_pub='', volume='', number='',
                 fpage='', lpage='', article_id=''):

        self.acron_title = acron_title
        self.year_pub = str(year_pub)
        self.volume = volume
        self.number = number
        self.fpage = fpage
        self.lpage = lpage
        self.article_id = article_id

    def __unicode__(self):
        return self.stamp

    def __str__(self):
        return self.stamp

    def __repr__(self):
        return self.stamp

    def _get_numbers(self, text):
        """
        Get just numbers in a text.
        """
        return re.sub("[^0-9]", "", text)

    def _clean_year_pub(self):
        """
        Clean the year removing all caracter and keep just 4/1 numbers.
        """
        if self.year_pub:
            return ' {0}'.format(self._get_numbers(self.year_pub)[:4])
        else:
            return ''

    def _clean_volume(self):
        """
        Clean the volume removing all caracter and keep just numbers.
        """
        return self._get_numbers(self.volume)

    def _clean_number(self):
        """
        Clean the number stripped the beginning and the end of the string.
        """
        return self.number.strip()

    def _clean_acron_title(self):
        """
        Clean the title stripped the beginning and the end of the string.
        """
        return self.acron_title.strip()

    def get_journal(self):
        """
        Method to build the journal, it can have ``year_pub`` or not.
        """
        if self.acron_title:
            title = self._clean_acron_title()
        else:
            raise ValueError('The journal is mandatory to mount the bibliographic legend')

        year_pub = self._clean_year_pub()

        return '{0}{1}'.format(title, year_pub)

    def get_issue(self):
        """
        Method to build the issue, it can use a suffix separator or not.
        """
        volume = self._clean_volume()
        number = self._clean_number()

        if number:
            number = '({0})'.format(number)

        if volume or number:
            return '{0}{1}{2}'.format(';', volume, number)
        else:
            return ''

    def get_article(self):
        """
        Method to build the article, it can use a suffix separator or not.
        """
        article = ''

        if self.fpage and self.lpage:
            article = '{0}-{1}'.format(self.fpage, self.lpage)
        elif self.fpage:
            article = self.fpage
        elif self.lpage:
            article = self.lpage
        elif self.article_id:
            article = self.article_id
        else:
            return article

        return '{0}{1}'.format(':', article)

    @property
    def stamp(self):
        """
        Print the legend follow the basic definition:

            REVISTA ANO;VOLUME(NUMBER):ID_ARTICLE
        """
        args = [self.get_journal(), self.get_issue(), self.get_article()]

        return '{0}{1}{2}'.format(*args)


if __name__ == '__main__':

    kwargs = {'volume': 'v19', 'acron_title': 'Revista X', 'year_pub': 2016,
              'article_id': '019278765', 'number': '7', 'fpage': "123",
              'lpage': "987"}

    legend = Legendarium(**kwargs)

    print("Teste com todos os params")
    print(legend.stamp + "\n")

    ############################################################################
    kwargs = {'volume': 'v19', 'acron_title': 'Revista X',
              'article_id': '019278765', 'number': '7'}

    legend = Legendarium(**kwargs)

    print("Teste sem o param year_pub")
    print(legend.stamp + "\n")

    ############################################################################

    kwargs = {'acron_title': 'Revista X', 'year_pub': 2016,
              'article_id': '019278765', 'number': '7'}

    legend = Legendarium(**kwargs)

    print("Teste sem o param volume")
    print(legend.stamp + "\n")

    ############################################################################

    kwargs = {'volume': 'v19', 'acron_title': 'Revista X', 'year_pub': 2016,
              'article_id': '019278765'}

    legend = Legendarium(**kwargs)

    print("Teste sem o param number")
    print(legend.stamp + "\n")

    ############################################################################

    kwargs = {'acron_title': 'Revista X', 'year_pub': 2016,
              'article_id': '019278765'}

    legend = Legendarium(**kwargs)

    print("Teste sem o param volume e number")
    print(legend.stamp + "\n")

    ###########################################################################

    kwargs = {'volume': 'v19', 'acron_title': 'Revista X', 'year_pub': 2016,
              'number': '7'}

    legend = Legendarium(**kwargs)

    print("Teste sem o param artigo")
    print(legend.stamp + "\n")

    ############################################################################

    kwargs = {'acron_title': 'Revista X', 'year_pub': 2016}

    legend = Legendarium(**kwargs)

    print("Teste somente o acron_title e year_pub")
    print(legend.stamp + "\n")

    ############################################################################

    kwargs = {'volume': 'v19', 'year_pub': 2016, 'article_id': '019278765',
              'number': '7'}

    legend = Legendarium(**kwargs)

    print("Teste sem o param acron_title")
    print(legend.stamp + "\n")

    ############################################################################
