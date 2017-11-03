from HiddenMarkovModel import HiddenMarkovModel as HMM

start = {'H' : 0.5, 'L': 0.5}
states = ('H', 'L')
trans =  {
			'L': {'H': 0.4, 'L': 0.6},
			'H': {'H': 0.5, 'L': 0.5}}
emissions =  {
			'H'	: {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2},
			'L': {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}}

vit = HMM(start, states, trans, emissions)
print(vit)
print(vit.viterbi("GGCACTGAA"))
