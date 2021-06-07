This folder is basic NBC without any operations. The program just use training data as input and use NBC as model to run test data file and to classify trip types.

Raw data file: data.csv

Firstly, run: python3 split_and_select.py
It separates data to training data-set and test data-set.

Then, run: python3 basic_NBC.py
It will return training accuracy based on training data-set and testing accuracy based on test data-set.


###########
Here is the running output:
Training Accuracy: 0.64
Testing Accuracy: 0.58