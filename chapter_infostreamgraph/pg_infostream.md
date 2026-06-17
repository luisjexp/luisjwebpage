# Live Action Battle Space


```{figure} ./fig1_node_hierarchy.png
:width: 620px
:align: center

Initial organization of units across the battle field. In this example, the layout units follows the "chain-of-command path.


```


# Communication represented as a directed graph

```{figure} fig2_dirgraph.png
:width: 620px
:align: center

The arrows represent the origin and destination of a signal between pairs of units. The frequency of communication between units is represented by the width of the arrows. If two units do not communicate, then no arrows are drawn.

In this example, the company sends signals towards the platoons but never sends a direct signal towards the squads. Platoon 2 sends signals down to the squads more often than they send it back up. 


```


# Communication frequency represented as a matrix

```{figure} fig3_matrix.png
:width: 620px
:align: center

A matrix representation of the graph above. Numbers in each box represent number of times a signal was sent between a pair of units.

Numbers in the lower triangle show the frequency of signals originating from higher levels of the chain of the command. 

Numbers in the upper triangle show frequency of signals originating from the bottom towards the top of the chain.


```


# Losing Connections

```{figure} fig4_pruned.png
:width: 620px
:align: center

As units are deployed across the battle ground, the network begins to prune. Units are unable to send messages back to the network, but can still receive signals. Others are faced with the opposite problem: they can only send signals back to the network, but cannot receive them.  In the extreme case, a unit is completely disconnected, unable to send or receive signals to and from the network


```


# Recovering or Adding New Connections


```{figure} fig5_add.png
:width: 620px
:align: center

The network may need to more add channels or recover lost ones. In this example, channels are added so that units can send and receive signals from most other units. This network may have its draw backs, since it may lead to over-communication, or a large electronic footprint.


```


# Updating mission objectives


```{figure} fig6_update.gif
:width: 620px
:align: center

A significant event might require a change in mission objectives. An ideal network should quickly process this information and update all units on new mission objectives. In this example, information about an event is received by mission command, who decides on a new course of action and updates all units.

```

