import tensorflow as tf
from sklearn.datasets import load_diabetes
dataset = load_diabetes()

#setting the data and labels
data = dataset.data
labels = dataset.target
# Parameters
learning_rate = 0.5
training_epochs = 100
batch_size = 200
display_step = 20
#AdadeltaOptimizer

# tf Graph Input
x = tf.placeholder(tf.float32, [None, 784]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax
correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
# Calculate accuracy
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Minimize error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
# Gradient Descent
optimizer = tf.train.AdadeltaOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)
    tf.summary.scalar('loss', cost)
    tf.summary.scalar('accuracy', accuracy)
    merged_summary = tf.summary.merge_all()
    summary_writer = tf.summary.FileWriter('./graphslogistic/loss', graph=tf.get_default_graph())

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(data.train.num_examples/batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = data.train.next_batch(batch_size)
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c,a, summary = sess.run([optimizer, cost,accuracy ,merged_summary], feed_dict={x: batch_xs,y:batch_ys})
            summary_writer.add_summary(summary,epoch* total_batch + i)
            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy:", accuracy.eval({x: data.test.images, y: data.test.labels}))