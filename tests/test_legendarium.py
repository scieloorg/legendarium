# coding: utf-8
import unittest

from legendarium.formatter import (
    CitationFormatter,
    short_format,
    very_short_format,
    descriptive_format,
    descriptive_very_short_format,
    descriptive_html_format,
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
            'Rev.Mal-Estar Subj, 2011 67(9) suppl. 3',
            result
        )

    def test_descriptive_format(self):

        result = descriptive_format(**self.sample)

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, 2011, Volume: 67, Number: 9, Supplement: 3, Article number: e00120416',
            result
        )

    def test_descriptive_format_1(self):

        self.sample['elocation'] = ''

        result = descriptive_format(**self.sample)

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, 2011, Volume: 67, Number: 9, Supplement: 3, Pages: 154-200',
            result
        )

    def test_descriptive_html_format(self):

        result = descriptive_html_format(**self.sample)

        self.assertEqual(
            '<div class="biblio_label"><span class="title">Revista Mal-Estar Subjetivo</span><span class="year">2011</span><span class="prefix volume">Volume:</span> <span class="value volume">67</span><span class="prefix number">Number:</span> <span class="value number">9</span><span class="prefix supplement">Supplement:</span> <span class="value supplement">3</span><span class="prefix pages">Article number:</span> <span class="value pages">e00120416</span></div>',
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
            '2011, Volume: 67, Number: 9, Supplement: 3',
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
            '<div class="biblio_label"><span class="year">2011</span><span class="prefix volume">Volume:</span> <span class="value volume">67</span><span class="prefix number">Number:</span> <span class="value number">9</span><span class="prefix supplement">Supplement:</span> <span class="value supplement">3</span></div>',
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
