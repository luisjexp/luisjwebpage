# Motion After Effect

<iframe width="100%" height="420"
  src="https://www.youtube.com/embed/oNhcpOIQCNs"
  title="Motion aftereffect video"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  allowfullscreen>
</iframe>

# Motion direction tuning and perception 
Unlike the tilt illusion, which depends on how nearby stimuli interact at the same moment, the motion aftereffect depends on what happens to motion-sensitive neurons after prolonged stimulation over time.


## Properties of Individual Cells
Before introducing theories of the illusion, let’s briefly review how the visual system represents motion direction. The human visual cortex contains neurons, or “units,” that are tuned to the direction of a moving stimulus. A few basic properties of these motion-tuned units matter here:

1. These units are tuned to **motion**, not to static stimuli, though they still exhibit a baseline level of activity even in the absence of stimulation.
2. Each unit has a **preferred direction**. It responds best to one particular direction of motion.
3. Although a unit responds most strongly to its preferred direction, it also responds more weakly to nearby directions.
4. The farther the motion direction is from the unit’s preferred direction, the weaker the response.

## Perceiving Motion Direction

So how do motion-tuned units give rise to our experience of motion?

When you view a static image, motion-tuned cells are relatively quiet, firing only at baseline rates. In this state, the system is roughly balanced: no one motion direction is strongly favored over another.

That changes when you view a moving object, for example one moving downward. Such a stimulus activates cells that prefer downward motion more strongly than cells tuned to other directions. The population is now in an **imbalanced activation state**. In this simple picture, motion is perceived when one direction-tuned population becomes more active than the others.

Let’s highlight two key points:
- The visual system contains units tuned to many different motion directions.
- Motion is perceived when there is an imbalance in the activity of cells tuned to different motion directions.

# Adaptation Theory

So why do we experience the aftereffect? One classical idea is that neuronal adaptation, or “fatigue,” is the culprit. The idea begins with the following property of visual neurons: when they are stimulated for a prolonged period of time, their response can decline, even when the stimulus is one they normally prefer. After such prolonged stimulation, the neuron enters a state of reduced sensitivity. It takes time to recover, but eventually it returns to its normal responsiveness.

Try the interactive neuronal adaptation simulation below, or [open it in a new tab](https://ilearn.med.monash.edu.au/physiology/experiments/action-potentials/adaptation#simulation).

<div style="margin: 1.5rem 0 2rem 0; padding: 1rem; border: 2px solid #d0d7de; border-radius: 6px; background: #f8f9fa;">
  <iframe
    src="https://ilearn.med.monash.edu.au/physiology/experiments/action-potentials/adaptation#simulation"
    title="Neuronal adaptation simulation"
    frameborder="0"
    scrolling="yes"
    style="display: block; width: 100%; height: 650px; border: 3px solid #8c959f; background: white;"
    allowfullscreen>
  </iframe>
</div>

So how can this property explain the motion aftereffect? Imagine fixating on downward motion, such as a waterfall, for a prolonged time:

- At first, downward motion strongly activates downward-preferring neurons more than the others. This imbalance gives rise to the perception of downward movement.
- But the longer those neurons are stimulated, the more their responses decline. They become less sensitive than they were at the start.
- When you then look at a stationary image, the downward-preferring neurons are still recovering and are therefore less active than usual.
- The population is now imbalanced in the opposite direction. Relative to the fatigued downward-preferring units, neurons tuned to upward motion are more active.
- As a result, the stationary image can appear to move upward.

<!-- ```{figure} ../assets/After_effect_tuning_after_adapt.png
:width: 560px
:align: center

Imbalance after adaptation.
``` -->


**Evidence For the theory**:

The primary support for this idea comes from classical work showing that some neurons reduce their firing after a few seconds of stimulation. For example, Barlow and Hill (1963) reported such response declines in rabbit retina. Supporting the theory further, the duration of neural adaptation has been argued to resemble the duration of the perceptual aftereffect in humans (Thompson 2009). The appeal of the theory is that it links a change in neuronal responsiveness to a change in perceptual experience. 

**Chief Limitation:**

However, the theory has its flaws. One important challenge is that neurons in V1, where many direction-tuned cells exist, do not appear to fatigue in the simple way the theory requires, either under normal stimulation or in response to adapting stimuli (Bednar 2000, citing Finlayson & Cynader, 1995; McLean & Palmer; Vidyasagar, 1990). More broadly, fatigue can sometimes take too long to develop, whereas some illusory effects emerge almost immediately (Tolhurst 1974).

---

So adaptation theory captures an important part of the phenomenon, but may not provide the full explanation.
