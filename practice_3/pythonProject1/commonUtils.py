class CommonUtils:

    @staticmethod
    def translit_to_eng(s):
        s = s.lower()
        rus_to_eng = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
                      'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
                      'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
                      'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                      'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
                      'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'i', 'ь': '',
                      'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '-'}
        s_eng = ''

        for x in s:
            s_eng += rus_to_eng.get(x)

        return s_eng


    @staticmethod
    def save_to_file(filename, listt):
        f = open(filename, 'w')
        for x in listt:
            f.write(x + '\n')
        f.close()

