import click
import logging
import tensorflow as tf
from pathlib import Path
import os



def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """

    train_dir = os.path.join(input_filepath, 'training')
    test_dir = os.path.join(input_filepath, 'testing')

    BATCH_SIZE = 32
    IMG_SIZE = (160, 160)

    train_dataset = tf.keras.utils.image_dataset_from_directory(train_dir,
                                                            shuffle=True,
                                                            batch_size=BATCH_SIZE,
                                                            image_size=IMG_SIZE)
    test_dataset = tf.keras.utils.image_dataset_from_directory(test_dir,
                                                                 shuffle=True,
                                                                 batch_size=BATCH_SIZE,
                                                                 image_size=IMG_SIZE)
    class_names = train_dataset.class_names
    val_batches = tf.data.experimental.cardinality(train_dataset)

    validation_dataset = train_dataset.take(val_batches // 5)

    train_dataset = train_dataset.skip(val_batches // 5)

    AUTOTUNE = tf.data.AUTOTUNE

    train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
    validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)
    test_dataset = test_dataset.prefetch(buffer_size=AUTOTUNE)

    return (train_dataset, validation_dataset, test_dataset, class_names)

    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')