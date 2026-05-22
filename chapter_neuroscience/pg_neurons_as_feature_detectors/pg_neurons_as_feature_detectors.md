# Neurons as Feature Detectors

Visual neurons are often described as feature detectors. The basic idea is simple: some neurons respond strongly when a particular visual pattern appears in their receptive field.

In this page, we focus on edge-like features. The goal is to understand how a neuron can act like a filter: it receives a small region of an image, compares that region to a preferred pattern, and produces a response. We will build this idea step by step, moving from images, to receptive fields, to filters, and finally to feature detection itself.

:::{note} Main questions:

Main questions:

- Why would the visual system detect features?
- How can an image be treated as numbers?
- How can a neuron act like a filter?
- How can filtering detect whether a feature is present?
:::


## Why Detect Features?

The visual system should be sensitive to important structure in the world. In vision, edges are especially important. An edge is a sharp change in brightness, and such changes often correspond to object boundaries, such as the boundary between a laptop and the desk it sits on.

**Why this matters:**
- Animals need to detect objects: Objects guide action: reaching, avoiding, grabbing, tracking.
- Edges are information rich.[^1]

[^1]: There's lots say about the idea if information content. See [](https://psycnet.apa.org/doi/10.1037/h0054663) for a foundation.  

Object recognition is not the only goal of vision, but it is one of the central ones.

## Local Receptive Fields

A neuron does not analyze the whole image at once. Instead, it receives input from a limited region of visual space: its receptive field. This is the first key simplification. A neuron “sees” only a small part of the visual scene, not the entire image.

```{figure} 2018_williams_receptive_field_CNN.png
:width: 400px
:align: center

A neuron receives input from a small region of an image.
```

In this illustration, the pink/orange spheres represent neurons in visual cortex. The blue/green array represents an image projected onto the eye. One neuron receives input from a small image region, shown by the gray square.

So before we can talk about feature detection, we first have to isolate the local patch of image that the neuron is analyzing.

## Images as Matrices

To understand filtering, it helps to treat an image as a matrix of pixels.
* Each pixel has a luminance value.
* Larger values mean brighter pixels.

Once an image is written this way, it becomes possible to compare local image patches numerically. (For now, we can keep things simple and think only about black-and-white images.)

```{figure} Untitled.png
:width: 300px
:align: center

An image can be represented as a matrix.
```

```{figure} Untitled_1.png
:width: 300px
:align: center

Pixel values describe local brightness.
```

```{figure} Untitled_2.png
:width: 400px
:align: center

The same image can be described numerically.
```

**Try it**
- Find regions of sharp luminance change in an image.
- Ask: where are the edges? What local pixel pattern marks that edge?


## Neurons as Filters

We can now move from the image to the neuron. One useful way to think about a neuron’s receptive field is as a matrix of weights, or a _filter_. The filter describes what kind of image pattern the neuron is looking for. When the filter is compared to a local image region, it measures how well that region matches the preferred pattern. If the match is strong, the neuron responds more strongly.

```{figure} 2013_Pratt_orientedfilters_eg.png
:width: 600px
:align: center

4 Examples of oriented filters represented as a matrix of weights.
```

The numbers represent the strength and direction of the weights applied to pixels in an image region.


## Calculating Similarity with a Linear Combination
We now have the two ingredients we need:
* an image region, represented as pixel values
* a filter, represented as a matrix of weights


The next question is simple: how do we measure how well the image region matches the filter? One standard answer is a linear combination:
* Multiply each pixel value by the corresponding filter weight.
* Add the results.
* The final number is the filter response.

```{figure} 2016_pang_linfilters_detect_features_croppedoutcaption.png
:width: 360px
:align: center

Linear combination of image values and filter weights as a mechanism for feature detection. A filter gives a large response when the stimulus matches the pattern it is looking for. From Pang et al. 2016.
```
This figure shows the core idea: filtering a stimulus yields one number.

That number tells us how well the stimulus matches the filter.
A stimulus that matches a positive-deflection filter gives a positive response.
A stimulus that matches a negative-deflection filter gives a negative response.
A stimulus with balanced positive and negative deflections gives a response near zero.

In other words, the filter converts a local pattern into a response value. The example in the figure uses changes in luminance over time, but the same logic applies to spatial patterns in an image. Once we can compute that response at one location, the next step is to move the filter across the image and ask where it responds most strongly.

**Detecting Edge-like features**

A feature detector is useful only if it can be applied across many image locations. When we slide the filter across the image and repeatedly compute its response, some regions produce much larger values than others. Those are the locations where the image matches the filter best.

```{figure} output_of_contrast_enhanced_image.png
:width: 720px
:align: center

Output of a contrast-enhancement filter.
```
In this case, the filtered image emphasizes changes in brightness. In other words, it highlights edges. This particular mask is also similar in spirit to the on-center receptive fields discussed on the [retinal ganglion cell page](../pg_retina_cscells.ipynb), where positive weighting in one region and negative weighting in the surround makes the neuron especially sensitive to local contrast. That is why filters are useful models of feature detectors: they respond selectively when the right kind of structure is present.
## Summary

* Images can be treated as matrices of pixel values.
* A neuron’s receptive field can be treated as a filter.
* Filtering measures how well a local image region matches that filter.
* Stronger matches produce stronger neural responses.
* This gives us one useful way to understand neurons as feature detectors.

