from .Base_Action import *

class AnalyzeAction(Base_Action):
    
    def __init__(self, action_xml, root_action=None):
        super(self.__class__, self).__init__(action_xml, root_action)
        self.buildConfiguration = self.contents.get('buildConfiguration');