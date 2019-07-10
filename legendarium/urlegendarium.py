# coding: utf-8

import re


class URLegendarium(object):

    def __init__(self, acron='', year_pub='', volume='', number='',
                 fpage='', fpage_sequence='', lpage='', article_id='',
                 suppl_number='', doi='', order=''):

        self.acron = str(acron).strip() if acron else ''
        self.year_pub = str(year_pub).strip() if year_pub else ''
        self.volume = str(volume).strip() if volume else ''
        self.number = str(number).strip() if number else ''
        self.suppl_number = str(suppl_number).strip() if suppl_number else ''
        self.fpage = str(fpage).strip() if fpage else ''
        self.fpage_sequence = str(fpage_sequence).strip() if fpage_sequence else ''
        self.lpage = str(lpage).strip() if lpage else ''
        self.article_id = str(article_id).strip() if article_id else ''
        self.doi = str(doi).strip() if doi else ''
        self.order = str(order).strip() if order else ''

    def __unicode__(self):
        return self.url_article

    def __str__(self):
        return self.url_article

    def __repr__(self):
        return self.url_article

    def _get_numbers(self, text):
        """
        Get just numbers in a text.
        """
        if text:
            return re.sub("[^0-9]", "", text)
        else:
            return ''

    def _clean_year_pub(self):
        """
        Clean the year removing all caracter and keep just 4/1 numbers.
        """
        if self.year_pub:
            year = self._get_numbers(self.year_pub)
            if len(year) == 4:
                return '{0}'.format(year[:4])
            else:
                raise ValueError(u'Probably not a valid year')
        else:
            return u''

    def _clean_volume(self):
        """
        Clean the volume stripped the beginning and the end of the string.
        """
        if self.volume:
            return self.volume.strip()
        else:
            return ''

    def _clean_number(self):
        """
        Clean the number stripped the beginning and the end of the string.
        """
        if self.number:
            return self.number.strip()
        else:
            return ''

    def _clean_acron(self):
        """
        Clean the title stripped the beginning and the end of the string.
        """
        return self.acron.strip()

    def _clean_suppl_number(self):
        """
        Clean the supplement number stripped the beginning and the end of the string.
        """
        if self.suppl_number:
            return self.suppl_number.strip()
        else:
            return ''

    def get_journal_seg(self):
        """
        Method to build the journal URL.
        """
        if self.acron:
            title = self._clean_acron()
        else:
            raise ValueError(u'The journal is mandatory to mount the URL')

        return u'{0}'.format(title)

    def get_issue_seg(self):
        """
        Method to build the issue.
        """
        year = self._clean_year_pub()
        volume = self._clean_volume()
        number = self._clean_number()
        suppl = self._clean_suppl_number()

        if suppl:
            suppl = u'suppl{0}'.format(suppl)

        if number:
            number = u'n{0}'.format(number)

        if volume:
            volume = u'v{0}'.format(volume)

        if year:
            year = u'{0}'.format(year)

        if year or volume or number or suppl:
            # We give preference to number
            return u'{0}.{1}{2}{3}'.format(year, volume, number, suppl)
        else:
            raise ValueError(u'Year or Volume or Year must exists to form URL Issue Segment')

    def get_article_seg(self):
        """
        Method to build the article.
        """
        article = u''

        if self.article_id:
            article = self.article_id
        elif self.fpage and self.lpage:
            if self.fpage_sequence:
                article = u'{0}_{1}-{2}'.format(self.fpage, self.fpage_sequence, self.lpage)
            else:
                article = u'{0}-{1}'.format(self.fpage, self.lpage)
        elif self.fpage:
            if self.fpage_sequence:
                article = u'{0}_{1}'.format(self.fpage, self.fpage_sequence)
            else:
                article = self.fpage
        elif self.lpage:
            article = self.lpage
        elif self.doi:
            article = self.doi
        elif self.order:
            article = u'o{0}'.format(self.order)
        else:
            return article

        return article

    @property
    def url_journal(self):
        """
        Print the url follow the basic definition:

            REVISTA/
        """
        args = [self.get_journal_seg()]

        return u'{0}/'.format(*args)

    @property
    def url_issue(self):
        """
        Print the url follow the basic definition:

            REVISTA/nVOLUMEvNUMBER
        """
        args = [self.get_journal_seg(), self.get_issue_seg()]

        return u'{0}/{1}'.format(*args)

    @property
    def url_article(self):
        """
        Print the url follow the basic definition:

            REVISTA/nVOLUMEvNUMBER/e1928639
        """
        args = [self.get_journal_seg(), self.get_issue_seg(), self.get_article_seg()]

        return u'{0}/{1}/{2}'.format(*args)
