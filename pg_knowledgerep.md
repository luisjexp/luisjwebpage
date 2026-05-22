---
bibliography: [chapter_approach/pg__references.bib]
---


# Learning and Knowledge Networks

Humans appear to represent many forms of knowledge in associative networks including sensory, spatial, and semantic.  How do we acquire these representations?

We can try to answer this question by studying how humans learn learning about conceptual spaces that take the form of a graph: Complex, spatially or temporally structured information can be formalized as a ‘graph’ composed of ‘nodes’, corresponding to a set of mental concepts, and ‘edges’ , corresponding  the transition probability between such nodes. Recent work [@basset_2020_learnreview] shows that humans can indeed learn to navigate such graph-structured conceptual spaces by repeatedly ‘walking’ along the network contours. For example, when hearing someone speak, there is a certain probability of hearing one syllable after hearing another syllable (see figure below). The same idea can be generalized to a multitude of actions (e.g., object identification).  See [@basset_2020_learnreview] for an excellent review on this topic.

```{figure} /assets/lynnbasset_2020_repnetworkreview_fig1.png
:width: 480px
:align: center


```
Due to our limited cognitive capacity, we are only capable of learning some, but not all types of graph-like patterns of concepts. What differentiates the “learnable” patterns from the “un-learnable” ones? What can this tell us about the way information is stored in the human brain? Can we augment human learning of graph-patterns when under difficult learning situations? These are the sorts of questions I am interested in. Given my background in vision-science, I had perform a visual-navigation task in which the order of visible objects is depends on a random walk through a graph-structure. Here I show some of examples of this preliminary work.




## Introduction to the Experiment

This experiment is motivated by recent work on graph-learning [@https://doi.org/10.1016/j.cognition.2022.105103 ; @https://doi.org/10.1038/s41598-017-12876-5 ; @https://doi.org/10.1038/s41562-018-0463-8]. Read the figure captions below for an overview.

```{figure} /assets/jimenez_graphlearning_graph.png
:width: 480px
:align: center

```
**Figure 1: Graph structure of the statistical pattern of an image sequence to be learned by a participant.** Nodes represent the set of images presented to an observer. A line between a pair of images means that there is a non-zero probability that one image is be presented following the presentation of the image it is paired with. The path drawn by the lines with arrows is created by performing a random walk through the graph.  



```{figure} /assets/jimenez_graphlearning_task.png
:width: 480px
:align: center

```

**Figure 2: Right: An example sequence of images presented to the participant**. Images are presented one by one, for about half a second. The sequence of images is based on the sequence of nodes traversed by the random walk in figure 1. **Left:** **Example of a Query trial**. Every so often, the walk is stopped, and the subject is asked to guess which images can be presented next.


```{figure} /assets/jimenez_graphlearning_task_pilot.mp4
:width: 100%
:align: center

```
**Figure 3: Live recording of experimental stimulus.** Images drawn from a random walk through a graph. Note you can slow down the play back speed**.** On the right is a graph of 12 nodes each of which represents an image category (e.g. satellites, daisies, rockets, pizza, tents, cats, irons, etc). *This graph is not visible to the participant*. The random walk starts by at a random node (the node surrounded triangle), and an image associated with that node is presented on the participant’s screen (left). This node is connected to multiple nodes surrounded by green squares. Among these nodes, one is chosen randomly to be the next node in the sequence (the node surrounded by the light green square). 

After about 1/2 a second, the graph on the right is updated so the green triangle now surrounds the newly selected node, and this node’s corresponding image replaces the old image on the screen. Every few seconds, the walk stops. At this point, the participant must guess what the next image will be. Four images are presented to the participant, only one of which is a viable image. This image  corresponds to the node surrounded by the *light green square*. The other images correspond to nodes marked with a *red X* on the graph.  Once the participant makes a choice, the random walk continues. 

Over time, the participant improves her performance by providing more and more correct answers. That is, the participant learns the graph.  

## Preliminary Results

coming soon!

