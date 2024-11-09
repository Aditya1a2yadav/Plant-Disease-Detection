
# English to Hindi Translation Model

This repository contains a model that performs English-to-Hindi translation by fine-tuning a pre-trained Hugging Face model on a custom dataset. The process involves converting English audio to text using audio-to-text model and then translating the text into Hindi.

## Table of Contents

- [Overview](#overview)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Dependencies](#dependencies)
- [Training](#training)
- [Results](#results)

## Overview

This project aims to translate English phrases to Hindi by leveraging a combination of speech-to-text and machine translation models. The pipeline involves:
1. Converting English audio to text using the audio-to-text model.
2. Translating the resulting text from English to Hindi using a fine-tuned translation model.

## Model Details

- **Translation Model:** Fine-tuned on a 10K dataset of English-Hindi translation pairs using Hugging Face Transformers.
- **Speech-to-Text Model:** Facebook's Wav2Vec2 is used to transcribe English audio to text.
- **Framework:** TensorFlow & Hugging Face Transformers.

## Dataset

The translation model was fine-tuned on a dataset of 10,000 English-Hindi translation pairs. The dataset was pre-processed and tokenized using a custom tokenizer compatible with the Hugging Face model.

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.8+
- TensorFlow 2.4+
- Hugging Face Transformers
- torchaudio (audio-text-model)
- numpy
- pandas



## Training

The training process involved fine-tuning a pre-trained Hugging Face model on the English-Hindi translation dataset.

### Steps:
1. **Data Preprocessing:**
   - Tokenization of English and Hindi text pairs.
   
2. **Fine-Tuning:**
   - Fine-tune the translation model using the preprocessed dataset.

3. **Speech-to-Text:**
   - The Facebook's Wav2Vec2 model was employed to convert English audio into text.
   
4. **Inference:**
   - The fine-tuned translation model translates the transcribed English text into Hindi.


## Results

The fine-tuned model achieved satisfactory results, translating English text into accurate Hindi equivalents. The speech-to-text model also effectively converted English audio to text, making the entire pipeline robust for practical applications.


This README provides an overview of your project, details about the model and dataset, and instructions on how to use the model.
