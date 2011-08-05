'''
Created on 2011-08-04

@author: Alec
'''
from mocker import MockerTestCase

from mocking_snakes.mocker import xyz_cacher as mut

SLEEP_TIME = 60

class TestXYZCacher(MockerTestCase):
    
    def test_keep_synced(self):
        """Keep the cache in sync with the original source."""
        m_time = self.mocker.mock()
        cacher = mut.XYZCacher(time_mod=m_time)
        p_cacher = self.mocker.patch(cacher)
        
        p_cacher.sync_cache()
        p_cacher.write_cache()
        
        m_time.sleep(SLEEP_TIME)
        
        self.mocker.replay()
        
        cacher.keep_synced(interval=SLEEP_TIME)