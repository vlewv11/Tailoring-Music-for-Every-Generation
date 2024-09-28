Age-Based Music Recommendation System

Overview

This graduation assignment project features a system that predicts a user’s age based on their photo and recommends music tailored to that age group. The project uses a Convolutional Neural Network (CNN) model for age prediction and integrates with the Spotify API for music recommendations.

Components

1. CNN Model

The CNN model predicts the age of a user based on their photo. It employs several optimization techniques to enhance performance:

Dropouts: To prevent overfitting by randomly dropping units during training.

Batch Normalization: To normalize activations and gradients throughout training, improving convergence.

Data Augmentation: To artificially increase the diversity of the training dataset by applying transformations to the images.

The model achieves a Mean Absolute Error (MAE) of 6.32, indicating the average deviation of the predicted age from the actual age.

2. Flask Server
   
The server is built using Flask and includes three main pages:

Upload Photo: Users can upload their photos for age prediction.

Age Prediction Confirmation: Users can confirm the predicted age.

Music Recommendations: A list of recommended music tracks is displayed based on the predicted age.

3. Music Recommendation
   
Initial Music Tracks: 10 music tracks were created for each age group.

Spotify API Integration: The system uses the Spotify API to recommend and download additional music tracks based on the user’s age group. This allows for a dynamic and personalized music experience.

Project Structure

server.py: Main Flask application file.

static/: Directory for static files (CSS, JavaScript).

templates/: Directory for HTML templates.

model/: Directory containing the trained CNN model.

music/: Directory for storing initial and recommended music tracks.

data/: Directory for storing users' photo to retraing the model.
