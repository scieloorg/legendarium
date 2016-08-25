# coding: utf-8
import unittest

from legendarium import Legendarium


class TestLegendarium(unittest.TestCase):

    def setUp(self):
        self.dict_leg = {'acron_title': 'Rev.Mal-Estar Subj',
                         'year_pub': '2011',
                         'volume': '67',
                         'number': '9',
                         'fpage': '154',
                         'lpage':'200',
                         'article_id':'e00120416'
                         }


    def test_build_legend_with_all_param(self):
        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011;67(9):154-200', leg.stamp)


    def test_build_legend_without_acron_title(self):

        del(self.dict_leg['acron_title']) # Remove the journal

        leg = Legendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.stamp)


    def test_build_legend_without_year_pub(self):

        del(self.dict_leg['year_pub']) # Remove the publisher year

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj;67(9):154-200', leg.stamp)


    def test_build_legend_without_volume(self):

        del(self.dict_leg['volume']) # Remove the volume

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011;(9):154-200', leg.stamp)


    def test_build_legend_without_number(self):

        del(self.dict_leg['number']) # Remove the number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011;67:154-200', leg.stamp)


    def test_build_legend_without_volume_and_number(self):

        del(self.dict_leg['volume']) # Remove the volume
        del(self.dict_leg['number']) # Remove the number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011:154-200', leg.stamp)


    def test_build_legend_without_volume_and_number_and_year_pub(self):

        del(self.dict_leg['volume']) # Remove the volume
        del(self.dict_leg['number']) # Remove the number
        del(self.dict_leg['year_pub']) # Remove the number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj:154-200', leg.stamp)


    def test_build_legend_without_volume_and_number_and_year_pub_and_pages(self):

        del(self.dict_leg['volume']) # Remove the volume
        del(self.dict_leg['number']) # Remove the number
        del(self.dict_leg['year_pub']) # Remove the publisher year
        del(self.dict_leg['fpage']) # Remove the first page
        del(self.dict_leg['lpage']) # Remove the last page
        del(self.dict_leg['article_id']) # Remove the article identifier

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj', leg.stamp)


    def test_build_legend_with_wrong_value_in_year(self):

        self.dict_leg['year_pub'] = "20" # Wrong value in year

        leg = Legendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.stamp)


    def test_build_legend_with_wrong_value_in_year_more_digits(self):

        self.dict_leg['year_pub'] = "2009088" # Wrong value in year

        leg = Legendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.stamp)


    def test_build_legend_with_wrong_value_volume(self):

        self.dict_leg['volume'] = "903A" # Wrong value in volume

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011;903(9):154-200', leg.stamp)


    def test_build_legend_with_wrong_value_fpage(self):

        self.dict_leg['fpage'] = "oja9sn10" # Wrong value in fpage

        leg = Legendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.stamp)


    def test_build_legend_with_wrong_value_lpage(self):

        self.dict_leg['lpage'] = "oja9sn10" # Wrong value in lpage

        leg = Legendarium(**self.dict_leg)

        self.assertRaises(ValueError, lambda: leg.stamp)


    def test_build_legend_with_just_fpage(self):

        del(self.dict_leg['lpage']) # Remove fpage

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011;67(9):154', leg.stamp)


    def test_build_legend_with_just_lpage(self):

        del(self.dict_leg['fpage']) # Remove fpage

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011;67(9):200', leg.stamp)


    def test_build_legend_without_fpage_lpage_elocation(self):

        del(self.dict_leg['fpage']) # Remove fpage
        del(self.dict_leg['lpage']) # Remove lpage
        del(self.dict_leg['article_id']) # Remove article_id

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011;67(9)', leg.stamp)


    def test_build_legend_without_volume_number(self):

        del(self.dict_leg['volume']) # Remove volume
        del(self.dict_leg['number']) # Remove number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011:154-200', leg.stamp)


    def test_build_legend_with_elocation(self):

        del(self.dict_leg['fpage']) # Remove the volume
        del(self.dict_leg['lpage']) # Remove the number

        leg = Legendarium(**self.dict_leg)

        self.assertEqual('Rev.Mal-Estar Subj 2011;67(9):e00120416', leg.stamp)

if __name__ == "__main__":
    unittest.main()
