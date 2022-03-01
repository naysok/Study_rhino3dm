import rhino3dm


model = rhino3dm.File3dm()
PATH = "./_3dm/00_write_3dm.3dm"


for i in range(5):

    ### Define Geometry
    pt = rhino3dm.Point3d(i, i, i)
    pc = rhino3dm.PointCloud([pt])
    # print(pt)
    # print(type(pt))


    ### Define UserText
    attr = rhino3dm.ObjectAttributes()
    attr.SetUserString("TEST_KEY_0", str(i))
    attr.SetUserString("TEST_KEY_1", "Hello World!!")


    ### Add Object
    model.Objects.AddPointCloud(pc, attr)



model.Write(PATH, 6)