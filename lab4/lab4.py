import arcpy

# Set up workspace directory and path
arcpy.env.workspace = "C:/Users/Jikun/Documents/GP/GPlabs/lab4"
folder_path = "C:/Users/Jikun/Documents/GP/GPlabs/lab4"

# create new GDB
arcpy.CreateFileGDB_management(folder_path, "GPlab4.gdb")

# read file
return1 = arcpy.MakeXYEventLayer_management('garages.csv', 'X', 'Y', 'garages')
arcpy.FeatureClassToGeodatabase_conversion(return1, r'GPlab4.gdb')

# copy structures to new GDB
arcpy.Copy_management(r"Campus.gdb\Structures", r"GPlab4.gdb\Structures")

# make sure spatial reference are consistent
spatial_ref = arcpy.Describe('GPlab4.gdb/Structures').spatialReference
arcpy.Project_management('GPlab4.gdb/garages', 'GPlab4.gdb/garages_projected', spatial_ref)

# buffer analysis & intersection
return2 = arcpy.Buffer_analysis('GPlab4.gdb/garages_projected', 'GPlab4.gdb/garages_buffered', '150 Meters')
arcpy.Intersect_analysis(['GPlab4.gdb/garages_buffered','GPlab4.gdb/Structures'], 'GPlab4.gdb/intersection', 'ALL')

# .csv file output
arcpy.TableToTable_conversion('GPlab4.gdb/intersection', folder_path, 'submit.csv')