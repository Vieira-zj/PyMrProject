# -*- coding: utf-8 -*-
'''
Created on 2016-8-8

@author: zhengjin
'''
import sys
import os

sys.path.append(os.environ['MR_PROJECT_PATH'])
from MrUtils import MrBaseMrUtils, MrBaseConstants
from MrTestCases import MrTestTemplate

# ----------------------------------------------------------
# Variables
# ----------------------------------------------------------
g_device = None
g_hierarchy_viewer = None
g_snapshot_dir = ''


# ----------------------------------------------------------
# Test cases
# ----------------------------------------------------------
def test_init():
    global g_device
    global g_hierarchy_viewer
    global g_snapshot_dir
 
    g_device = MrTestTemplate.g_device
    g_hierarchy_viewer = MrTestTemplate.g_hierarchy_viewer
    g_snapshot_dir = MrTestTemplate.g_snapshot_dir

def test_open_news_tab_of_right_area():
    MrTestTemplate.open_tab((1350,300))
    
    msg = 'test_open_news_tab_of_right_area, verify main title text of news tab'
    main_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/news_special_list_item_title')
    if main_title is None or main_title == '':
        MrTestTemplate.failed_and_take_snapshot(msg)
        return
    else:
        print 'News tab main title: %s' %main_title
        print 'PASS, %s' %msg

    msg = 'test_open_news_tab_of_right_area, verify sub title text of news tab'    
    sub_title = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/news_play_title')
    if sub_title is None or sub_title == '':
        MrTestTemplate.failed_and_take_snapshot(msg)
        return
    else:
        print 'News tab sub title: %s' %sub_title.split(' ')[0]
        print 'PASS, %s' %msg

    msg = 'test_open_news_tab_of_right_area, verify video player\n'
    player_view = MrBaseMrUtils.find_view_by_id(g_hierarchy_viewer, 'id/news_player_view')
    if player_view is None:
        MrTestTemplate.failed_and_take_snapshot(msg)
    else:
        print 'Player view: %s' %type(player_view)
        print 'PASS, %s' %msg

def test_playing_news():
    # max new player windows
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_RIGHT)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_RIGHT)
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)

    # pause player
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    cur_play_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_current')
    time_start = MrTestTemplate.format_play_time(cur_play_time)
    
    # replay news
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    play_time = 15.0
    MrBaseMrUtils.mr_wait(play_time)
    
    # pause player
    MrBaseMrUtils.press_and_wait(g_device, MrBaseConstants.KEY_ENTER)
    cur_play_time = MrBaseMrUtils.get_text_by_id(g_hierarchy_viewer, 'id/time_current')
    time_end = MrTestTemplate.format_play_time(cur_play_time)
    
    msg = 'test_playing_news, verify news is playing\n'
    during = time_end - time_start
    print 'Play news during time: %d' %during
    if during >= play_time:
        print 'PASS, %s' %msg
    else:
        MrTestTemplate.failed_and_take_snapshot(msg)


# ----------------------------------------------------------
# Main
# ----------------------------------------------------------
def test_main():
    test_open_news_tab_of_right_area()
    test_playing_news()

MrTestTemplate.main(os.path.basename(__file__), 
                    test_init,
                    test_main)
