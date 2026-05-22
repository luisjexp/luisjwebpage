# Decoding Engagement from Hand Motion in Short Writing Tasks

```{figure} assets/videoprocessing_lstmsiagram.png
(A) Overview of the video preprocessing and feature-extraction pipeline. (B) Two-layer LSTM regressor (128 hidden units per layer) mapping per-frame feature sequences to a single predicted engagement score.
```
``` {figure} assets/mask_example.gif

```
:::{note}
This project was carried out by my student Merey Kurmanova a 10th-grader under my mentorship. She carried out much of the work end-to-end: refining the research question, collecting video dataset, analysis and writing. 
:::

# Overview
This project examines whether a Long Short-Term Memory (LSTM) model can be used to predict engagement in real time from hand-movement patterns during writing tasks. The goal was to offer a privacy-preserving alternative to facial- and gaze-based engagement tracking, and to identify writing-related tasks that elicit engagement signals that are decodable from hand motion. The pages here contain high-level details and code covering experimental design, data collection, and parts of the modeling + analysis.

It is useful for students learning to integrate a set of connected ideas often encountered in neuroscientific research, from data preprocessing, to sequence modeling, to building a meaningful understanding of what a black-box model is actually using to make its predictions.

Specifically we'll cover the following...
- **Computer vision**: process video frames to isolate motion, track hand position, and extract movement features.
- **Recurrent neural networks for time series data**: use a 2-layer LSTM to map a sequence of movement features to a single engagement rating for each trial.
- **Behavior and interpretation**: relate model predictions to underlying movement features, so we can form a simple story about what patterns tend to align with higher vs lower engagement. I discuss the importance of this step at length [in this post](../chapter_approach/pg_02_approaches.md)


# Study Design
The dataset contains **24 videos from one participant**. \
Each trial lasted 10 seconds. The participant completed three kinds of tasks:
- **Copying tasks:** copy short text strings.
- **Creative tasks:** draw simple shapes or objects.
- **High-load tasks:** write short responses to open-ended prompts.

Each task was recorded under two conditions: \
- **Focused:** complete the task without a secondary task.
- **Dual-task:** complete the task while mentally counting backward by 3.

After each trial, the participant rated their engagement from 1 to 5.



# Pipeline/Methodology
The notebooks follow the main analysis pipeline: 
1. Standardize the manually edited videos.
2. Compute motion energy as a simple measure of frame-to-frame change.
3. Extract hand-position and motion features from each video.
4. Train an LSTM model to predict engagement from the time series.


```{figure} assets/task.jpg
:width: 500px
Research methodology
```