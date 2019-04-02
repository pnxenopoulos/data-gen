import numpy as np

def generateData(n = 1000, classes = 2, features = 2):
	''' This is a function to generate data that follows an attributable pattern
	@param n Integer: The number of samples to generate
	@param classes Integer: The number of classes to generate
	@param features Integer: The number of features to generate
	'''
	# start errors
	# end errors
	data = np.empty((n, features + 1))
	start = 0
	stop = 1
	class_labels = np.array([])
	for f in np.arange(0, features):
		samples_per_feature = int(n/features)
		samples_per_class = int(samples_per_feature/classes)
		sampled_data = np.array([])
		for c in np.arange(0, classes):
			sampled_data = np.append(sampled_data, np.random.uniform(stop - 1, stop, samples_per_class))
			class_labels = np.append(class_labels, np.repeat(c, samples_per_class))
			stop = stop + 1
		sampled_data = np.append(sampled_data, np.random.uniform(start, stop, n - samples_per_feature))
		start = stop - 1
		data[:,f] = sampled_data
	data[:,features] = class_labels
	return data