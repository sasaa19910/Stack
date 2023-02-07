class Stac:
    def __init__(self):
        self.my_stac = []
        self.open_list = ["[", "{", "("]
        self.close_list = ["]", "}", ")"]

    def main(self, element):
        for i in element:
            if i in self.open_list:
                self.my_stac.append(i)
            elif i in self.close_list:
                pos = self.close_list.index(i)
                if len(self.my_stac) > 0 and self.open_list[pos] == self.my_stac[-1]:
                    self.my_stac.pop()
                else:
                    return "Несбалансированно"
        if len(self.my_stac) == 0:
            return "Сбалансированно"
        else:
            return "Несбалансированно"








