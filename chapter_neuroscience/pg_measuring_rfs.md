# Measuring Receptive Fields

_How do we actually measure what a visual neuron is tuned to?_

A key property of neurons in primary visual cortex is that they have spatially local receptive fields and are tuned to features such as orientation. On this page, I show the basic workflow I used to measure orientation tuning and ON/OFF receptive fields in mouse V1: present visual stimuli, record neural activity, and estimate receptive field structure from the responses.

# Stimulation and recording
The first step is to present visual stimuli while recording activity from neurons in visual cortex. The basic flow is simple: set up the experiment, present the stimuli, and track how the cells respond. Different stimulus sets are used for different measurement goals: gratings are useful for estimating orientation and spatial frequency tuning, while "sparse noise" is useful for mapping the ON and OFF structure of a receptive field.


```{figure} ../assets/jimenez2018_fig1a.png 

Setup for two-photon imaging of primary visual cortex in alert, head-fixed mice.
```
Here is an example experiment where we perform 2-photon imaging in an awake behaving mouse. A cranial window is implanted over the primary visual cortex (area V1). Mice are head-restrained but otherwise free to walk, rest, or groom on a spherical treadmill. Eye movements and locomotion are monitored by cameras synchronized to the microscope.

```{figure} ../assets/jimenez2018_fig1b.png
:width: 620px
:align: center


```
Here are the two stimulus sets used to measure receptive fields. Top row: pseudo-random sequences of full-field sinusoidal gratings used to estimate tuning for orientation and spatial frequency. The orientation domain can be sampled in equal steps of 10° for a total of 18 possible orientations; the spatial frequency domain can be sampled in equal steps on a logarithmic scale from 0.0079 to 0.1549 cycles/°, for a total of 12 possible spatial frequencies; and for each combination of orientation and spatial frequency, spatial phase can be sampled in steps of 45°, leading to 8 possible phase settings. Bottom row: sparse noise stimuli, consisting of randomly flashed bright and dark spots, used to map the ON and OFF subregions of each cell.

```{figure} ../assets/method_gratings.mp4
:width: 150px
:align: center

```

<iframe width="100%" height="420"
  src="https://www.youtube.com/embed/G5LpOtZsUtg"
  title="Motion aftereffect video"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  allowfullscreen
  >

</iframe>

/

Once these stimuli are ready, the next step is to present them while simultaneously recording activity from populations of neurons in V1. The figure here shows an example recording during visual stimulation: fluorescence signals from example cells are tracked over time while the mouse remains head-fixed on the spherical treadmill, with locomotion and eye state monitored in parallel. These recordings provide the response time series that are later used to estimate tuning kernels and ON/OFF receptive field maps.

# Estimating receptive fields

Once the stimuli have been presented and the responses recorded, the next step is to estimate the receptive field structure of each cell. For orientation and spatial frequency tuning, this means fitting a linear model between the neuron’s response and the grating stimulus sequence [@ringach_spatialclustering_2016]. The result is a tuning kernel in orientation × spatial frequency space.

A similar idea is used to estimate ON and OFF maps. Here, the model relates the neuron’s response to the location of bright and dark spot stimuli. The resulting maps are then smoothed with a Gaussian window of σ = 5°, which tends to produce smooth kernels and is also close to the diameter of a typical receptive field in mouse V1.

For each cell, we then choose the optimal time delay between stimulus and response. For tuning kernels, the optimal delay is the one at which the kernel variance reaches its maximum. A tuning kernel is treated as significant if its peak variance is roughly two times baseline, measured at negative time lags where the response should not depend on stimulus orientation. For ON and OFF maps, the optimal delay is chosen as the one at which map kurtosis reaches its maximum. In practice, I usually treat a map as significant when its peak kurtosis is greater than 8.


## Orientation X Spatial Frequency Tuning Kernel Examples

```{figure} ../assets/jimenez2018_fig1c.png
:width: 620px
:align: center


```
Here are two examples of tuning kernels in orientation × spatial frequency space. The kernels are normalized and shown in arbitrary units. From each kernel, we can estimate the cell’s preferred orientation by taking a horizontal slice, and its preferred spatial frequency by taking a vertical slice. We can also compare tuning kernels across pairs of cells.

## Examples of ON and OFF Maps of Mouse V1 neurons 

```{figure} ../assets/jimenez2018_fig1d.png
:width: 620px
:align: center

```
These are two examples of ON and OFF maps from mouse V1 neurons. Each cell has one ON map and one OFF map. The maps are normalized and shown in arbitrary units, and their dimensions correspond to positions in visual space on the stimulus screen. These maps can also be compared across cells.

# Manual detection of “significant” ON/OFF maps


<iframe width="100%" height="420"
  src="https://www.youtube.com/embed/OfaunAGLLGw"
  title="Motion aftereffect video"
  frameborder="4"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  allowfullscreen>

</iframe>

\

Typically we consider a receptive field map significant if its peak kurtosis is high. However, this method isn’t perfect, so I also like to manually go through all the maps and look for the ones with good structure. Here, the upper left plot shows a neuron’s kernel (here they are only spatial receptive field maps). The bottom left shows the location of segmented cells in the imaging plane. The bottom center and bottom right plots show the kurtosis and variance of receptive field maps at each time lag, respectively. Note how these spread-based measures are plotted across time lags, and for a "good" neuron they tend to rise and fall (rather than stay flat), and show clear peak at the lag where the receptive field is best expressed.