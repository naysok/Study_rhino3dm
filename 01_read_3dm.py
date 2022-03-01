import rhino3dm


PATH = "./_3dm/00_write_3dm.3dm"

model = rhino3dm.File3dm().Read(PATH)

# print(model)
# print(model.Objects)
# print(model.Objects.Geometry)
# print(model.Attributes)


# print(len(model.Objects))

k0 = "TEST_KEY_0"
k1 = "TEST_KEY_1"


for i, obj in enumerate(model.Objects):
    # print(obj)
    # print(obj.Attributes)

    # print(obj.Geometry.Location)
    # print(obj.Attributes)
    print("---")

    print("POS : {}".format(obj.Geometry[0].Location))
    # print(obj.Geometry)

    
    print("{} : {}".format(k0, obj.Attributes.GetUserString(k0)))
    print("{} : {}".format(k1, obj.Attributes.GetUserString(k1)))


    
