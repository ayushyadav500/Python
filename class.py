class Util:
    @staticmethod
    def is_valid_number (amount):
        try:
            if (float(amount))>0 :
                return True
            return False
        except:
            return False

class AccountUI:
    def get_input_for_deposit(self, amount):
        if (not is_valid_number(amount)):
            print("Amount should be greater than 0. Try again")
        else:
            print("Successfully deposited")