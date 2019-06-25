#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# sid.djilali-saiah@epitech.eu

import sys
from Wallet import Wallet


class Bot:

    def __init__(self):
        self.wallet = Wallet()
        self.analyzer = 0
        self.buyRequests = []
        self.sellRequests = []
        self.file = open(".bot.log", "w+")
        self.file.truncate()

    def __writeLog__(self, str):
        self.file.write("--> " + str)

    def __generateBuyRequest__(self, nb, marketplace):
        request = "BUY:" + str(nb) + ":" + marketplace + "\n"
        self.__writeLog__(request)
        self.buyRequests.append(request)

    def __generateSellRequest__(self, nb, marketplace):
        request = "SELL:" + str(nb) + ":" + marketplace + "\n"
        self.__writeLog__(request)
        self.sellRequests.append(request)

    def __endRequest__(self):
        self.__writeLog__("EXIT\n")
        sys.stdout.write("EXIT\n")
        sys.stdout.flush()

    def __checkResource__(self, nb, marketplace):
        if marketplace == "crypto" and nb <= self.wallet.crypto:
            return True
        elif marketplace == "forex" and nb <= self.wallet.forex:
            return True
        elif marketplace == "raw_material" and nb <= self.wallet.raw_material:
            return True
        elif marketplace == "stock_exchange" and nb <= self.wallet.stock_exchange:
            return True
        else:
            return False

    def __checkCurrentMoney__(self, nb):
        if nb <= self.wallet.current_money:
            return True
        else:
            return False

    def __fillSellRequests__(self):
        pass

    def __fillBuyRequests__(self):
        self.__generateBuyRequest__(100, "forex")

    def __sendRequests__(self, status):
        if status is "sell":
            for request in self.sellRequests:
                sys.stdout.write(request)
                sys.stdout.flush()
                self.sellRequests.remove(request)
        elif "buy":
            for request in self.buyRequests:
                sys.stdout.write(request)
                sys.stdout.flush()
                self.buyRequests.remove(request)

    def run(self):
        self.wallet.update()
        self.__fillBuyRequests__()
        self.wallet.update()
        self.__sendRequests__("buy")
        self.__endRequest__()
        """self.wallet.forex = 5
        if self.wallet.forex > 0:
            self.__generateBuyRequest__(str(self.wallet.forex), "forex")
        self.wallet.crypto = 1
        if self.__checkResource__(self.wallet.crypto, "crypto") is True:
            self.__generateSellRequest__(str(self.wallet.crypto), "crypto")
        self.__sendRequests__("sell")
        self.__sendRequests__("buy")"""
