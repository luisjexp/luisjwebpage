# Hermann Grid

## What do you see?

```{figure} ../assets/hermans_grid_illusion.png
:width: 480px
:align: center

Hermann grid illusion.
```

This image is known as the Hermann grid illusion. It consists of a regular array of black squares separated by horizontal and vertical white bars. When you look at it, faint gray dots or smudges seem to appear at the intersections of the white lines. _Why do we see them?_

# Background: Center-Surround Cells

To understand the classical explanation, we first need to review a type of neuron found in the retina: the center-surround retinal ganglion cell (which I will abbreviate as CS cell). These cells have often been used to explain the gray blobs seen in the Hermann grid.

**Several properties of CS cells matter here:**
1. Location preference: A CS cell responds best to stimuli appearing in a particular region of visual space. The farther the stimulus is from that preferred location, the weaker the response.
3. Size tuning: A CS cell responds depending on how light is distributed across its receptive field. Light in the center tends to increase the response, whereas light in the surrounding region tends to suppress it.
4. No orientation tuning: CS cells are not tuned to orientation. If an elongated bar falls on the receptive field, the cell responds similarly whether the bar is vertical, horizontal, or diagonal.

```{figure} ../assets/cs_cells_rfs_simulation.gif
:width: 200px
<!-- :align: center -->
Try this great interactive simulation [here](https://www.macmillanlearning.com/studentresources/college/df/biology/life_11e/life_activity_46_02.html).
```





# The Classical Model
Now we can describe the classical account of the illusion. The idea is that the gray blobs at the intersections arise because CS cells responding to the intersections are less active than CS cells responding to the straight white corridors between intersections. Here is the logic:

First, imagine a CS cell whose receptive field is centered on an intersection. That cell receives light not only in the center of its receptive field, but also in more of the surrounding region. Because extra light in the surround suppresses the cell’s activity, its response is relatively weak.

Now imagine a CS cell centered on a non-intersection region of a white bar. That cell still receives light in the center, but the surround contains less light than at an intersection. As a result, its response is stronger.

The classical theory therefore predicts an imbalance across the population: cells responding to intersections are less active than cells responding to neighboring white corridors. This weaker response at the intersections is then proposed to give rise to the illusory gray blobs.


```{figure} ../assets/hermans_grid_retinal_projection_classic_theory_zoomIN.png
:width: 520px
:align: center

Retinal projection of the Hermann grid under the classical center-surround account.
```

# Limitations and Alternative Ideas
The classical theory is elegant, but it is likely too simple. Below are two important reasons why it struggles.

## The illusion is perceived over a large range of sizes
The classical model predicts that the illusion should occur only when the size of the grid is well matched to the size of CS receptive fields. If the intersections are too large, so that they extend beyond the receptive field, the illusion should weaken or disappear. You can also ask the opposite question: what should happen if the grid is too small?

This prediction follows from the fact that retinal receptors, ganglion cells, and their receptive fields have fixed physical sizes. 

We can test this prediction by changing the size of the grid and therefore changing how much of the receptive field is covered by the intersections. But contrary to the model’s prediction, the illusory blobs are perceived across a fairly wide range of grid sizes.

To explain this 'size invariance', the theory must be expanded. One possibility is that the illusion is not generated only by retinal ganglion cells, but also by neurons in later visual areas, such as V1, whose receptive fields are larger (Wolfe, 1984; Spillmann, 1994; Schiller and Carvey, 2005).


## The illusion changes when the grid is rotated

The classical model also predicts that the illusion should persist when the grid is rotated.

This follows from the fact that CS receptive fields are circular. If a receptive field is circular, then rotating the stimulus should not matter very much, at least in the classical account.

We can test this by rotating the grid. But contrary to the model’s prediction, the illusion weakens when the grid is tilted away from horizontal and vertical orientations (Schiller and Carvey, 2005).  the results of 

To account for this rotation effect, one can invoke orientation-tuned neurons in V1 (Hubel and Wiesel, 1968). In V1, more neurons tend to prefer cardinal orientations (horizontal and vertical) than oblique ones, and human visual performance is also generally worse for oblique orientations, a phenomenon known as the oblique effect (Appelle, 1972; Westheimer, 2003).


<!-- ```{figure} ../assets/herman_grid_excercise_var_graph_results.png
:width: 620px
:align: center

Exercise for the Hermann grid.
``` -->



# Homework

1. Draw grids at different orientations and show how they would project onto the receptive fields of CS cells.
2. Describe what the classical theory predicts should happen to CS cells in each case.
3. Draw grids of different sizes and show how they would project onto and cover the receptive fields of CS cells.
4. Describe what the classical theory predicts should happen in each case.

**Bonus**

Can you think of another prediction made by the classical model? How could you test it?

