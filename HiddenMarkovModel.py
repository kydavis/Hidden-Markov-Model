import math

"""
	Viterbi algorithm is used for Hidden Markov Models

	Parameters:
		start: initial probability state
		states: set of states
		trans: Transition probabilities between states
		emission: Emission probabilities from each state
		
		Example Parameters:

		start = {'H' : 0.5, 'L': 0.5}

		states = ('H', 'L')

		trans ={'L': {'H': 0.4, 'L': 0.6},
				'H': {'H': 0.5, 'L': 0.5}}

		emissions ={'H' : {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2},
					'L': {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}}

"""

class	HiddenMarkovModel:

	def __init__(self, start, states, trans, emission):
		self.start = _logMatrix(start)
		self.states = states
		self.trans = _logMatrix(trans)
		self.emissions = _logMatrix(emission)

	def __repr__(self):
		return ("Start:\n{}\n".format(_probMatrix(self.start)) +
				"States:\n{}\n".format(self.states) +
				"Transition Probabilities:\n{}\n".format(_probMatrix(self.trans)) +
				"Emission Probabilities:\n{}\n".format(_probMatrix(self.emissions)))

	"""
		viterbi will run the viterbi algorithm on a list of emissions and
			return the probability and sequence for the most probable
			sequence of states responsible for the emissions.

		Parameters:
			observations: list of observations
		Return:
			Probability of Viterbi path
			Most probable path of hidden states	
	"""
	def viterbi(self, observations):
		paths = self.__initState(observations[0])
		for obs in observations[1:]:
			paths = self.__nextState(paths, obs)
		maxProb = -float("inf")
		for path in paths:
			if (path["prob"] > maxProb):
				maxProb = path["prob"]
				maxPath = path["path"]
		return (2**maxProb, maxPath)

	"""
		__initState calculates the starting probabilities of each state given the
			first observation.
	"""
	def	__initState(self, obs):
		init= []
		for state in self.states:
			init.append({"path" : [state], "last" : state, 
						"prob" : self.start[state] + self.emissions[state][obs]})
		return (init)

	"""
		__nextState determines which path would be the best path for each of the
			new state transitions.
	"""
	def __nextState(self, paths, obs):
		ret = []
		for state in self.states:
			maxProb = -float("inf")
			maxPath = {"path" : []}
			for path in paths:
				pathProb = path["prob"] + self.trans[path["last"]][state]
				if (pathProb > maxProb):
					maxProb = pathProb
					maxPath = path
			ret.append({"path" : maxPath["path"] + [state],
						"last" : state,
						"prob" : self.emissions[state][obs] + maxProb})
		return (ret)

###############################################################################
#Helper Functions                                                             #
###############################################################################

"""
	_logMatrix takes the probability matrices given to the HMM and converts the
 probabilities into log format. This is done to prevent underflow of extremely
 small probabilities.
"""

def _logMatrix(matrix):
	ret = {}
	for row in matrix:
		if type(matrix[row]) is dict:
			ret[row] = {}
			for column in matrix[row]:
				ret[row][column] = -float("inf")
				if (matrix[row][column]):
					ret[row][column] = math.log(matrix[row][column], 2)
		elif type(matrix[row]) is float:
			ret[row] = -float("inf")
			if (matrix[row]):
				ret[row] = math.log(matrix[row], 2)
		else:
			raise TypeError("Values in start, trans, and emission " +
							"matrices must be dictionaries or floats")
	return (ret)

"""
	_probMatrix takes the log matrix in the HMM and converts the
 log probabilities into probability format. This is done for displaying
 the matrices inside the class.
"""
def _probMatrix(matrix):
	ret = {}
	for row in matrix:
		if type(matrix[row]) is dict:
			ret[row] = {}
			for column in matrix[row]:
				ret[row][column] = 0.0
				if (matrix[row][column] != -float("inf")):
					ret[row][column] = 2**matrix[row][column]
		elif type(matrix[row]) is float:
			ret[row] = 0.0
			if (matrix[row] != -float("inf")):
				ret[row] = 2**matrix[row]
		else:
			raise TypeError("Values in start, trans, and emission " +
							"matrices must be dictionaries or floats")
	return (ret)
