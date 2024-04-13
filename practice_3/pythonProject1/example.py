class Phone(Devices):
    color = "red"

    def __init__(self):
        self.model = "new"
        self._size = 10  # protected
        self.__weight = 500  # private

    def turn_off(self, house="3"):
        pass


phone = Phone()
phone.model = 3
phone._size = 20
phone._Phone__weight = 1000
phone.turn_off()
