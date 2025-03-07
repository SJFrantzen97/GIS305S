import arcpy
arcpy.env.workspace = r"C:\Users\Spencer\Desktop\FRCCSpring2025\ProgrammingGIS\Assignments\Assignment1b\Assignment1b.gdb"
arcpy.env.overwriteOutput = True


flayer = arcpy.MakeFeatureLayer_management("U.S. Cities", "Cities_Layer")

qry = "POP1990 > 20000"
arcpy.management.SelectLayerByAttribute(flayer, "NEW_SELECTION", qry)

my_cnt = arcpy.management.GetCount(flayer)
print(f"Selected cities is: {my_cnt}")

arcpy.management.SelectLayerByLocation(flayer, "WITHIN_A_DISTANCE", "U.S. Rivers (Generalized)", "10 miles", "SUBSET_SELECTION")

my_cnt = arcpy.management.GetCount(flayer)
print(f"Selected cities is: {my_cnt}")


field = 'POP1990'
total = 0
i = 1
with arcpy.da.SearchCursor(flayer, field) as cursor:
    for row in cursor:
        print(i, str(row[0]))
        total = total + row[0]
        i = i + 1

print(f"Total population is: {total:,}")
