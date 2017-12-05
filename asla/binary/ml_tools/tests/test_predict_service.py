import os
import sys
root_path = os.path.dirname(os.path.abspath('../..'))
sys.path.append(root_path)

import unittest
import numpy as np

os.environ["NOQT"] = "1"

from ...ml_tools.predict_service import PredictService


class TestPredictService(unittest.TestCase):

    def test_predict_label(self):
        cur_dir = os.path.dirname(__file__)
        model_file = os.path.join(cur_dir, '6am_model.pkl')
        scaler_file = os.path.join(cur_dir, '6am_scaler.pkl')
        predict_service = PredictService(model_file, scaler_file)
        # Dummy data to predict
        predict_service.to_predict = np.asarray([[5.0,0.125,0.0,0.0,0.0,0.0,0.55296113010933867,0.67653411572754241,0.69780003132586876,0.74102900850043096,0.6634389246600072,0.11345243800438023,0.17445422016899959,0.26690042450082874,0.31103571933640223,0.080651081838595526,0.18339206841125338,0.25992562492289384,0.10725728253357197,0.19136316840382186,0.11052538451193428,2.3600479179444553,1.423684074243704,1.2193373478313259,1.3787421430525422,1.8782982966727362,0.88200012058902488,0.90492168372858905,0.91951544728644952,0.95917906534368502,0.23522334780831472,0.47179926359638952,0.6895920968465824,0.24220802345506276,0.46665416180339131,0.2275940909176403,0.82858997483909991,1.0598975988045112,1.0613093621751988,1.0086268166263856,0.97205897225001392,0.55971720564115068,0.66786072033963118,0.73357604437143975,0.77366485896820913,0.19619047142955057,0.36402141134592148,0.50970999551465102,0.17971702237110246,0.33953478956353339,0.16585222754080831,0.67631114049672947,0.83918840073946277,0.86016485218826633,0.86079636953801353,0.77518341191654894,0.27961422018532089,0.37843416909519018,0.48128123049558713,0.54093294045127904,0.12715428622811437,0.25668807567507013,0.37087256366304938,0.13593514205045282,0.26430273204264987,0.14419067025281573,91.448771004802481,92.5260190491868,74.812856611354078,67.421586184044997,14.796171350880568,25.544343151467515,36.770627980511946,18.311535247336849,28.377390573189974,11.278095655880383,64.73988145362145,27.534519142823441,29.676516138823377,18.087582735962236,22.749053869250538,-0.046837049419991672,0.94903579354286194,-0.30791656114161015,41.244068145751953,0.97056254744529724,0.90398047491908073,-0.10257465206086636,-0.31005820445716381,-0.94296222925186157,-0.010315084829926491,0.080708242952823639,-0.043758377432823181,3.6186888217926025,-5.7211041450500488,-36.080680847167969,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
]])
        label = predict_service.predict_label()[0]
        assert label is not None
