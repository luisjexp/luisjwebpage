# Limited input Model
I'll walk through a simple idea for how orientation selectivity and orientation maps in V1 might arise from the structure of retinal input. The model we are reviewing is based on work from @https://doi.org/10.1038/nn.2824. The idea proposes that the spatial arrangement of ON and OFF retinal ganglion cells already contains enough structure to help explain both the preferred orientation of individual V1 neurons and the larger-scale organization of orientation maps across cortex.

# The Orientation Map In V1

## Cells in V1 Detect Edges
```{figure} ../assets/hubweisel_spikeResp2Ori.png
:width: 200px
:align: center

```

```{figure} ../assets/orituned_cells_simulation.gif
:width: 200px
:align: center

```

All known mammals have visual neurons that are tuned to the orientation of elongated stimuli, such as edges. These cells do not respond equally to every edge. The stimulus has to be at a "preferred" angle. Some cells respond best to vertical edges, others to 45-degree edges, and others to horizontal ones. Such cells are said to prefer a particular orientation. Orientation-tuned cells were first described in primary visual cortex, but depending on the species, similar tuning can also be found in the retina, thalamus, and higher visual areas. 

To summarize: A “well behaved” orientation tuned neuron
1. responds to a stimulus with some kind of elongated feature, such as a bar, or a grating.
2. has preferred orientation. It fire the most when a stimulus is at a particular orientation. Different units have different preferred orientations.
3. it also respond, though less strongly, to stimulus orientations that differ from its preferred. The strength of the its response is inversely related to the difference between its preferred orientation and the stimulus orientation. The larger the difference, the weaker the response.


## Cells with Similar Orientation Preferences cluster together 
```{figure} ../assets/oricolumns_pinwheelstructure.png

:width: 200px
:align: center

```

These edge-detecting cells are found in a region of the brain known as V1, which sits near the back of the head. Here is a picture of the surface of V1. Each pixel corresponds to a cell, and its color indicates the orientation that the cell prefers. Notice that cells with similar orientation preferences cluster together. For example, cells that prefer vertical edges tend to lie near other cells with similar preferences.

# The Model

The authors of the paper attempted to provide a simple and detailed explanation for both the formation of orientation-selective cells and the periodic maps these cells create across cortex. In short, the model proposes that V1 cells inherit this structure by sampling from a highly organized arrangement of cells in the eye. According to the model, that retinal input is already structured enough to bias V1 neurons toward particular edge orientations and to generate periodic orientation maps.

**Cells in the Eye Are Highly Organized**

To introduce the model, I'll begin by explaining the highly structured patterns of cells in the eye.

There are two relevant cell types in the eye: ON-center cells and OFF-center cells. The first step in the model is to look at how these cells are physically arranged across the retina. In this framework, ON and OFF cells are treated as paired units. These pairs are distributed across the retinal surface, and each pair is called a dipole.

```{figure} ../assets/paikringach_2012_interference.png

:width: 300px
:align: center

```

The two cells in each pair have opposite signs: an OFF-center cell (blue) is coupled with an ON-center cell (red). Each pair therefore defines an angle, and that angle changes gradually as one moves across the retinal surface.

**Dipoles Send Output to V1 Cells**

Each dipole is assumed to project to a cell in V1, with nearby retinal positions mapping to nearby cortical positions. This is a simplified description, but it is enough for the basic logic of the model: a dipole near the center of the retina connects to a V1 cell near the corresponding region of cortex.

So the picture is this: the retina contains a highly structured array of ON/OFF pairs whose angle varies smoothly across space, and the summed output of each pair is sent downstream to a V1 neuron.

```{figure} ../assets/onoff_nn_layered_v1pathway.png
:width: 200px
:align: center

```

**Edge Detection in V1 Depends on Angle of Cell Couple in the Eye**

When light falls on an ON-center cell, its activity increases. When light falls on an OFF-center cell, the opposite happens: its activity is suppressed. In this model, the activity of the two cells is summed and sent to a neuron in V1.

Now consider a horizontal bar of light falling on a dipole that is also aligned horizontally on the retinal surface. In that case, the ON and OFF components tend to cancel, leading to little or no net drive to the target V1 neuron. More generally, when the orientation of the stimulus matches the orientation of the dipole, the net response is weak.

By contrast, if the edge is oriented orthogonally to the dipole angle, the balance changes and the combined output becomes stronger. In that case, the target V1 neuron receives a larger signal. This is the basic logic by which dipole angle becomes linked to preferred orientation in cortex.

```{figure} ../assets/onoff_edgedect_vs__ori_cartoon.png
:alt: 
:width: 300px
:align: center

Dipole angle relates to edge orientation responses of the ON-center and Off-center RGCs, and their summed output. (Left) The on-center cell (red) is activated by the horizontal strip of light, but its off-center counter part (blue) is suppressed. The opposite would be true if the gray strip landed on their receptive fields. (Right) In this scenerio, both cells reveive their "preferred" stimulus: The on-center cell is activated by the horizontal strip of light, and the off-center cell  is also activated but by the white strip. In both cases, the net output is summed by the target cell in V1 (green).
```


# Model’s Results: 
The authors then ran a computer simulation to test what happens when the retina is presented with many edges at different orientations. They examined how retinal dipoles responded, how those responses combined, and what kind of orientation map would emerge in V1. The result was a map organized in a way that resembled real cortical orientation maps.

```{figure} ../assets/paikringach_2012_rotation_cartoon.png
:width: 200px
:align: center

```

**Orientation Maps with Iso-Orienation Domains**

The simulation also produced a more specific prediction. The resulting maps contained regions in which particular orientations were over-represented, and these regions were arranged across cortex in a roughly hexagonal pattern. That is a strong and testable prediction: if the model is correct, similar structure should be visible in real brains.

::::{figure}
:class: grid grid-cols-2 items-start gap-4


:::{image} ../assets/paikringach_2012_isoori_dipoles.png
:width: 300px
:align: center

:::

:::{image} ../assets/paikringach_2012_isoori_orientation.png
:width: 300px
:align: center

:::
::::
**Iso-Orientation Domains Found in Real Brains**

The authors then looked at orientation maps from several mammalian species and found that these iso-orientation domains were indeed arranged in a roughly hexagonal manner. This figure shows examples from four species: monkeys, cats, ferrets, and tree shrews. Without getting into the full details of the analysis, the main point is that the yellow regions mark areas where nearby orientations are especially similar, in line with the model’s prediction.

```{figure} ../assets/paikringach_2012_isoori_simulation.png
:width: 350px
:align: center

```

---

This model provides a simple explanation for how orientation maps may be formed. It does not rely on experience-dependent plasticity or on a complicated set of genetic rules.
