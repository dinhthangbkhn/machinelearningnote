import tensorflow as tf 
import tensorflow_addons as tfa 
import tensorflow_datasets as tfds 
from tensorflow.keras.layers import Conv2D, Flatten, Dense
import io 
import numpy as np 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def _normalize_img(img, label):
    img = tf.cast(img, tf.float32) / 255.
    return (img, label)

train_dataset, test_dataset = tfds.load(name="mnist",
                                       split=['train', 'test'],
                                       as_supervised=True)
train_dataset = train_dataset.shuffle(1024).batch(32)
train_dataset = train_dataset.map(_normalize_img)

test_dataset = test_dataset.batch(32)
test_dataset = test_dataset.map(_normalize_img)


# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(filters=64, kernel_size=2, padding='same', activation='relu', input_shape=(28,28,1)),
#     tf.keras.layers.MaxPooling2D(pool_size=2),
#     tf.keras.layers.Dropout(0.3),
#     tf.keras.layers.Conv2D(filters=32, kernel_size=2, padding='same', activation='relu'),
#     tf.keras.layers.MaxPooling2D(pool_size=2),
#     tf.keras.layers.Dropout(0.3),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(256, activation=None), # No activation on final dense layer
#     tf.keras.layers.Lambda(lambda x: tf.math.l2_normalize(x, axis=1)) # L2 normalize embeddings

# ])

class MyModel(tf.keras.models.Model):
    def __init__(self) -> None:
        super(MyModel, self).__init__()
        self.conv1 = Conv2D(32, 3, activation="relu")
        self.flatten = Flatten()
        self.d1 = Dense(128, activation='relu')
        self.d2 = Dense(64, activation=None)
    
    def call(self, x):
        x = self.conv1(x)
        x = self.flatten(x)
        x = self.d1(x)
        x = self.d2(x)
        x = tf.math.l2_normalize(x, axis=1)
        return x 

loss_object = tfa.losses.TripletSemiHardLoss()
optimizer = tf.keras.optimizers.Adam()

# @tf.function turned the whole function into graph mode
# @tf.function 
def train_step(images, labels):
    with tf.GradientTape() as tape:
        predictions = model(images, training=True)
        loss = loss_object(labels, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss.numpy()

# @tf.function
def test_step(images, labels):
    # training=False is only needed if there are layers with different
    # behavior during training versus inference (e.g. Dropout).
    predictions = model(images, training=False)
    t_loss = loss_object(labels, predictions)
    return t_loss.numpy()

EPOCHS = 5
model = MyModel()
for epoch in range(EPOCHS):
    # Reset the metrics at the start of the next epoch
    #train_loss.reset_states()
    #train_accuracy.reset_states()
    #test_loss.reset_states()
    #test_accuracy.reset_states()
    train_loss_arr = []
    test_loss_arr = []
    for images, labels in train_dataset:
        train_loss = train_step(images, labels)
        train_loss_arr.append(train_loss)

    for test_images, test_labels in test_dataset:
        test_loss = test_step(test_images, test_labels)
        test_loss_arr.append(test_loss)

    print(
        f'Epoch {epoch + 1}, '
        f'Loss: {np.array(train_loss_arr).mean()}, '
        #f'Accuracy: {train_accuracy.result() * 100}, '
        f'Test Loss: {np.array(test_loss_arr).mean()}, '
        #f'Test Accuracy: {test_accuracy.result() * 100}'
    )