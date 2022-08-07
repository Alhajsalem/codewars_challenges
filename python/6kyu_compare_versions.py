def compare_versions(version1,version2):

    def compare_versions(version1, version2):
    v1 = map(int, version1.split('.'))
    v2 = map(int, version2.split('.'))
    return list(v1) >= list(v2)
    #    return [int(n) for n in v1.split(".")] >= [int(n) for n in v2.split(".")]

    # v1_a = version1.split(".");
    # v2_a = version2.split(".");
   
    # if len(v1_a) < len(v2_a):
    #     print("cc")
    #     for ind,item in enumerate(v1_a):
    #         if item == v2_a[ind]:
    #             continue
    #         elif int(item) >= int(v2_a[ind]):
    #             return True
    #         else:
    #             return False
    #     return False

    # if len(v2_a) < len(v1_a):
    #     for ind,item in enumerate(v2_a):
    #         if item == v1_a[ind]:
    #             continue
    #         elif int(item) >= int(v1_a[ind]):
    #             return False
    #         else:
    #             return True
    #     return True

    # if len(v2_a) == len(v1_a):
    #     for ind,item in enumerate(v2_a):
    #         if int(item) == int(v1_a[ind]):
    #             continue
    #         elif int(item) >= int(v1_a[ind]):
    #             return False
    #         else:
    #             return True
    #     return True
print(compare_versions("10.4", "10.4.8")),