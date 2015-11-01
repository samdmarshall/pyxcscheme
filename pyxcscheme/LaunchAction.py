from .Base_Action import *

class LaunchAction(Base_Action):
    
    def __init__(self, action_xml, root_action=None):
        super(self.__class__, self).__init__(action_xml, root_action)
        self.selectedDebuggerIdentifier = self.contents.get('selectedDebuggerIdentifier');
        self.selectedLauncherIdentifier = self.contents.get('selectedLauncherIdentifier');
        self.launchStyle = self.contents.get('launchStyle');
        self.useCustomWorkingDirectory = self.contents.get('useCustomWorkingDirectory');
        self.buildConfiguration = self.contents.get('buildConfiguration');
        self.ignoresPersistentStateOnLaunch = self.contents.get('ignoresPersistentStateOnLaunch');
        self.debugDocumentVersioning = self.contents.get('debugDocumentVersioning');
        self.allowLocationSimulation = self.contents.get('allowLocationSimulation');