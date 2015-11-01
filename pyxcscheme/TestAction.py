from .Base_Action import *

class TestAction(Base_Action):
    
    def __init__(self, action_xml, root_action=None):
        super(self.__class__, self).__init__(action_xml, root_action)
        self.selectedDebuggerIdentifier = self.contents.get('selectedDebuggerIdentifier');
        self.selectedLauncherIdentifier = self.contents.get('selectedLauncherIdentifier');
        self.shouldUseLaunchSchemeArgsEnv = self.contents.get('shouldUseLaunchSchemeArgsEnv');
        self.buildConfiguration = self.contents.get('buildConfiguration');