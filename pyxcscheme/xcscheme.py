import os

def FindSchemeFilesOfTypeInPath(type_string, directory_path):
    schemes = list()
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if not file_name.startswith('.') and file_path.endswith('.xcscheme') and os.path.isfile(file_path):
            scheme_obj = xcscheme(type_string, file_path)
            schemes.append(scheme_obj)
    return schemes

def LoadSchemes(root_file_path):
    schemes = list()
    if os.path.exists(root_file_path):
        userdata_path = os.path.join(root_file_path, 'xcuserdata')
        has_userdata = os.path.exists(userdata_path)
    
        shareddata_path = os.path.join(root_file_path, 'xcshareddata')
        has_shareddata = os.path.exists(shareddata_path)
    
        # loading schemes
        
        # user schemes
        user_scheme_path = None
        has_user_schemes = False
        if has_userdata:
            user_scheme_path = os.path.join(userdata_path, ''+os.getlogin()+'.xcuserdatad/xcschemes')
            has_user_schemes = os.path.exists(user_scheme_path)
        
        if has_user_schemes:
            schemes.extend(FindSchemeFilesOfTypeInPath('user', user_scheme_path))
        
        # shared schemes
        shared_scheme_path = None
        has_shared_schemes = False
        if has_shareddata:
            shared_scheme_path = os.path.join(shareddata_path, 'xcschemes')
            has_shared_schemes = os.path.exists(shared_scheme_path)
        
        if has_shared_schemes:
            schemes.extend(FindSchemeFilesOfTypeInPath('shared', shared_scheme_path))
                    
    return schemes

import xml.etree.ElementTree as xml

import AnalyzeAction
import ArchiveAction
import Base_Action
import BuildableProductRunnable
import BuildableReference
import BuildAction
import BuildActionEntry
import LaunchAction
import ProfileAction
import Testables
import TestAction

class xcscheme(object):
    
    def __init__(self, scheme_type, scheme_path):
        if scheme_type == 'user' or scheme_type == 'shared':
            self.schemeType = scheme_type
            if os.path.exists(scheme_path):
                self.filePath = scheme_path
                self.name =  os.path.basename(self.filePath).split('.xcscheme')[0]
                self.contents = None
                try:
                    self.contents = xml.parse(self.filePath)
                except:
                    print('Error in reading scheme contents at path "%s"!', self.filePath)
                    raise
                
                self.buildAction = BuildAction.BuildAction(self.getAction('BuildAction'))
                self.testAction = TestAction.TestAction(self.getAction('TestAction'), self.buildAction)
                self.launchAction = LaunchAction.LaunchAction(self.getAction('LaunchAction'))
                self.profileAction = ProfileAction.ProfileAction(self.getAction('ProfileAction'))
                self.analyzeAction = AnalyzeAction.AnalyzeAction(self.getAction('AnalyzeAction'), self.buildAction)
                self.archiveAction = ArchiveAction.ArchiveAction(self.getAction('ArchiveAction'), self.buildAction)
                
            else:
                print('Error in loading scheme file at path "%s"!' % self.filePath)
                raise Exception
        else:
            print('Invalid scheme type "%s" passed to initializer!' % scheme_type)
            raise Exception
    
    def __repr__(self):
        if self.isValid():
            return '<%s : %s : "%s">' % (self.__class__.__name__, self.name, self.filePath)
        else:
            return '<%s : INVALID OBJECT>' % (self.__class__.__name__)
    
    def __attrs(self):
        return (self.name, self.filePath)

    def __eq__(self, other):
        return isinstance(other, xcscheme) and self.name == other.name and self.filePath == other.filePath and self.schemeType == other.schemeType

    def __hash__(self):
        return hash(self.__attrs())
    
    def isValid(self):
        return self.contents != None
    
    def actionLookup(self, action_name):
        """
        This method returns the method for the passed action type, None otherwise.
        """
        action_name = action_name.lower();
        lookup = {
            'build': self.buildAction,
            'test': self.testAction,
            'launch': self.launchAction,
            'profile': self.profileAction,
            'analyze': self.analyzeAction,
            'archive': self.archiveAction
        };
        return lookup.get(action_name, None);
    
    def getAction(self, action_type):
        """
        This method returns all the object for the passed action type, otherwise None.
        """
        action = None
        if self.isValid():
            action = filter(lambda action: action.tag == action_type, list(self.contents.getroot()))[0]
        return action