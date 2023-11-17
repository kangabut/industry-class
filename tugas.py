# x = [1,2,3,4]
# print("type")
# print(type(x))
# print("length of list")
# print(len(x))
# print("print list")
# print(x)
# print("iterate list")
# for i in x:
#     print(i)
# print("adding new velue")
# x.append("x")
# print(x)
# print("iterate list")
# for i in x:
#     print(i)


# x = {
#     "nama":"raditya",
#     "y":[1,2,3,4,5],
#     "alamat" : {
#         "kota":"Kota Depok",
#         "kec":"Sawangan"
#     }
# }
# print('print dict')
# print(x)
# print('print value dict')
# print(x['nama'])
# print(x['y'])
# print(x['alamat'])
# print(x["alamat"]['kota'])



x = [
    {
        "nama":"Khri",
        "y":[1,2,3,4,5],
        "alamat" : {
            "kota":"Kota Depok",
            "kec":"Bojongsari"
        }
    },{
        "nama":"RaditGaming773",
        "y":[1,2],
        "alamat": {
            "kota":"Kota Bogor",
            "kec":"Bogor"
        }
    }
]

for i in x:
    if len(i['y']) == 2 :
        print(i['nama'])
        print(i['alamat']['kota'])