import arcpy
source = r"C:\Users\Jikun\Documents\GP\GPlabs\lab7\\"
band1 = arcpy.sa.Raster("b.TIF") # blue
band2 = arcpy.sa.Raster("g.TIF") # green
band3 = arcpy.sa.Raster("r.TIF") # red
composite = arcpy.CompositeBands_management([band1, band2, band3], source + "combined.tif")

gdb = r"C:\Users\Jikun\Documents\GP\GPlabs\lab7\gplab7"
azimuth = 45
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(gdb + r"\tx_dem", gdb + r"\tx_hillshade", azimuth, altitude, shadows, z_factor)

output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"
z_unit = "METER"
arcpy.ddd.Slope(gdb + "/tx_dem", gdb + "/tx_dem_slopes", output_measurement, z_factor, method, z_unit)
