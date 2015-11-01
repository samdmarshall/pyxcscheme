import xml.etree.ElementTree as xml

class Base_Action(object):
    
    def __init__(self, action_xml, root_action=None):
        self.root = root_action
        self.contents = action_xml;
    
    def performAction(self, container, xcparse_object, configuration_name, additional_settings):
        """
        container = xcscheme object - scheme that is having an action performed
        xcparse_object = xcparse object
        scheme_config_settings = dictionary containing any additional environment variables to set
        """
        print 'implement me!';