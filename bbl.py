import bpy
import bmesh
import math as m

def del_existing():
   del_obj = [item.name for item in bpy.data.objects if item.type == "MESH" or "LAMP"]
for obj in del_obj:
    bpy.data.objects[obj].select = True
bpy.ops.object.delete()

for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

def makeMaterial(name, diffuse, specular, alpha):
   mat = bpy.data.materials.new(name)
   mat.diffuse_color = diffuse
   mat.diffuse_shader = 'LAMBERT' 
   mat.diffuse_intensity = 1.0 
   mat.specular_color = specular
   mat.specular_shader = 'PHONG'
   mat.specular_intensity = 0.5
   mat.alpha = alpha
   mat.ambient = 1
   return mat

def setMaterial(ob, mat):
   me = ob.data
   me.materials.append(mat)

def add_lamp(lname,srctype,location):
   scene = bpy.context.scene
   newl = bpy.data.lamps.new(name=lname,type=srctype)
   objl = bpy.data.objects.new(name=lname, object_data = newl)
   scene.objects.link(objl)
   objl.location=location
   print(list(bpy.data.objects))
   bpy.data.objects[lname].select = True
   bpy.data.objects["hemi"].data.energy = 0.9
   #scene.objects.active = objl
   #objl.select = True
   #scene.objects.active = objl
   #objl.use_trasparency = True

def add_camera():
   cam = bpy.ops.object.camera_add(view_align=True, location=(0.0,34,11.0),rotation=(m.radians(80), 0.0, m.radians(180)))
   #cam.location = (6.0,6.0,7.0)

def my_handler(scene):
   bpy.data.objects["Plane.003"].select = True
   bpy.data.objects["Plane.003"].location.x += -0.2
   bpy.data.objects["Plane.002"].location.x += 0.2
   print(bpy.data.objects.get("Cube").location)
   print(scene.objects["Plane.003"].location)


if __name__ == "__main__":
   del_existing()
   bpy.ops.mesh.primitive_plane_add(location = (0,0,0))
   bpy.data.objects["Plane"].select = True
   bpy.ops.rigidbody.object_add()
   selobj = bpy.context.active_object
   selobj.scale = (8,8,0)
   plane_mat = makeMaterial('planemat', (0.8,0.8,0.8), (0.5,0.5,0), 1)
   plane_mat2 = makeMaterial('planemat2', (0.6,0.0,0.0), (0.5,0.5,0), 1)
   plane_mat3 = makeMaterial('planemat3', (0.0,0.5,0.0), (0.5,0.5,0), 1)
   plane_mat4 = makeMaterial('planemat4', (0.0,0.0,0.5), (0.5,0.5,0), 1)
   setMaterial(bpy.context.object, plane_mat)
   bpy.ops.mesh.primitive_plane_add(location = (-8,-8,0))
   bpy.data.objects["Plane.001"].select = True
   bpy.ops.transform.rotate(value=m.radians(90),axis=(1,0,0))
   bpy.ops.transform.resize(value=(8,8,5))
   bpy.ops.transform.translate(value=(8,0,5))
   setMaterial(bpy.context.object, plane_mat2)
   bpy.ops.mesh.primitive_plane_add(location = (-8,-8,0))
   bpy.data.objects["Plane.002"].select = True
   bpy.ops.transform.rotate(value=m.radians(90),axis=(0,1,0))
   bpy.ops.transform.resize(value=(8,8,5))
   bpy.ops.transform.translate(value=(0,8,5))
   setMaterial(bpy.context.object, plane_mat3)
   bpy.ops.mesh.primitive_plane_add(location = (8,-8,0))
   bpy.data.objects["Plane.003"].select = True
   bpy.ops.transform.rotate(value=m.radians(90),axis=(0,1,0))
   bpy.ops.transform.resize(value=(8,8,5))
   bpy.ops.transform.translate(value=(0,8,5))
   setMaterial(bpy.context.object, plane_mat4)
   #selobj.rotate = (1,0,0)
   bpy.ops.mesh.primitive_plane_add(location = (0,0,10))
   selobj = bpy.context.active_object
   selobj.scale = (8,8,0)
   bpy.ops.mesh.primitive_cube_add(location = (2.5,0,1))
   bpy.data.objects["Cube"].select = True
   print('Cube',bpy.ops.rigidbody.object_add())
   selobj = bpy.context.active_object
   selobj.scale = (1,1,1)
   #print(bpy.context.object)
   #selobj.translate = (0,0,0)
   blue = makeMaterial('transcube', (0.16,0.05,0.8), (0.5,0.5,0), 2)
   setMaterial(bpy.context.object, blue)
   bpy.data.materials["transcube"].use_transparency = True
   bpy.data.materials["transcube"].transparency_method = 'RAYTRACE'
   bpy.data.materials["transcube"].raytrace_transparency.ior = 1.5
   bpy.data.materials["transcube"].alpha = 0.2
   #bpy.data.objects['Cube'].active_material = bpy.data.materials["transcube"]
   #print(bpy.data.materials["transcube"].use_transparency)
   bpy.ops.mesh.primitive_ico_sphere_add(location = (-4.3,3,1))
   bpy.data.objects["Icosphere"].select = True
   bpy.ops.rigidbody.object_add()
   bpy.ops.transform.resize(value=(1,1,1))
   bpy.data.objects['Icosphere'].active_material  = bpy.data.materials["transcube"]
   bpy.ops.object.modifier_add(type='SUBSURF')
   bpy.context.object.modifiers["Subsurf"].levels = 4
   bpy.ops.object.modifier_apply(apply_as='DATA',modifier='Subsurf')
   for obj in bpy.data.objects:
       for each in obj.data.polygons:
           each.use_smooth = 1
   #obj = bpy.context.active_object
   add_lamp("hemi","HEMI", (0,0,9.9))
   add_camera()
   bpy.context.scene.use_gravity = False
   bpy.context.scene.frame_end = 150

   # every frame change, this function is called.
   while len(bpy.app.handlers.frame_change_pre) > 0:
       bpy.app.handlers.frame_change_pre.pop()
   bpy.app.handlers.frame_change_pre.append(my_handler)