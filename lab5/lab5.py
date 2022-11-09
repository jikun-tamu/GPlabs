import arcpy

# Set up workspace directory; fetch gdb from last lab
arcpy.env.workspace = "C:/Users/Jikun/Documents/GP/GPlabs/lab5"
campus = "C:/Users/Jikun/Documents/GP/GPlabs/lab4/Campus.gdb"

# Setup our user input variables
buildingNumber_input = input("Please enter a building number: ")
bufferSize_input = int(input("Please enter a buffer size: "))

# Generate our where_clause
where_clause = "Bldg = '%s'" % buildingNumber_input

# Check if building exists
structures = campus + "/Structures"
cursor = arcpy.SearchCursor(structures, where_clause=where_clause)
shouldProceed = False
for row in cursor:
    if row.getValue("Bldg") == buildingNumber_input:
        shouldProceed = True

# If we shouldProceed do so
if shouldProceed:
    # Generate the name for our output buffer layer
    buildingBuff = "/building_%s_buffed_%s" % (buildingNumber_input, bufferSize_input)
    # Get reference to building
    buildingFeature = arcpy.Select_analysis(structures, campus + "/building_%s" % (buildingNumber_input), where_clause)
    # Buffer the selected building
    arcpy.Buffer_analysis(buildingFeature, campus + buildingBuff, bufferSize_input)
    # Clip the structures to our buffered feature
    arcpy.Clip_analysis(structures, campus + buildingBuff, campus + "/clip_%s" % (buildingNumber_input))
    # Remove the feature class we just created
    arcpy.Delete_management(campus + "/building_%s" % (buildingNumber_input))
else:
    print("Seems we couldn't find the building you entered")


