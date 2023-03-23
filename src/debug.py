import ipdb

from .jackpot import Gambler
from .jackpot import Dealer
from .jackpot import Bid

rex = Gambler("Rex")
dealer = Dealer("Chris")
bid_1 = Bid(rex, dealer, 300)





ipdb.set_trace()