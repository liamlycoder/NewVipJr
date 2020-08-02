person1 = {"hobby1", "hobby2", "hobby3"}
person2 = {"hobby4", "hobby5", "hobby3"}
person3 = {"hobby4", "hobby5", "hobby6"}

list = [{"name":"A","hobby":person1},
        {"name":"B","hobby":person2},
        {"name":"C","hobby":person3}]

for i in range(len(list)-1):
        for j in range(len(list)):
                if list[i]["hobby"] & list[j]["hobby"]:
                        pass
                else:
                  print("{}和{}不会成为好朋友".format(list[i]["name"],list[j]["name"]))