import tensorflow as tf
print(tf.version) # 2.6.0
# Create a tensor
string = tf.Variable('this is a string', tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)
#Rank/Degree of Tensors
rank1_tensor = tf.Variable(['Test'], tf.string)
rank2_tensor = tf.Variable([['test', 'ok'], ['test', 'yes']], tf.string)
tf.rank(rank2_tensor) #Determine the rank of a tensor
#Shape of Tensors
rank2_tensor.shape #Determine the shape of a tensor
#Changing Shape
tensor1 = tf.ones([1,2,3]) # tf.ones() creates a shape [1,2,3] tensor full of ones
tensor2 = tf.reshape(tensor1, [2,3,1]) # reshape existing data to shape [2,3,1]
tensor3 = tf.reshape(tensor2, [3, -1]) # -1 tells the tensor to calculate the size of the dimension in that place
                                        # This will reshape the tensor to [3,3]
#The number of elements in the reshaped tensor MUST match the number in the original
print(tensor1,tensor2,tensor3)
#Slicing Tensors
#Creating a 2D tensor
matrix = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20]]
tensor = tf.Variable(matrix, dtype=tf.int32)
print(tf.rank(tensor))
print(tensor.shape)
#Now lets select some different rows and columns from our tensor
three = tensor[0,2]  # selects the 3rd element from the 1st row
print(three)  # -> 3
row1 = tensor[0]  # selects the first row   
print(row1)
column1 = tensor[:, 0]  # selects the first column
print(column1)
row_2_and_4 = tensor[1::2]  # selects second and fourth row
print(row_2_and_4)
column_1_in_row_2_and_3 = tensor[1:3, 0]
print(column_1_in_row_2_and_3)
#Types of Tensors
#Variable
#Constant
#Placeholder
#SparseTensor
