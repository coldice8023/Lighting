class User(object):
	def __init__(self, pref_illuminance, tolerance):
		self.pref_illuminance = pref_illuminance
		self.tolerance = tolerance

	def accept_prob(self, x):
		from numpy import exp
		from numpy import log
		return exp(-(log(x) - log(self.pref_illuminance)) ** 2 / (2 * self.tolerance ** 2))

	def get_feedback(self, x):
		from numpy import random
		acc_prob = self.accept_prob(x)
		rand_num = random.rand(1)
		return