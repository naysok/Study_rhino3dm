import rhino3dm


model = rhino3dm.File3dm()


PATH = "./_3dm/00_write_3dm.3dm"

for i in range(5):

    ### Define Geometry
    pt = rhino3dm.Point(rhino3dm.Point3d(i, i, i))
    # print(pt)
    # print(type(pt))
    
    ### Define UserText
    pt.SetUserString("TEST_KEY", str(i))
    print(pt.GetUserStrings())

    model.Objects.Add(pt)
    # model.Objects.Add(pt, at)


### Check Attribute
t0 = model.Objects

for i, tt in enumerate(t0):
    
    if i != 0:
        print(tt)
        print(tt.Geometry)
        ttt = tt.Geometry
        print(ttt.GetUserStrings())


model.Write(PATH, 6)