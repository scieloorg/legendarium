# coding: utf-8
import unittest

from legendarium.urlegendarium import URLegendarium


class TestLegendarium(unittest.TestCase):

    def setUp(self):
        self.dict_leg = {'acron': u'spm',
                         'year_pub': u'2011',
                         'volume': u'67',
                         'number': u'9',
                         'suppl_number': u'3',
                         'fpage': u'154',
                         'lpage': u'200',
                         'article_id': u'e00120416'
                         }

    def test_build_url_article_with_sequence(self):
        del(self.dict_leg['article_id'])
        self.dict_leg['fpage_sequence'] = 1

        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67n9suppl3/154_1-200', str(leg))

    def test_build_url_article_with_sequence_without_last_page(self):
        del(self.dict_leg['article_id'])
        del(self.dict_leg['lpage'])
        self.dict_leg['fpage_sequence'] = 1

        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67n9suppl3/154_1', str(leg))

    def test_build_url_journal_with_all_param(self):
        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/', leg.url_journal)

    def test_build_url_issue_with_all_param(self):
        del(self.dict_leg['suppl_number'])  # Remove the suppl_number

        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67n9', leg.url_issue)

    def test_build_url_article_with_all_param(self):
        del(self.dict_leg['suppl_number'])  # Remove the suppl_number
        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67n9/e00120416', leg.url_article)

    def test_build_url_article_without_eloaction_param(self):
        del(self.dict_leg['suppl_number'])  # Remove the suppl_number
        del(self.dict_leg['article_id'])

        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67n9/154-200', leg.url_article)

    def test_build_url_article_without_fpage_param(self):
        del(self.dict_leg['suppl_number'])  # Remove the suppl_number
        del(self.dict_leg['article_id'])
        del(self.dict_leg['fpage'])

        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67n9/200', leg.url_article)

    def test_build_url_article_without_lpage_param(self):
        del(self.dict_leg['suppl_number'])  # Remove the suppl_number
        del(self.dict_leg['article_id'])
        del(self.dict_leg['lpage'])

        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67n9/154', leg.url_article)

    def test_build_url_journal_without_acron_param(self):

        del(self.dict_leg['acron'])  # Remove the acron

        leg = URLegendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.url_journal)

    def test_build_url_issue_without_year_vol_num_param(self):

        del(self.dict_leg['year_pub'])  # Remove the year_pub
        del(self.dict_leg['volume'])  # Remove the volume
        del(self.dict_leg['number'])  # Remove the number
        del(self.dict_leg['suppl_number'])  # Remove the suppl_number

        leg = URLegendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.url_issue)

    def test_build_url_issue_supplment_volume(self):

        del(self.dict_leg['number'])  # Remove the number

        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67suppl3', leg.url_issue)

    def test_build_url_issue_supplment_number(self):

        leg = URLegendarium(**self.dict_leg)

        self.assertEqual(u'spm/2011.v67n9suppl3', leg.url_issue)


if __name__ == "__main__":
    unittest.main()
