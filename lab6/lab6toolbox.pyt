# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [UniqueValueMap]


class UniqueValueMap(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "UniqueValueMap"
        self.description = "Create a unique value map"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        # Reference to our .aprx
        project = arcpy.mp.ArcGISProject(r"C:\Users\Jikun\Documents\ArcGIS\Projects\gplab6" + r"\\gplab6.aprx")
        # Grab the first map in the .aprx
        campus = project.listMaps('Map')[0]
        # Loop through available layers in the map
        for layer in campus.listLayers():
            # Check that the layer is a feature layer
            if layer.isFeatureLayer:
                # Obtain a copy of the layer's symbology
                symbology = layer.symbology
                # Makes sure symbology has an attribute "renderer"
                if hasattr(symbology, 'renderer'):
                    # Check if the layer's name is "Structures"
                    if layer.name == "Structures":
                        # Update the copy's renderer to be "UniqueValueRenderer"
                        symbology.updateRenderer('UniqueValueRenderer')
                        # Tells arcpy that we want to use "Type" as our unique value
                        symbology.renderer.fields = ["Type"]
                        # Set the layer's actual symbology equal to the copy's
                        layer.symbology = symbology # Very important step
                    else:
                        print("NOT Structures")
        project.saveACopy(r"C:\Users\Jikun\Documents\ArcGIS\Projects\gplab6" + r"\\gplab6.aprx")
        return
