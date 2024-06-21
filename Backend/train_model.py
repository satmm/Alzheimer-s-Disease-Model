import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.transform import resize
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import InputLayer, BatchNormalization, Dropout, Flatten, Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.applications.densenet import DenseNet169
from tensorflow.keras.optimizers import Adam
import os

# Data Augmentation
train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=30,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   vertical_flip=True,
                                   validation_split=0.2)

valid_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
test_datagen = ImageDataGenerator(rescale=1./255)

# Update the paths to point to the correct directories
train_directory = 'Alzheimer_s Dataset/train'
test_directory = 'Alzheimer_s Dataset/test'

train_dataset = train_datagen.flow_from_directory(directory=train_directory,
                                                  target_size=(224, 224),
                                                  class_mode='categorical',
                                                  subset='training',
                                                  batch_size=128)

valid_dataset = valid_datagen.flow_from_directory(directory=train_directory,
                                                  target_size=(224, 224),
                                                  class_mode='categorical',
                                                  subset='validation',
                                                  batch_size=128)

# Model Initialization
base_model = DenseNet169(input_shape=(224, 224, 3), include_top=False, weights="imagenet")

# Freezing Layers
for layer in base_model.layers:
    layer.trainable = False

# Building Model
model = Sequential()
model.add(base_model)
model.add(Dropout(0.5))
model.add(Flatten())
model.add(BatchNormalization())
model.add(Dense(2048, kernel_initializer='he_uniform'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1024, kernel_initializer='he_uniform'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))

# Summary
model.summary()

# Model Compile
OPT = Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=OPT)

# Defining Callbacks
filepath = './best_weights.keras'
earlystopping = EarlyStopping(monitor='val_accuracy', mode='max', patience=15, verbose=1)
checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', mode='max', save_best_only=True, verbose=1)

callback_list = [earlystopping, checkpoint]

# Model Training
model_history = model.fit(train_dataset,
                          validation_data=valid_dataset,
                          epochs=500,
                          callbacks=callback_list,
                          verbose=1)

# Save the model
model.save('alzheimers_model.keras')


