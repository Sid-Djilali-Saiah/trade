#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# sid.djilali-saiah@epitech.eu


class Wallet:

    def __init__(self):
        self.forex = 0
        self.crypto = 0
        self.raw_material = 0
        self.stock_exchange = 0
        self.current_money = 10000.0

    def update(self):
        i = 0
        filename = "../server/.server.log"
        with open(filename) as file:
            content = file.read().splitlines()
        while not content[i] == "marketplace;shares":
            content.remove(content[i])
            i += 1
        content.remove(content[i])
        while i != len(content):
            if content[i].split(';')[0] == "stock_exchange":
                self.stock_exchange = int(content[i].split(';')[1])
            elif content[i].split(';')[0] == "raw_material":
                self.raw_material = int(content[i].split(';')[1])
            elif content[i].split(';')[0] == "forex":
                self.forex = int(content[i].split(';')[1])
            elif content[i].split(';')[0] == "crypto":
                self.crypto = int(content[i].split(';')[1])
            elif content[i].split(';')[0] == "current_money":
                self.current_money = float(content[i].split(';')[1])
            i += 1

    def printWallet(self):
        print(self.stock_exchange)
        print(self.raw_material)
        print(self.forex)
        print(self.crypto)
        print(self.current_money)
