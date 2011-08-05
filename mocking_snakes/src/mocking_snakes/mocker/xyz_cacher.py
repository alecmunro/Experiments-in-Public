'''
Created on 2011-08-04

@author: Alec
'''
import time

DEFAULT_INTERVAL = 20

class XYZCacher(object):
    
    
    def __init__(self, time_mod=time):
        self.time = time_mod
    
    
    def keep_synced(self, interval=DEFAULT_INTERVAL):
        """Loop to keep the cache in sync with the original source.
        Check the cache every *interval* seconds."""
        
        self.sync_cache()
        self.write_cache()
        
        self.time.sleep(interval)
        
    
    def sync_cache(self):
        pass
    
    def write_cache(self):
        pass