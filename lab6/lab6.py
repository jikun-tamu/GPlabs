import arcpy
import time
# Reference to our .aprx
project = arcpy.mp.ArcGISProject(r"C:\Users\Jikun\Documents\ArcGIS\Projects\gplab6" + r"\\gplab6.aprx")
# Grab the first map in the .aprx
readTime = 2.5
start = 0
maximum = 100
step = 25
arcpy.SetProgressor("step", "Read map...", start, maximum, step)
time.sleep(readTime)
campus = project.listMaps('Map')[0]
# Loop through available layers in the map
arcpy.SetProgressorPosition(start + step)
arcpy.SetProgressorLabel("Looping layers on map...")
time.sleep(readTime)
for layer in campus.listLayers():
    # Check that the layer is a feature layer
    if layer.isFeatureLayer:
        # Obtain a copy of the layer's symbology
        symbology = layer.symbology
        # Makes sure symbology has an attribute "renderer"
        if hasattr(symbology, 'renderer'):
            # Check if the layer's name is "Structures"
            if layer.name == "Structures":
                arcpy.SetProgressorPosition(start + step)
                arcpy.SetProgressorLabel("Structures found! Coloring....")
                time.sleep(readTime)
                # Update the copy's renderer to be "UniqueValueRenderer"
                symbology.updateRenderer('UniqueValueRenderer')
                # Tells arcpy that we want to use "Type" as our unique value
                symbology.renderer.fields = ["Type"]
                # Set the layer's actual symbology equal to the copy's
                layer.symbology = symbology # Very important step
            else:
                print("NOT Structures")
project.saveACopy(r"C:\Users\Jikun\Documents\ArcGIS\Projects\gplab6" + r"\\gplab6.aprx")

