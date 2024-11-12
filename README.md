# Plant Disease Detection

This repository contains a model for detecting plant diseases by training on a large dataset of plant images. The project leverages both custom-built CNN architectures and fine-tuned pre-trained models to achieve high accuracy in classifying various plant diseases.

## Table of Contents

- [Overview](#overview)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Dependencies](#dependencies)
- [Training](#training)
- [Results](#results)

## Overview

This project focuses on detecting and recognizing plant diseases from images. The workflow involves training a model on a dataset of plant images, using both a custom CNN and pre-trained models to enhance performance. The best-performing model is then utilized for classifying diseases across 38 different classes.

## Model Details

- **Custom CNN Model:** Designed and trained from scratch to classify plant diseases with an accuracy of 88.2%.
- **Pre-trained Models:** Fine-tuned models like VGG16, ResNET50, DenseNET201, and InceptionV3 were used. The InceptionV3 model achieved the highest accuracy of 92.8%.
- **Framework:** TensorFlow & Keras were used for model development and training.

## Dataset

The model was trained on a dataset consisting of 50,000 images representing 38 different classes of plant diseases. The dataset was pre-processed and augmented to improve the robustness of the model.

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.8+
- TensorFlow 2.4+
- Keras
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Git LFS (for managing large files)

## Training

The training process involved fine-tuning a pre-trained Hugging Face model on the English-Hindi translation dataset.

### Steps:
1. **Data Preprocessing:**
   - Images were resized, normalized, and augmented to create a robust dataset.
   
2. **Custom CNN Training:**
   - A custom CNN model was trained from scratch on the pre-processed dataset.
     
3. **Pre-trained Model Fine-Tuning:**
   - Pre-trained models (VGG16, ResNET50, DenseNET201, InceptionV3) were fine-tuned on the dataset to enhance performance.
   
4. **Evaluation:**
   - The models were evaluated on the test set to determine their accuracy, with InceptionV3 achieving the highest accuracy.

## Results

- **Custom CNN Model:** Achieved an accuracy of 88.2%.
- **Best Pre-trained Model (InceptionV3)**: Achieved an accuracy of 92.8%.
- The model is capable of accurately classifying plant diseases across 38 classes, making it a valuable tool for agricultural diagnostics.
