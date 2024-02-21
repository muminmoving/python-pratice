import json

from data_define import Record


class File_reader:
    def reader(self) -> list[Record]:
        pass


class Text_filereader(File_reader):
    def __init__(self, path):
        self.path = path

    def reader(self) -> list[Record]:
        i = open(self.path, "r", encoding="UTF-8")
        data = i.readlines()
        list1 = []
        for j in data:
            j = j.strip()
            j = j.split(",")
            record = Record(j[0], j[1], int(j[2]), j[3])
            list1.append(record)

        i.close
        return list1


class Json_filereader(File_reader):
    def __init__(self, path):
        self.path = path

    def reader(self) -> list[Record]:
        i = open(self.path, "r", encoding="UTF-8")
        list2: list[Record] = []
        for j in i.readlines():
            data_dict = json.loads(j)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            list2.append(record)

        i.close
        return list2


if __name__ == "__main__":
    test_filereader = Text_filereader("C:/Users/moving/Desktop/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt")
    i = test_filereader.reader()
    json_filereader = Json_filereader("C:/Users/moving/Desktop/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年2月销售数据JSON.txt")
    e = json_filereader.reader()
    for l in i:
        print(l)
    for l in e:
        print(l)