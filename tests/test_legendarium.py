# coding: utf-8
import unittest

from legendarium.formatter import (
    CitationFormatter,
    short_format,
    very_short_format,
    descriptive_format,
    descriptive_short_format,
    descriptive_very_short_format,
    descriptive_html_format,
    descriptive_html_short_format,
    descriptive_html_very_short_format,
    get_numbers
)


class TestLegendarium(unittest.TestCase):

    def setUp(self):
        self.sample = {
            'title': u'Revista Mal-Estar Subjetivo',
            'short_title': u'Rev.Mal-Estar Subj',
            'pubdate': u'2011',
            'volume': u'67',
            'number': u'9',
            'fpage': u'154',
            'lpage': u'200',
            'elocation': u'e00120416',
            'suppl': u'3'
        }

        self.legendarium = CitationFormatter(**self.sample)

    def test_descriptive_ymd_date_pt(self):

        import locale

        locale.setlocale(locale.LC_TIME, 'pt_BR')

        self.sample['pubdate'] = '2011-12-31'

        legendarium = CitationFormatter(**self.sample)

        self.assertEqual(
            '31 DEZ 2011',
            legendarium.descriptive_dmy_date
        )

    def test_descriptive_ymd_date_en(self):

        import locale

        locale.setlocale(locale.LC_TIME, 'en_US')

        self.sample['pubdate'] = '2011-12-31'

        legendarium = CitationFormatter(**self.sample)

        self.assertEqual(
            '31 DEC 2011',
            legendarium.descriptive_dmy_date
        )

    def test_descriptive_ymd_date_es(self):

        import locale

        locale.setlocale(locale.LC_TIME, 'es_ES')

        self.sample['pubdate'] = '2011-12-31'

        legendarium = CitationFormatter(**self.sample)

        self.assertEqual(
            '31 DIC 2011',
            legendarium.descriptive_dmy_date
        )

    def test_format(self):

        result = self.legendarium.format('%T, %Y, %v(%n), %p')

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, 2011, 67(9), 154-200',
            result
        )

    def test_very_short_format(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])
        del(self.sample['elocation'])
        result = very_short_format(**self.sample)

        self.assertEqual(
            '2011, 67(9) suppl. 3',
            result
        )

    def test_very_short_format_1(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])
        del(self.sample['elocation'])

        self.sample['suppl'] = ''

        result = very_short_format(**self.sample)

        self.assertEqual(
            '2011, 67(9)',
            result
        )

    def test_very_short_format_2(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])
        del(self.sample['elocation'])

        self.sample['suppl'] = ''

        result = very_short_format(**self.sample)

        self.assertEqual(
            '2011, 67(9)',
            result
        )

    def test_very_short_format_3(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])
        del(self.sample['elocation'])

        self.sample['suppl'] = ''
        self.sample['number'] = ''

        result = very_short_format(**self.sample)

        self.assertEqual(
            '2011, 67',
            result
        )

    def test_very_short_format_4(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])
        del(self.sample['elocation'])

        self.sample['number'] = ''

        result = very_short_format(**self.sample)

        self.assertEqual(
            '2011, 67 suppl. 3',
            result
        )

    def test_very_short_format_5(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])
        del(self.sample['elocation'])

        self.sample['volume'] = ''

        result = very_short_format(**self.sample)

        self.assertEqual(
            '2011, (9) suppl. 3',
            result
        )

    def test_very_short_format_6(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])
        del(self.sample['elocation'])

        self.sample['suppl'] = ''
        self.sample['volume'] = ''

        result = very_short_format(**self.sample)

        self.assertEqual(
            '2011, (9)',
            result
        )

    def test_short_format(self):

        data = dict(self.sample)
        del(data['fpage'])
        del(data['lpage'])
        del(data['elocation'])
        result = short_format(**data)

        self.assertEqual(
            'Rev.Mal-Estar Subj, 2011 67(9) suppl 3',
            result
        )

    def test_short_format_suppl_volume(self):

        data = {
            'title': 'Revista de Odontologia da Universidade de São Paulo',
            'short_title': 'Rev. Odontol. Univ. São Paulo',
            'pubdate': '1997',
            'volume': '11',
            'number': '',
            'suppl': '1'
        }

        result = short_format(**data)

        self.assertEqual(
            'Rev. Odontol. Univ. São Paulo, 1997 11 suppl 1',
            result

        )

    def test_short_format_suppl_number(self):

        data = {
            'title': 'Revista de Odontologia da Universidade de São Paulo',
            'short_title': 'Rev. Odontol. Univ. São Paulo',
            'pubdate': '1997',
            'volume': '11',
            'number': '21',
            'suppl': '1'
        }

        result = short_format(**data)

        self.assertEqual(
            'Rev. Odontol. Univ. São Paulo, 1997 11(21) suppl 1',
            result

        )

    def test_short_format_suppl_number_1(self):

        data = {
            'title': 'Revista de Odontologia da Universidade de São Paulo',
            'short_title': 'Rev. Odontol. Univ. São Paulo',
            'pubdate': '1997',
            'volume': '11',
            'number': '21',
            'suppl': '0'
        }

        result = short_format(**data)

        self.assertEqual(
            'Rev. Odontol. Univ. São Paulo, 1997 11(21) suppl',
            result

        )

    def test_short_format_suppl_volume_1(self):

        data = {
            'title': 'Revista de Odontologia da Universidade de São Paulo',
            'short_title': 'Rev. Odontol. Univ. São Paulo',
            'pubdate': '1997',
            'volume': '11',
            'number': '',
            'suppl': '0'
        }

        result = short_format(**data)

        self.assertEqual(
            'Rev. Odontol. Univ. São Paulo, 1997 11 suppl',
            result

        )

    def test_descriptive_format(self):

        result = descriptive_format(**self.sample)

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, Volume: 67, Issue: 9 Supplement 3, Article number: e00120416, Published: 2011',
            result
        )

    def test_descriptive_format_1(self):

        self.sample['elocation'] = ''

        result = descriptive_format(**self.sample)

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, Volume: 67, Issue: 9 Supplement 3, Pages: 154-200, Published: 2011',
            result
        )

    def test_descriptive_format_number_only(self):

        data = {
            'title': 'Cadernos Pagu ',
            'short_title': 'Cad. Pagu',
            'pubdate': '2017',
            'volume': '',
            'number': '50',
            'suppl': '',
            'fpage': '',
            'lpage': '',
            'elocation': 'e175002'
        }

        result = descriptive_format(**data)

        self.assertEqual(
            'Cadernos Pagu, Issue: 50, Article number: e175002, Published: 2017',
            result

        )

    def test_descriptive_format_suppl_number(self):

        data = {
            'title': 'Revista de Odontologia da Universidade de São Paulo',
            'short_title': 'Rev. Odontol. Univ. São Paulo',
            'pubdate': '1997',
            'volume': '11',
            'number': '21',
            'suppl': '1',
            'fpage': '121',
            'lpage': '143',
            'elocation': ''
        }

        result = descriptive_format(**data)

        self.assertEqual(
            'Revista de Odontologia da Universidade de São Paulo, Volume: 11, Issue: 21 Supplement 1, Pages: 121-143, Published: 1997',
            result

        )

    def test_descriptive_format_suppl_number_1(self):

        data = {
            'title': 'Revista de Odontologia da Universidade de São Paulo',
            'short_title': 'Rev. Odontol. Univ. São Paulo',
            'pubdate': '1997',
            'volume': '11',
            'number': '21',
            'suppl': '0',
            'fpage': '121',
            'lpage': '143',
            'elocation': ''
        }

        result = descriptive_format(**data)

        self.assertEqual(
            'Revista de Odontologia da Universidade de São Paulo, Volume: 11, Issue: 21 Supplement, Pages: 121-143, Published: 1997',
            result

        )

    def test_descriptive_format_suppl_volume(self):

        data = {
            'title': 'Revista de Odontologia da Universidade de São Paulo',
            'short_title': 'Rev. Odontol. Univ. São Paulo',
            'pubdate': '1997',
            'volume': '11',
            'number': '',
            'suppl': '1',
            'fpage': '121',
            'lpage': '143',
            'elocation': ''
        }

        result = descriptive_format(**data)

        self.assertEqual(
            'Revista de Odontologia da Universidade de São Paulo, Volume: 11 Supplement 1, Pages: 121-143, Published: 1997',
            result

        )

    def test_descriptive_format_suppl_volume_1(self):

        data = {
            'title': 'Revista de Odontologia da Universidade de São Paulo',
            'short_title': 'Rev. Odontol. Univ. São Paulo',
            'pubdate': '1997',
            'volume': '11',
            'number': '',
            'suppl': '0',
            'fpage': '121',
            'lpage': '143',
            'elocation': ''
        }

        result = descriptive_format(**data)

        self.assertEqual(
            'Revista de Odontologia da Universidade de São Paulo, Volume: 11 Supplement, Pages: 121-143, Published: 1997',
            result

        )

    def test_descriptive_short_format(self):

        del(self.sample['elocation'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])

        result = descriptive_short_format(**self.sample)

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, Volume: 67, Issue: 9 Supplement 3, Published: 2011',
            result
        )

    def test_descriptive_html_format(self):

        result = descriptive_html_format(**self.sample)

        self.assertEqual(
            '<div class="biblio_label"><span class="title">Revista Mal-Estar Subjetivo</span><span class="prefix volume">Volume:</span> <span class="value volume">67</span><span class="prefix number">Issue:</span> <span class="value number">9</span><span class="prefix supplement">Supplement</span> <span class="value supplement">3</span><span class="prefix pages">Article number:</span> <span class="value pages">e00120416</span><span class="prefix published">Published:</span> <span class="value published">2011</span></div>',
            result
        )

    def test_descriptive_html_short_format(self):

        del(self.sample['elocation'])
        del(self.sample['fpage'])
        del(self.sample['lpage'])

        result = descriptive_html_short_format(**self.sample)

        self.assertEqual(
            '<div class="biblio_label"><span class="title">Revista Mal-Estar Subjetivo</span><span class="prefix volume">Volume:</span> <span class="value volume">67</span><span class="prefix number">Issue:</span> <span class="value number">9</span><span class="prefix supplement">Supplement</span> <span class="value supplement">3</span><span class="prefix published">Published:</span> <span class="value published">2011</span></div>',
            result
        )

    def test_descriptive_very_short_format(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['lpage'])
        del(self.sample['fpage'])
        del(self.sample['elocation'])

        result = descriptive_very_short_format(**self.sample)

        self.assertEqual(
            '2011, Volume: 67, Issue: 9 Supplement 3',
            result
        )

    def test_descriptive_html_very_short_format(self):

        del(self.sample['title'])
        del(self.sample['short_title'])
        del(self.sample['lpage'])
        del(self.sample['fpage'])
        del(self.sample['elocation'])

        result = descriptive_html_very_short_format(**self.sample)

        self.assertEqual(
            '<div class="biblio_label"><span class="year">2011</span><span class="prefix volume">Volume:</span> <span class="value volume">67</span><span class="prefix number">Issue:</span> <span class="value number">9</span><span class="prefix supplement">Supplement</span> <span class="value supplement">3</span></div>',
            result
        )

    def test_pages(self):
        result = self.legendarium.pages

        self.assertEqual(
            '154-200',
            result
        )

    def test_pages_1(self):

        del(self.sample['fpage'])

        result = CitationFormatter(**self.sample).pages

        self.assertEqual(
            '200',
            result
        )

    def test_pages_2(self):

        del(self.sample['lpage'])

        result = CitationFormatter(**self.sample).pages

        self.assertEqual(
            '154',
            result
        )

    def test_pages_3(self):

        del(self.sample['fpage'])
        del(self.sample['lpage'])

        result = CitationFormatter(**self.sample).pages

        self.assertEqual(
            'e00120416',
            result
        )

    def test_pages_3(self):

        del(self.sample['fpage'])
        del(self.sample['lpage'])
        del(self.sample['elocation'])

        result = CitationFormatter(**self.sample).pages

        self.assertEqual(
            '',
            result
        )

    def test_get_numbers_1(self):

        result = get_numbers('v22')

        self.assertEqual('22', result)

    def test_get_numbers_2(self):

        result = get_numbers('vol. 22.')

        self.assertEqual('22', result)

    def test_get_numbers_3(self):

        result = get_numbers('vol.')

        self.assertEqual('', result)

    def test_build_raw_format(self):
        result = self.legendarium.rawformat

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, Rev.Mal-Estar Subj, 2011, 67, 9, 3, 154, 200, e00120416',
            result
        )
