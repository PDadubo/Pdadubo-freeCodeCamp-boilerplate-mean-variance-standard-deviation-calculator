import numpy as np

def calculate(list):
  if len(list) != 9: #The input of the function should be a list containing 9 digits and if not , it should raise a ValueError exception with the message: "List must contain nine numbers."
    raise ValueError("List must contain nine numbers.") 
  list = np.array(list).reshape(3,3) #elements in a 3 x 3 matrix.

  #uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns
  output = { 
    "mean": [np.mean(list, axis=0).tolist(), np.mean(list, axis=1).tolist(), np.mean(list)],
    "variance": [np.var(list, axis=0).tolist(), np.var(list, axis=1).tolist(), np.var(list)],
    "standard deviation": [np.std(list, axis=0).tolist(), np.std(list, axis=1).tolist(), np.std(list)],
    "max": [np.max(list, axis=0).tolist(), np.max(list, axis=1).tolist(), np.max(list)],
    "min": [np.min(list, axis=0).tolist(), np.min(list, axis=1).tolist(), np.min(list)],
    "sum": [np.sum(list, axis=0).tolist(), np.sum(list, axis=1).tolist(), np.sum(list)]
  }

  return output


    