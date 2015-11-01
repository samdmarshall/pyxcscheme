class BuildableReference(object):
    
    def __init__(self, entry_item):
        self.contents = entry_item;
        self.BuildableIdentifier = self.contents.get('BuildableIdentifier', None)
        self.BlueprintIdentifier = self.contents.get('BlueprintIdentifier', None)
        self.BuildableName = self.contents.get('BuildableName', None);
        self.BlueprintName = self.contents.get('BlueprintName', None);
        self.ReferencedContainer = self.contents.get('ReferencedContainer', None);