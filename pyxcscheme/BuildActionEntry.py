from .BuildableReference import *

class BuildActionEntry(object):
    
    def __init__(self, entry_item):
        self.contents = entry_item;
        self.buildForTesting = self.contents.get('buildForTesting');
        self.buildForRunning = self.contents.get('buildForRunning');
        self.buildForProfiling = self.contents.get('buildForProfiling');
        self.buildForArchiving = self.contents.get('buildForArchiving');
        self.buildForAnalyzing = self.contents.get('buildForAnalyzing');
        self.target = BuildableReference(self.contents.find('./BuildableReference'));