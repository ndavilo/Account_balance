
class Account:
    """
        In balancing your account,
        you simply supply lists of your debits and credits (deposits and withdrawals),
        and this function will add them up to determine your balance.

        deposits is a list of all the money paid into the account from a given period

        withdrawals is a list of all the money paid out of the account from a given period

    """

    def __init__(self, deposits, withdrawals):
        """_summary_

        Args:
            deposits (_type_): _description_
            withdrawals (_type_): _description_

        Returns:
            _type_: _description_
        """
        if type(deposits) == list and type(withdrawals) == list:
            self.deposits           = deposits
            self.withdrawals        = withdrawals
            self.total_deposit      = sum(deposits)
            self.total_withdrawal   = sum(withdrawals)
        else:
            return 'error! not a list'

    def balance(self):
        """_summary_

        Returns:
            _type_: float balance
        """
        self.balance = self.total_deposit - self.total_withdrawal
        return (self.balance)

    def correct_balance(self, supplied_balance):
        """
        To check if the currrent balance is correct
        supply the balance as float.

        Args:
            supplied_balance (_type_): float value

        Returns:
            _type_: boolean 
        """
        if supplied_balance == self.balance:
            return True
        else:
            return False
