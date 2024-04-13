class Human:
    default_name = "Ivan"
    default_age = 18

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__home = False

    def info(self):
        print("\n---------------PERSON---INFO---------------")
        print("Hello! My name is " + self.name + ".\nI'm " + str(self.age) + ".\nI have " + str(
            self.__money) + " money and i", "have" if self.__home else "have NO(", "home.")

    @staticmethod
    def default_info():
        print("\n---------------DEFAULT---INFO---------------")
        print("Name: ", Human.default_name)
        print("Age: ", Human.default_age)

    def __make_deal(self, house, price):
        self.__money -= price
        self.__home = house

    def earn(self):
        self.__money += 10

    def buy_house(self, house, sale):
        print("\n---------------U-R-TRYING-TO-BUY-THE-HOUSE---------------")
        final_price = house.final_price(sale)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            print("U HAVE THE HOUSE NOW")
        else:
            print("TOO POOR. NOT ENOUGH MONEY.\nU NEED ", final_price - self.__money, " MORE")


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        return self._price * ((100 - sale) / 100)


class SmallHouse(House):

    def __init__(self, price):
        super().__init__(40, price)


Human.default_info()
person1 = Human("Vova", 24)
person1.info()
small_house = SmallHouse(10)
person1.buy_house(small_house, 0)
person1.earn()
person1.buy_house(small_house, 20)
Human.default_info()
person1.info()
