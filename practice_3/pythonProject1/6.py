class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg):
        if isinstance(kg, (int, float)):
            self.__kg = kg
        else:
            print("BAD DATA")


weight = KgToPounds(12)
print(weight.to_pounds())
print(weight.kg)
weight.kg = 41
print(weight.kg)
weight.kg = 'десять'
print(weight.kg)
