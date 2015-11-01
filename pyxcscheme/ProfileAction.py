from .Base_Action import *

class ProfileAction(Base_Action):
    
    def __init__(self, action_xml, root_action=None):
        super(self.__class__, self).__init__(action_xml, root_action)
        self.shouldUseLaunchSchemeArgsEnv = self.contents.get('shouldUseLaunchSchemeArgsEnv');
        self.savedToolIdentifier = self.contents.get('savedToolIdentifier');
        self.useCustomWorkingDirectory = self.contents.get('useCustomWorkingDirectory');
        self.buildConfiguration = self.contents.get('buildConfiguration');
        self.debugDocumentVersioning = self.contents.get('debugDocumentVersioning');