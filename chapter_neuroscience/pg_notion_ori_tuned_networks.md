# Population Coding with Tuned Neurons

This page explains one central idea in systems neuroscience: a stimulus is often represented not by one neuron, but by the activity of a population of tuned neurons. Here we focus on orientation, since it is easy to visualize, easy to code, and closely tied to many classic ideas in visual neuroscience.

:::{note} Big Idea: Populations Encode Stimuli

- The visual system contains neurons tuned to different stimulus features.
- A single neuron is not enough to identify the stimulus.
- The useful signal is the pattern of activity across the population.
- Perception depends on which groups of neurons are relatively more active.
:::

# Conceptual Overview

Many mammals have visual neurons that are tuned to the orientation of elongated stimuli. These neurons respond when features such as bars, edges, or gratings appear in the visual field. A single neuron, however, is not enough to specify the stimulus. The key idea is that orientation is represented by the pattern of activity across many neurons at once. When there is no strong oriented stimulus, the population remains relatively balanced. But when an oriented stimulus is shown, neurons that prefer that orientation respond more strongly than others, creating an imbalanced population response. In this simple picture, the visual system can infer the stimulus orientation from that pattern across the population.

 
The next figure makes this idea concrete in two steps: first, the tuning curves of individual cells; second, the population response produced when a single oriented stimulus is shown.
```{figure} ../assets/population_tuning_curves_classical.png
:width: 620px
:align: center

Panel A shows how individual neurons differ from one another: each has its own preferred orientation and tuning curve. Panel B then shows the key idea of population coding: once a single stimulus is presented, the full population produces a structured response pattern. 

```

The coding exercise below recreates this figure step by step. First, we build the tuning curves of individual orientation-tuned cells. Then we use those cells together as a population and ask how the full network responds to one stimulus orientation.

---
# Coding Exercise: Orientation-Tuned Population

## The Bell-Shaped Tuning Curve

A tuning curve is a stimulus-response function. Here, we will use the simplest version: a bell-shaped curve, also known as a Gaussian. Using a Gaussian is not the only way to describe an orientation tuning curve, and it may not be the "best" biological model (see Swindale 1998). We use it here because it is simple and easy to code. The shape of a neurons tuning curve can be characterized by two properties: its center and its spread....

* The center: The neuron responds most strongly to its preferred stimulus, so the center of the Gaussian is placed at the neuron's preferred orientation.
* The spread: A neuron also responds to orientations near its preferred orientation. The spread of the Gaussian tells us how far from the preferred orientation a stimulus can be and still elicit a response. 

## Build the Tuning Curve Network

We will create a population of visual neurons. Each neuron will have a Gaussian-shaped tuning curve. Different cells will have different orientation preferences, so the Gaussians will have different centers. All cells will have the same tuning width. Here, we set the spread of all neurons 15 degrees. This means a neuron responds mostly to orientations within about +/- 15 degrees of its preferred orientation.

```python
# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Creating the tuning function
def normal_dist(ori_vals, center, spread):
    Y = np.exp(-0.5 * ((ori_vals - center) / spread) ** 2)
    return Y

# 15 neurons with different orientation preferences
# that evenly span all orientations from 1 to 180 degrees
num_cells = 15
ori_vals = np.arange(0, 180, 10)
ori_pref_list = np.linspace(1, 180, num_cells)

# all curves have a spread/width of 15
tun_curve_width = 15
data = []
for k, n in enumerate(ori_pref_list):
  response = normal_dist(ori_vals, n, tun_curve_width)
  data.append(dict(zip(ori_vals, response)))

df = pd.DataFrame(data)

# display dataframe as a heatmap
df.style.background_gradient(cmap='viridis')\
.set_properties(**{'font-size': '5px'})
```


```{figure} ../assets/tuningpop_heatmap.png
:width: 620px
:align: center

There are 15 rows, one for each neuron. There are 18 columns, one for each stimulus orientation. The color tells us how strongly each neuron responds to each orientation.
```

Let us now slow down and look at one neuron at a time. We begin by plotting the tuning curve of a single cell, which is simply a horizontal slice through the heat map above.

```python
# plot the horizontal slice
cell_id = 10
df.iloc[cell_id].plot()
plt.xlabel('Stimulus Orientation')
plt.ylabel('Neuron Response')
```

```{figure} ../assets/tuningpop_singlecellcurve9.png
:width: 560px
:align: center

Single-cell tuning curve.
```
The x-axis is stimulus orientation. The y-axis is in arbitrary units, where 1 means the neuron is responding at its maximum. The maximum response occurs when the stimulus is tilted at about 120 degrees, so this cell has an orientation preference near 120 degrees.

Now plot the curves of all the neurons:


```python
for k, n in enumerate(ori_pref_list):
  df.iloc[k].plot()

plt.xlabel('Stimulus Orientation')
plt.ylabel('Neuron Response')
```

```{figure} ../assets/tuningpop_tuningcurveset.png
:width: 560px
:align: center

Population of tuning curves.
```
Each curve describes how one cell responds to different stimulus orientations. The population has orientation preferences that span the full range from 1 to 180 degrees.

## Population Response to One Stimulus

We now move from the single-cell view back to the population view. To see how the full network responds to one stimulus, we take a vertical slice of the heat map, corresponding here to a stimulus orientation of 90 degrees.

```python
# plot the vertical slice
stim_orientation = 90
df[stim_orientation].plot()

plt.xlabel('Neuron ID')
plt.ylabel('Neuronal Response')
```

```{figure} ../assets/tuningpop_popResponseCode.png
:width: 500px
:align: center

Population response to a 90-degree stimulus.
```

The x-axis is the neuron ID. The y-axis is in arbitrary units, where 1 means the neuron is responding at its maximum.

Some neurons respond strongly to the 90-degree stimulus, especially the neuron with an orientation preference near 90 degrees. Other neurons are relatively silent, such as neurons that prefer orientations far from 90 degrees.

The population response is also bell-shaped. In other words, the response of the whole population has a similar shape to the tuning curve of an individual cell.

# Why This Matters

This is why population coding matters. The exercise is simple, but the same logic appears throughout visual neuroscience: perception depends on the relative activity of neural populations. That idea helps explain the motion aftereffect, where adaptation changes the balance of motion-tuned cells, and the tilt illusion, where surrounding context may shift the activity of orientation-tuned cells.