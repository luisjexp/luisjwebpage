# The Tilt Illusion


# What Do You See?

```{figure} ../assets/simultaneous_tilt_stimulus.png
:width: 460px
:align: center

Simultaneous tilt illusion.
```
The center grating is vertical. Yet, depending on the orientation of the surrounding grating, it can appear tilted. Our goal is to understand why this happens.

## Two Illusions in One

Below is a quantitative description of the tilt illusion (see Clifford 2014). This figure is especially useful because it shows that there are actually two effects here: a repulsive effect and an attractive effect.

In the figure, the y-axis shows the perceived tilt of the central grating, and the x-axis shows the orientation of the surround grating. Importantly, the central grating is always vertical. The only thing that changes is the tilt of the surround.

```{figure} ../assets/2014_clifford_fig1.png
:width: 760px
:align: center

Repulsive and attractive effects in the tilt illusion.
```
* **Repulsion**: When the surround is tilted by a small amount, the central grating appears tilted in the opposite direction. In that sense, the center and surround seem to push away from one another.
* **Attraction**: When the surround is tilted much farther away, the effect can reverse. The central grating then appears tilted toward the surround orientation.

So the tilt illusion is not just one illusion. It contains both a repulsive and an attractive component, depending on the angle of the surround. Our goal is to determine why this happens.

# Perceiving Object Orientation

Before introducing theories of the tilt illusion, we first need a simple picture of how the visual system represents orientation. We will do this by introducing two concepts: the response of individual cells to an oriented stimulus, and the population response of many cells to that stimulus.

```{figure} ../assets/population_tuning_curves_classical.png
:width: 420px
:align: center

A population of orientation-tuned neurons can represent stimulus orientation through its pattern of activity. When an oriented stimulus is presented, neurons that prefer that orientation respond more strongly than others, creating an imbalanced population response. This population-level activity can then be used to infer the orientation of the stimulus.
```


### Orientation-Tuned Cells

All known mammals have visual neurons that are tuned to the orientation of elongated stimuli. For example, when you look at a grating made of vertical bars, a particular set of neurons becomes active. Several key properties of these cells matter here:
1. Orientation-tuned neurons respond selectively to elongated stimuli, not just to any shape. 
2. These neurons also exhibit a baseline level of activity, even when no relevant stimulus is present.
3. Each unit has a preferred orientation: the orientation that drives it most strongly.
4. Although each unit has a preferred orientation, it also responds, more weakly, to nearby orientations. The farther the stimulus is from the preferred orientation, the weaker the response.

These properties are shown in figure A above.
```{figure} ../assets/orituned_cells_simulation.gif
:width: 200px
Also try this greate interactive simulation [here](https://www.macmillanlearning.com/studentresources/college/df/biology/life_11e/life_activity_46_02.html).
```

### Population tuning and imbalanced Networks
So how does the activity of these neurons allow us to perceive orientation?

When there are no elongated objects in view, orientation-tuned neurons remain relatively quiet, firing only at baseline rates. In this state, the system is roughly balanced: no one group of orientation-tuned neurons is strongly favored over another.

That changes when you view an oriented stimulus, such as a grating tilted at -45 degrees, as shown in panel B of the figure above. Neurons that prefer orientations near -45 degrees respond more strongly than the rest, while neurons tuned to other orientations respond less. The population is now imbalanced, with activity biased toward that -45 degree orientation. In this simple picture, perception depends on that imbalance: the visual system infers the stimulus orientation from the relative activity across the population.

:::{note} Summary
Two key ideas will matter for the rest of the discussion:

1. The visual system contains neurons tuned to many different orientations.
2. Orientation is represented by the relative activity of these neurons as a population.

:::
# Inhibition Theory

Can this population-based view explain the tilt illusion? One classical proposal is that inhibitory interactions between orientation-tuned populations are responsible. Blakemore and colleagues provided a simple and influential version of this idea:

```{figure} ../assets/1970_blakemore.png
:width: 300px
:align: center

From Blakemore et al. (1970). Their account proposes that inhibition between populations of orientation-tuned detectors gives rise to the apparent tilt in simultaneous tilt illusions.

```
Here is the proposed mechanism: a stimulus at one orientation activates a population of neurons tuned near that orientation. But those neurons do not respond in isolation; they can inhibit neighboring populations. If a second stimulus is added at a nearby orientation, the neurons responding to that second stimulus suppress part of the population responding to the first. Because this inhibition is not uniform across the population, the overall activity pattern shifts. That shifted pattern is then proposed to underlie the apparent change in perceived tilt.

## Limitation: Cannot Explain the Attraction Effect
There is however a limitation of the mechanistic explanation
```{figure} ../assets/2014_clifford_simtile_pureinhibition_model.png
:width: 300px
:align: center

Limitation of a purely inhibitory account of the tilt illusion (from Clifford 2014).

```

<!-- > FROM CLIFFORD 2014 (Fig. 3.) Limitation of a purely inhibitory account of the tilt illusion. (A) Schematic hill of activity in the response of a population of idealized orientation-tuned neurons to the presentation of a single stimulus orientation of 0 degrees. Response is plotted as a function of the preferred orientation of the neurons. Note the conceptual distinction between the population response to a given stimulus, as illustrated here, and the orientation tuning curve of a single neuron. (B) Illustration of the modulatory effect on the gain of the neuronal population when a surround stimulus is presented. Lateral inhibition operates between neurons tuned to the same orientation but with receptive fields covering different locations. This lateral inhibition is greatest at the orientation of the surround (here, 0 degrees). (C) A surround oriented at around 15 degrees has an asymmetric effect on the population response to a test at 0 degrees. Specifically, those neurons with preferred orientations closer to the surround orientation are inhibited more (red shaded region) than those on the opposite flank of the population response to the test. Thus, the resulting hill of activity is shifted away from the surround orientation: a repulsive tilt illusion. (D) A surround oriented at around 75 degrees has virtually no effect on the response to a test at 0 degrees. Thus, a purely inhibitory account of the tilt illusion is unable to account for the existence of the attractive effects observed experimentally with inducers remote in orientation from the test. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.) -->

This figure captures the logic of the limitation:

* Figure A shows the population response to the central vertical grating presented on its own.
* Figure B shows the inhibitory influence produced by the surround stimulus.
* Figure C shows what happens when the center and surround are presented together. The red curve represents inhibition driven by the surround, and the black curve shows the resulting population response to the central stimulus. Because the inhibition is asymmetric, the response to the center is shifted away from the surround orientation. This produces the repulsive effect.
* Figure D shows the key limitation: when the surround is very different in orientation from the center, a purely inhibitory model predicts little or no effect. It therefore cannot explain why the illusion later reverses and becomes attractive.

So the classical inhibitory account captures an important part of the illusion, but not all of it.

---

The tilt illusion connects to broader topics in vision science, including visual aftereffects, adaptation, spatial frequency tuning, and normalization models. All of these ideas build on a similar theme: perception depends on the relative activity of neural populations, not just the response of a single neuron.

---

# Homework


:::{note} Homework: Read on disinhibition Theory
Read the remainder of from Clifford 2014. Think about how the disinhibition model improves on the purely inhibitory account we describe here.

```{figure} ../assets/2014_clifford_disinhibition_model.png
:width: 200px
:align: center

```


:::
