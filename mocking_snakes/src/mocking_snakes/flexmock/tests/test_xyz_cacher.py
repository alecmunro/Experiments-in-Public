'''
Created on 2011-08-05

@author: Alec
'''
from unittest import TestCase

from flexmock import flexmock

from mocking_snakes.flexmock import xyz_cacher as mut

SLEEP_TIME = 60

class TestXYZCacher(TestCase):
    
    def test_keep_synced(self):
        """Keep the cache in sync with the original source."""
        m_time = flexmock()
        cacher = mut.XYZCacher(time_mod=m_time)
        flexmock(cacher)
        
        cacher.should_receive("sync_cache").once
        cacher.should_receive("write_cache").once
        
        m_time.should_receive("sleep").with_args(SLEEP_TIME).at_least.once
        
        cacher.keep_synced(interval=SLEEP_TIME)