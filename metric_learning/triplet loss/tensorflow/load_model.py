import tensorflow as tf 
model = tf.keras.models.load_model('saved_model/entire_model')
model.summary()