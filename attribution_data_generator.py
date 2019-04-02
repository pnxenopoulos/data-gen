import numpy as np

def generateData(n = 1000, classes = 2, features = 2):
	''' This is a function to generate data that follows an attributable pattern
	@param n Integer: The number of samples to generate
	@param classes Integer: The number of classes to generate
	@param features Integer: The number of features to generate
	'''
	# start errors
	# end errors
	data = np.empty((n, features + 2))
	class_labels = np.random.choice(np.arange(0, classes), n)
	feature_important = np.random.choice(np.arange(0, features), n)
	data[:, data.shape[1] - 2] = class_labels
	data[:, data.shape[1] - 1] = feature_important
	for s in np.arange(0, n):
		current_class = class_labels[s]
		current_feature = feature_important[s]
		low = 2 * current_feature + current_class
		high = low + 1
		max_low = 2 * current_feature
		max_high = max_low + classes
		data[s, current_feature] = np.random.uniform(low, high, 1)
		data[s, np.delete(np.arange(data.shape[1]-2), current_feature)] = np.random.uniform(max_low, max_high, features - 1)
	return data
