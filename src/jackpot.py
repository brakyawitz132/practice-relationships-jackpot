class Gambler:

    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)
        self.bids = []
        Gambler.all.append(self) 

    def get_name(self):
        return self.name

    def get_bids(self):
        return [bid for bid in Bid.all if bid.gambler == self]

    def get_dealers(self):
        return [bid.dealer for bid in Bid.all if bid.gambler == self]

    def highest_bid(self):
        sorted_bid_amounts = sorted(self.get_bids(), key=lambda bid: bid.amount, reverse=True)
        return sorted_bid_amounts[0]

    def average_bid_amount(self):
        bid_amounts = [bid.amount for bid in self.get_bids()]
        return sum(bid_amounts) / len(bid_amounts)

    def has_bidded(self, dealer):
        if isinstance(dealer, Dealer):
            return dealer in [bid.dealer for bid in self.get_bids()]

    def make_bid(self, dealer, amount):
        if isinstance(dealer, Dealer) and type(amount) in (float,int,):
            new_bid = Bid(self, dealer, amount)
            self.bids.append(new_bid)
            dealer.bids.append(new_bid)

    @classmethod
    def highest_average_gambler(cls):
        sorted_all = sorted(cls.all, key=lambda gambler: gambler.average_bid_amount(), reverse=True)
        return sorted_all[0]
        # return max((bid for bid in set(bid.gambler for bid in Bid.all)), key=lambda x: x.average_bid_amount)

class Dealer:

    def __init__(self, name):
        self.name = name
        self.bids = []

    def get_name(self):
        return self.name

    def get_bids(self):
        return [bid for bid in Bid.all if bid.dealer == self]

    def get_gamblers(self):
        return [bid.gambler for bid in Bid.all if bid.dealer == self]



class Bid:

    all = []

    def __init__(self, gambler, dealer, amount):
       self.gambler = gambler
       self.dealer = dealer
       self.amount = amount 
       Bid.all.append(self)

    def get_amount(self):
        return self.amount

    def get_gambler(self):
        return self.gambler

    def get_dealer(self):
        return self.dealer
    