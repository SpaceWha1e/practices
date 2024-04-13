import commonUtils


class SlugConverter:

    def __init__(self):
        print("Enter filename")
        self.__file_name = input()
        self.__slug_list = []

        print("Enter list, which ends with void string")
        self.run()

    def run(self):
        s = input()
        while s:
            self.__slug_list.append(commonUtils.CommonUtils.translit_to_eng(s))
            s = input()
        commonUtils.CommonUtils.save_to_file(self.__file_name, self.__slug_list)

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, f):
        self.__file_name = f

    @property
    def slug_list(self):
        return self.__slug_list

    @slug_list.setter
    def slug_list(self, listt):
        self.__slug_list = listt


