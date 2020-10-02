#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Griffin Staples
Date Created: Fri Oct 02 2020
License:
The MIT License (MIT)
Copyright (c) 2020 Griffin Staples

"""


import sys
import os
import time

sys.path.append(os.path.abspath("./trading/"))

from TradeManager import TradeManager

def run_every(func,update_time):
    start_time = time.time()
    
    func() #call function
    
    curr_time = time.time()
    if(curr_time-start_time<update_time):
                time.sleep(update_time-(curr_time-start_time))



if __name__ == "__main__":
    update_time = 60 #seconds
    print("Starting Trading Algorithm")

    # Instantiate Trade Manager
    Manager = TradeManager(def_options={})
    
    # Add traders
    Manager.add_trader("MySimpleTrader", "ETH", "BKRW", "Simple Linear")
    Manager.add_trader("MyNetworkTrader", "ETH", "BKRW","Simple Network")

    while True:
        try:
            run_every(Manager.run_traders, update_time)

        except Exception as e:
            print(e.__class__, "occurred!")
        finally:
            print("shut down routine")
            break
