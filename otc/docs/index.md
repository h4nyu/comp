
| name                     | description                                                                                      |
| --------                 | ----------------                                                                                 |
| stock_id                 | ID of the stock.                                                                                 |
| date_id                  | ID of the date.                                                                                  |
| seconds_in_bucket        | The number of seconds from the day's closing auction                                             |
| imbalance_size?          | The amount (volume) that is unmatched at the current reference price.                            |
| imbalance_buy_sell_flag? |                                                                                                  |
| reference_price?         |                                                                                                  |
| matched_size?            |                                                                                                  |
| far_price?               |                                                                                                  |
| near_price?              |                                                                                                  |
| bid_price                | Most competitive buy price.                                                                      |
| ask_price                | Most competitive sell price.                                                                     |
| far_price?               |                                                                                                  |
| near_price?              |                                                                                                  |
| bid_size                 | Size of the most competitive buy order.                                                          |
| ask_size                 | Size of the most competitive sell order.                                                         |
| wap                      | Weighted average price. (bid_size * ask_price) +  (ask_size * bid_price) / (bid_size + ask_size) |
| target                   |



* Order book is a list of orders, each order is a tuple of (price, size, count). In japan, the order book is called 板.
