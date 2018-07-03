import tensorflow as tf
#define the matrices for a , b and c

a = tf.constant([0,4,3,5], name="matrix_a",shape=[2,2])
b = tf.constant([4,0,7,17], name="matrix_b",shape=[2,2])
c = tf.constant([0,1,6,8], name="matrix_c",shape=[2,2])

#Applying power operation for matrix a
x = tf.pow(a,2)

#Addition operation for x + b

y=tf.add(x,b)

#define the multiply operation for y * c
z=tf.multiply(y,c)


#create the session for evaluating tensor objects
with tf.Session() as s:

    #Prints pi
    print(s.run(x))
    #print (a*a+b)
    print(s.run(y))
    #print (a*a+b)*c
    print(s.run(z))