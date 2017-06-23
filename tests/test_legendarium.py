# coding: utf-8
import unittest

from legendarium.legendarium import Legendarium


class TestLegendarium(unittest.TestCase):

    def setUp(self):
        self.dict_leg = {'acron_title': u'Rev.Mal-Estar Subj',
                         'year_pub': u'2011',
                         'volume': u'67',
                         'number': u'9',
                         'fpage': u'154',
                         'lpage': u'200',
                         'article_id': u'e00120416'
                         }

    def test_build_legend_with_all_param(self):
        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67(9):e00120416', leg.stamp)

    def test_build_legend_without_acron_title(self):

        del(self.dict_leg['acron_title'])  # Remove the journal

        leg = Legendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.stamp)

    def test_build_legend_without_year_pub(self):

        del(self.dict_leg['year_pub'])  # Remove the publisher year

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj;67(9):e00120416', leg.stamp)

    def test_build_legend_without_volume(self):

        del(self.dict_leg['volume'])  # Remove the volume

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;(9):e00120416', leg.stamp)

    def test_build_legend_without_number(self):

        del(self.dict_leg['number'])  # Remove the number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67:e00120416', leg.stamp)

    def test_build_legend_without_volume_and_number(self):

        del(self.dict_leg['volume'])  # Remove the volume
        del(self.dict_leg['number'])  # Remove the number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011:e00120416', leg.stamp)

    def test_build_legend_without_volume_and_number_and_year_pub(self):

        del(self.dict_leg['volume'])  # Remove the volume
        del(self.dict_leg['number'])  # Remove the number
        del(self.dict_leg['year_pub'])  # Remove the number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj:e00120416', leg.stamp)

    def test_build_legend_without_volume_and_number_and_year_pub_and_pages(self):

        del(self.dict_leg['volume'])  # Remove the volume
        del(self.dict_leg['number'])  # Remove the number
        del(self.dict_leg['year_pub'])  # Remove the publisher year
        del(self.dict_leg['fpage'])  # Remove the first page
        del(self.dict_leg['lpage'])  # Remove the last page
        del(self.dict_leg['article_id'])  # Remove the article identifier

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj', leg.stamp)

    def test_build_legend_with_wrong_value_in_year(self):

        self.dict_leg['year_pub'] = "20"  # Wrong value in year

        leg = Legendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.stamp)

    def test_build_legend_with_wrong_value_in_year_more_digits(self):

        self.dict_leg['year_pub'] = "2009088"  # Wrong value in year

        leg = Legendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.stamp)

    def test_build_legend_with_wrong_value_volume(self):

        self.dict_leg['volume'] = "903A"  # Wrong value in volume

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;903(9):e00120416', leg.stamp)

    def test_build_legend_with_wrong_value_fpage(self):

        del(self.dict_leg['article_id'])

        self.dict_leg['fpage'] = "oja9sn10"  # Wrong value in fpage, return wrong

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67(9):oja9sn10-200', leg.stamp)

    def test_build_legend_with_wrong_value_lpage(self):

        del(self.dict_leg['article_id'])

        self.dict_leg['lpage'] = "oja9sn10"  # Wrong value in lpage, return wrong

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67(9):154-oja9sn10', leg.stamp)

    def test_build_legend_with_just_fpage(self):

        del(self.dict_leg['lpage'])  # Remove fpage
        del(self.dict_leg['article_id'])  # Remove elocation that is preference

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67(9):154', leg.stamp)

    def test_build_legend_with_just_lpage(self):

        del(self.dict_leg['fpage'])  # Remove fpage
        del(self.dict_leg['article_id'])  # Remove elocation that is preference

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67(9):200', leg.stamp)

    def test_build_legend_without_fpage_lpage_elocation(self):

        del(self.dict_leg['fpage'])  # Remove fpage
        del(self.dict_leg['lpage'])  # Remove lpage
        del(self.dict_leg['article_id'])  # Remove article_id

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67(9)', leg.stamp)

    def test_build_legend_without_volume_number(self):

        del(self.dict_leg['volume'])  # Remove volume
        del(self.dict_leg['number'])  # Remove number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011:e00120416', leg.stamp)

    def test_build_legend_with_elocation(self):

        del(self.dict_leg['fpage'])  # Remove the fpage
        del(self.dict_leg['lpage'])  # Remove the lpage

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67(9):e00120416', leg.stamp)

    def test_build_acron_title_with_diacritics(self):

        self.dict_leg['acron_title'] = u'Acta Ortopédica Brasileira'

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Acta Ortopédica Brasileira 2011;67(9):e00120416', leg.stamp)

    def test_build_acron_and_check_if_article_id_is_the_preference(self):

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67(9):e00120416', leg.stamp)

    def test_build_acron_when_number_is_None(self):

        self.dict_leg['number'] = None

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;67:e00120416', leg.stamp)

    def test_build_acron_when_volume_is_None(self):

        self.dict_leg['volume'] = None

        leg = Legendarium(**self.dict_leg)

        self.assertEqual(u'Rev.Mal-Estar Subj 2011;(9):e00120416', leg.stamp)

if __name__ == "__main__":
    unittest.main()
