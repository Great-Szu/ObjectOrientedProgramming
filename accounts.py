from datetime import datetime, timezone


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.now(timezone.utc)
        return utc_time

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance, balance)]
        print("account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            current_balance = self.__balance
            self._transaction_list.append((Account._current_time(), amount, current_balance))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            current_balance = self.__balance
            self._transaction_list.append((Account._current_time(), -amount, current_balance))
        else:
            print("The amount must be greater than 0 and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount, balance in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {}, balance after transaction: {}".format(amount, tran_type, date, date.astimezone(), balance))


if __name__ == '__main__':
    # tim = Account("Tim", 0)
    # tim.show_balance()
    #
    # tim.deposit(1000)
    # # tim.show_balance()
    # tim.withdraw(500)
    # # tim.show_balance()
    #
    # tim.withdraw(200)
    # tim.show_transactions()


    steph = Account("Steph", 880)
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)
