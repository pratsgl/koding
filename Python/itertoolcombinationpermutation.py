from itertools import *
price=['sell_lt_buy','sell_eq_buy','sell_gt_buy']
past_delivery=['del_gt_95','del_bw_85_95','del_lt_85']
past_read=['read_gt_95','read_bw_85_95','read_lt_85']
latency=['x','y','z']
runtime_status=['good','dead','degraded']
customer_profit=['higly profitable','profitable','marginal profit','loss making']
platform_profit=['higly profitable','profitable','marginal profit','loss making']

for i in product(price,past_delivery,past_read,latency,runtime_status):
    print(i)

for i in product(price,past_delivery):
    print(i)
