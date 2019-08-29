from csv import reader
from math import sqrt
from random import randrange

filePath = '/home/steven/Data/Iris/iris.desc'

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            # print(row)
            dataset.append(row)
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        # print('before: ' + row[column])
        row[column] = float(row[column].strip()) # strip empty spaces and force to float from string.
        # print('after: ' + str(row[column]))

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    # enumerate the unique string values present in this column and then assign them a integer value base on i.
    for i, value in enumerate(unique):
        lookup[value] = i
        # print(value)
    for row in dataset:
        row[column] = lookup[row[column]]
        # print(row[column])
    return lookup

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
	left, right = list(), list()
	for row in dataset:
		if row[index] < value:
			left.append(row)
		else:
			right.append(row)
	return left, right

# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
	# count all samples at split point
	n_instances = float(sum([len(group) for group in groups]))
	# sum weighted Gini index for each group
	gini = 0.0
	for group in groups:
		size = float(len(group))
		# avoid division by zero
		if size == 0:
			continue
		score = 0.0
		# score the group based on the score for each class
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			score += p * p
		# weight the group score by its relative size
		gini += (1.0 - score) * (size / n_instances)
	return gini

# Select the best split point for a dataset
def get_split(dataset, n_features):
	class_values = list(set(row[-1] for row in dataset))
	b_index, b_value, b_score, b_groups = 999, 999, 999, None
	features = list()
	while len(features) < n_features:
		index = randrange(len(dataset[0])-1)
		if index not in features:
			features.append(index)
	for index in features:
		for row in dataset:
			groups = test_split(index, row[index], dataset)
			gini = gini_index(groups, class_values)
			if gini < b_score:
				b_index, b_value, b_score, b_groups = index, row[index], gini, groups
	return {'index':b_index, 'value':b_value, 'groups':b_groups}

# load and prepare data
filename =  str(filePath)
dataset = load_csv(filename)

# convert string attributes to floating point values
for i in range(0, len(dataset[0])-1): # Convert string values in the .csv file to 
    str_column_to_float(dataset, i)

str_column_to_int(dataset, -1)
n_features = int(sqrt(len(dataset[0])-1))

output = get_split(dataset, n_features)
# print(output)
# print(len(output["groups"][0]))
# print('1')
# print(output["groups"][0])
# print('2')
# print(output["groups"][1])
# print('3')
# print(output["groups"][2])
