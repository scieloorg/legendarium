# coding: utf-8
import unittest

from legendarium.legendarium import (
    Legendarium,
    short_format,
    descriptive_format,
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

        self.legendarium = Legendarium(**self.sample)

    def test_format(self):

        result = self.legendarium.format('%T, %Y, %v(%n), %p')

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, 2011, 67(9), 154-200',
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

        data = dict(self.sample)
        result = descriptive_format(**data)

        self.assertEqual(
            'Revista Mal-Estar Subjetivo, 2011 volume: 67 number: 9 supplement: 3 position: 154-200',
            result
        )

    def test_pages(self):
        result = self.legendarium.pages

        self.assertEqual(
            '154-200',
            result
        )

    def test_pages_1(self):

        data = dict(self.sample)
        del(data['fpage'])
        result = Legendarium(**data).pages

        self.assertEqual(
            '200',
            result
        )

    def test_pages_2(self):

        data = dict(self.sample)
        del(data['lpage'])
        result = Legendarium(**data).pages

        self.assertEqual(
            '154',
            result
        )

    def test_pages_3(self):

        data = dict(self.sample)
        del(data['fpage'])
        del(data['lpage'])
        result = Legendarium(**data).pages

        self.assertEqual(
            'e00120416',
            result
        )

    def test_pages_3(self):

        data = dict(self.sample)
        del(data['fpage'])
        del(data['lpage'])
        del(data['elocation'])
        result = Legendarium(**data).pages

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
