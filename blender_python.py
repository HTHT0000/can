import bpy
import math


def select_all():
    bpy.ops.object.select_all(action='SELECT')

def delete_all():
    if len(bpy.data.objects) > 0:
        select_all()
        bpy.ops.object.delete(use_global=False)
delete_all()

bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

data_kyuu = []
oiler = []
sum_data = []
ob = bpy.context.object
frame_num = 0
i = 0

#bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))


path = r"C:\Users\81807\OneDrive\デスクトップ\データの場所\kyuujiku.csv"
with open(path,"r") as f:
    next(f)
    for line in f:
        result = line.split(",")
        data_kyuu.append(result)
    #map(map_func,data_kyuu)
    print(data_kyuu)

path_s = r"C:\Users\81807\OneDrive\デスクトップ\多少いじったデータ保管場所\0tuikasita.csv"
with open(path_s,"r") as s:
    for lis in s:
        result_s = lis.split(",")
        sum_data.append(result_s)

oiler_x = float(data_kyuu[i][0])
oiler_y = float(data_kyuu[i][1])
oiler_z = float(data_kyuu[i][2])
bpy.context.scene.frame_set(frame_num)
float(data_kyuu[i+1][0])
ob.rotation_euler = (oiler_x/180*math.pi,oiler_y/180*math.pi,float(data_kyuu[i+1][2])/180*math.pi)
ob.keyframe_insert(data_path = "rotation_euler")
frame_num += 30


for i in range(len(data_kyuu)):
    if float(float(data_kyuu[i+1][0]) - oiler_x) > 180:
        oiler_x = float(data_kyuu[i+1][0]) - 360
    elif float(float(data_kyuu[i+1][0]) - oiler_x) < -180:
        oiler_x = -(float(data_kyuu[i+1][0])) + 360
    else:
        oiler_x = float(data_kyuu[i+1][0])
    if float(float(data_kyuu[i+1][1]) - oiler_y) > 180:
        oiler_y = float(data_kyuu[i+1][1]) + float(data_kyuu[i][1]) - 360
    elif float(float(data_kyuu[i+1][1]) - oiler_y) < -180:
        oiler_y = -(float(data_kyuu[i+1][1])) + 360
    else:
        oiler_y = float(data_kyuu[i+1][1])
    if float(float(data_kyuu[i+1][2]) - oiler_z) > 180:
        oiler_z = float(data_kyuu[i+1][2]) + float(data_kyuu[i][2]) - 360
    elif float(float(data_kyuu[i+1][2]) - oiler_z) < -180:
        oiler_z = -(float(data_kyuu[i+1][2])) + 360
    else:
        oiler_z = float(data_kyuu[i+1][2])
        
        
    print(oiler_x)
    print(oiler_y)
    print(oiler_z)

    bpy.context.scene.frame_set(frame_num)
    float(data_kyuu[i+1][0])
    ob.rotation_euler = (oiler_x/180*math.pi,oiler_y/180*math.pi,float(data_kyuu[i+1][2])/180*math.pi)
    ob.keyframe_insert(data_path = "rotation_euler")

    ob.location = sum_data[i+1]
    ob.keyframe_insert(data_path = "location")

    frame_num += 30
