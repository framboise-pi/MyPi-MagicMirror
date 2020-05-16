#!/usr/bin/env python
#coding=utf-8

import random

## SETTINGS
module_words_font = ('System', 60)
interval = 10 * 1000

def RandomWords():
	name = (
		"Jeanne", 
		"Pierre", 
		"Le Monde",
		"Le chat",
		"La vie"
	)
	verb = (
		"sent",
		"mange",
		"est",
		"dit",
		"regarde") 
	adv = (
		"incroyablement",
		"brille",
		"aboniablement",
		"exactement",
		"mystérieusement"
		)
	adj = (
		"adorable.",
		"sexy.",
		"horrible.",
		"vieux.",
		"bête."
		)
	num = random.randrange(0,5)
	return name[num] + ' ' + verb[num] + ' ' + adv[num] + ' ' + adj[num]
