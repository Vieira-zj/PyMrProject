# -*- coding: utf-8 -*-
'''
@author: zhengjin

A demo to write the test scripts base on unit test framework.

'''

import os
import sys
import time
import unittest
# import logging

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrRunner import MrTestRunner
from MrUtils import MrBaseConstants
from MrUtils import MrBaseMrUtils

# ----------------------------------------------------------
# Functions
# ----------------------------------------------------------
def init_env():
    print 'initialize the ENV variables.'
    MrBaseConstants.init_g_path_vars_for_win(MrTestRunner.g_user_run_num)
#     MrBaseMrUtils.init_log_config(MrBaseConstants.g_mr_prj_root_path)


# ----------------------------------------------------------
# Demo test cases
# ----------------------------------------------------------
class mr_test_demos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # class method is not invoked from monkeyrunner
        print 'class setUp.'
        
    @classmethod
    def tearDownClass(cls):
        # class method is not invoked from monkeyrunner
        print 'class tearDown.'

    def setUp(self):
        print 'method setUp.'
        self.device = MrBaseMrUtils.get_easy_device(MrTestRunner.g_user_device_no)
        
    def tearDown(self):
        print 'method tearDown.'

    def test_mr_demo_21(self):
        # test get text of textview on file manager main page
        print 'Run test case: mr_test_demo_01' 
        MrBaseMrUtils.start_activity(self.device, MrBaseConstants.g_component_filemanager)
        time.sleep(3.0)
        view_title = MrBaseMrUtils.get_text_by_id(self.device, 'id/tab_title')
        
        print 'Text of title: %s' %view_title
        self.assertTrue(len(view_title) > 0)
        
    def ignore_test_mr_demo_22(self):
        # test get text of textview on dynamic page "news"
        print 'Run test case: run mr_test_demo_02'
        MrBaseMrUtils.start_activity(self.device, MrBaseConstants.g_component_video_news)
        time.sleep(3.0)
        view_title = MrBaseMrUtils.get_text_by_id(self.device, 'id/news_special_list_item_title')
        print 'Text of title: %s' %view_title
        
    # test different activity
    def ignore_test_mr_demo_23(self):
        print 'TODO: test_mr_demo_23'


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
if __name__ == '__main__':
    init_env()
    unittest.main()

    pass
