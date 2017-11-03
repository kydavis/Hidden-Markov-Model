from HiddenMarkovModel import HiddenMarkovModel as HMM

"""
	Basic Test of HMM with coin flip

	States:
		Fair: Coin has two sides
		Loaded: Coin is double headed
	
	Emisssions:
		H: Heads
		T: Tails
"""

start = {'Fair' : 0.9, 'Loaded' : 0.1}
states = {'Fair', 'Loaded'}
trans = {
			'Fair' : {'Fair' : 1.0, 'Loaded' : 0.0},
			'Loaded' : {'Fair' : 0.0, 'Loaded' : 1.0}}

emissions = {
				'Fair' : {'H' : 0.5, 'T' : 0.5},
				'Loaded' : {'H' : 1.0, 'T' : 0.0}}

coin = HMM(start, states, trans, emissions)
print("Very Fair coin:{}".format(coin.viterbi("HHTHHTTHTHT")))
print("Loaded coin:{}".format(coin.viterbi("HHHHHHHHHHH")))
print("Odd coin:{}".format(coin.viterbi("HHHHHHHHHHHHHHT")))

print("Heads in a row:")
heads = "H"
for i in range(1, 11):
	print("{}:{}".format(i, coin.viterbi(heads)))
	heads = heads + "H"
