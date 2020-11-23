# -*- coding: UTF-8 -*-

# Import from standard library
import os
import toolboxwagon
import pandas as pd
# Import from our lib
from toolboxwagon.lib import clean_data
import pytest
import datetime
import unittest
import sys
import urllib.parse
import requests
from toolboxwagon.lib import search_city


def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(toolboxwagon.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)


class TestWeather(unittest.TestCase):
    def test_search_city_for_paris(self):
        city = search_city('Paris')
        self.assertEqual(city['title'], 'Paris')
        self.assertEqual(city['woeid'], 615702)

    def test_search_city_for_london(self):
        city = search_city('London')
        self.assertEqual(city['title'], 'London')
        self.assertEqual(city['woeid'], 44418)
