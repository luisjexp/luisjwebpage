---
bibliography: [pg__references.bib]
site:
  hide_title_block: False
  hide_toc: false
  hide_outline: false


---

# Types of Approaches to Inquiry
_What do we mean by "explaining"?_

A point that is often neglected when first investigating a system is the kind of explanatory achievement one wants from the investigation. Some approaches are satisfactory so long as they have predictive power: they anticipate new observations, forecast future outcomes, or establish how much of a phenomenon is predictable from the information available. A money-hungry quantitative investor may care only that a model predicts market movements well enough, not whether it says anything deep or even true about why those movements occur. Other approaches are oriented more directly toward explanation: they seek to identify the causes, mechanisms, or principles that account for an observed phenomenon. A central bank, by contrast, cannot simply raise interest rates because an economic model says it should; it must explain why inflation is rising, why tightening policy is expected to help, and why the country should accept the costs of that decision. Both approaches can be scientifically valuable, but they are not interchangeable, and confusion between them has produced considerable ambiguity in both methodology and interpretation[@marr_vision_1982; @shmueli_explain_2010].

:::{note} Key terms

* **predictive approach**: prioritizes accurate prediction of new observations.
* **explanatory approach**: prioritizes explaining why a phenomenon occurs.
* **variable-centered approach**: explains by modeling relations among variables.
* **analytical-mechanistic approach**: explains by modeling how a phenomenon is generated, and sometimes why that generative process is organized as it is.

:::
# Predictive and explanatory approaches

A predictive approach asks whether a model can generate accurate predictions for new or future observations. This allows predictive work to employ a wider range of methods, including methods that may be difficult to interpret directly in theoretical terms. Moreover, in a predictive approach, variables need not function as clean operationalizations of theoretical constructs, and the model itself need not correspond closely to an underlying causal account. What matters most is whether the model captures enough structure in the data to generalize successfully beyond the sample at hand. For that reason, predictive approaches often treat theoretical transparency as desirable but secondary [@shmueli_explain_2010].

An explanatory approach begins from a different priority. Here the model is expected to be answerable to a theory. The goal is not only to capture a pattern in the data, but to represent a hypothesized causal structure in a form that can be assessed empirically. In such work, the variables of the model are typically treated as operationalizations of theoretical constructs, and the model is judged partly by whether it permits meaningful interpretation in relation to the underlying theory. Explanatory approaches are therefore usually retrospective in orientation: they begin with a phenomenon and a prior theoretical account of it, then ask whether the data support that account. Their main concern is not simply whether a model performs well, but whether it says something informative about why the phenomenon occurs [@shmueli_explain_2010].

The difference between these approaches is not trivial. It affects the entire research process, including the choice of variables, the construction of the model, the criteria of evaluation, and the interpretation of success or failure. A model that is well suited for explanation may not be optimal for prediction, while a model that predicts extremely well may be of limited use for explanation. In finite and noisy data, these goals often come apart. The model that best approximates an underlying theoretical structure is not always the one that minimizes prediction error, and the model with the highest empirical accuracy is not always the one that best supports causal interpretation [@shmueli_explain_2010].

At the same time, it would be a mistake to treat predictive work as scientifically empty. Prediction-focused approaches can contribute to science in several ways. They can reveal that a phenomenon contains more regular structure than current theories can explain. They can establish empirical benchmarks against which explanatory models may later be compared. They can help identify useful variables, suggest new measurements, and motivate the search for new causal mechanisms. In this sense, predictive success may function as a reality check on explanatory ambition: if a phenomenon is barely predictable at all, then some theoretical expectations may need revision; if it is highly predictable by methods that current theories do not anticipate, then those theories may be incomplete. Prediction, therefore, need not be opposed to science. Its value depends on what claims are made on its behalf [@shmueli_explain_2010].

This point is especially important for contemporary work on AI and other complex systems. In practice, many fields already move back and forth between explanatory and predictive approaches. A researcher may begin with predictive tools in order to discover regularities, and only later ask what theory or mechanism might explain them. Conversely, a researcher may begin with a theory and then use predictive evaluation to determine whether the resulting model captures enough structure to be taken seriously. Scientific inquiry, in other words, often proceeds through a sequence of partial advances rather than through a single pure approach. It is therefore better to think of prediction and explanation as distinct but interacting approaches to inquiry, rather than as mutually exclusive camps [@shmueli_explain_2010; @marr_vision_1982].

In my view, then, prediction and explanation are both legitimate approaches. They answer different questions, support different inferences, and produce different forms of understanding. A clear account of scientific inquiry requires that they be distinguished before either is judged [@Hedstrom_Swedberg_1998; @Sorensen_1998; @shmueli_explain_2010].

# Subtypes of explanatory approaches

Within explanatory work, further distinctions are needed. Not all explanatory approaches aim at the same kind of understanding. A useful next distinction is between variable-centered and analytical-mechanistic approaches. Both belong, in a broad sense, to explanatory inquiry rather than purely predictive inquiry, because both are concerned with more than the generation of accurate output alone. Yet they do not seek the same kind of explanatory achievement.

## The variable-centered approach

The variable-centered approach treats explanation as a matter of identifying which variables matter, how strongly they matter, and in what direction they relate to an outcome. In this style of inquiry, theories are often translated into claims about which factors contribute to a phenomenon, which do not, and how variation in one factor is associated with variation in another [@Hedstrom_Swedberg_1998; @Sorensen_1998]. The attraction of this approach is easy to understand. It provides a disciplined and empirically tractable way to move beyond impressionistic description of a system. It also offers researchers a language for expressing causal claims with a degree of formal precision, especially when the variables used are intended as valid operationalizations of theoretical constructs.
Variation

**A focus on variation**

At its core, the variable-centered approach explains a phenomenon by explaining its variation. The question is not simply what a phenomenon is, but why it changes across people, groups, times, or conditions. In that sense, variables become the main actors of the explanation. If hours of sleep covary with reaction time, or years of education covary with income, then the model claims to have explained something by showing how variation in one factor tracks variation in another. This is already a real scientific achievement. It can reveal stable regularities, constrain theories, and make a vague problem empirically manageable. But it also shows the limit of the approach. A variable-centered model may tell us that sleep predicts reaction time, or that education predicts income, without yet explaining how the relation is produced. A regression coefficient, path coefficient, or standardized effect may summarize a relationship, but it does not by itself explain the process through which that relationship comes about [@Hedstrom_Swedberg_1998]. To say that one variable has a larger estimated effect than another is not the same as identifying the mechanism that produces the outcome. Variable-centered explanation can therefore move beyond surface description while still falling short of a deeper account of why the pattern exists at all.

**Controlling Variables**

This limitation becomes clearer in the typical practices that grew around the variable-centered tradition. One such practice is the accumulation of control variables. Once computational tools make it easy to include many candidate predictors, researchers are tempted to include them simply to be safe, even where the conceptual justification for doing so is weak [@Sorensen_1998]. The result can be a model that looks more rigorous because it contains more variables, but is actually less informative because the variables were added without a strong reason. In that case, explanation starts to drift into bookkeeping.

**Linear and additive specification**

Another practice is the emphasis on additive or linear specification, chosen not because theory requires it, but because it is convenient to estimate and interpret [@Sorensen_1998]. This does not mean linear models are useless. They are often powerful and clarifying. But the criticism is that ease of estimation can become a substitute for theoretical justification. A model may be linear because the software likes linearity, not because the system does.

**Variable importance**

A third practice is the attempt to compare the “importance” of variables using standardized coefficients or variance-based measures. Such comparisons often appear more meaningful than they are, especially when the variables compared differ in kind, scale, or role within the phenomenon under study [@Sorensen_1998]. To say that one variable explains more variance than another can be useful in a narrow statistical sense, but it does not necessarily tell us which part of the underlying process matters more.

:::{note} Variable Importance Is Important in Visual Neuroscience
In visual neuroscience, and also in machine learning, asking which features matter has often been scientifically productive. This is because such neuroscientific models are often aimed at understanding information-processing systems, where the concepts of feature, representation, and transformation are central to the system itself [@marr_vision_1982 ; @carter_blog_zoomin]: Discovering that a neuron or circuit is sensitive to some features rather than others can be a far-reaching idea, because it helps reveal what information is being extracted and used. Indeed, much of the progress in early visual neuroscience depended on identifying the stimulus features to which cells responded.
:::

**Association is not mechanism**

A further difficulty is that statistical association alone does not reliably distinguish genuine causation from coincidence, confounding, or spurious relation. A pattern may be robust enough to enter a model and yet remain theoretically unsatisfying if no plausible generative account of the relation can be given [@Hedstrom_Swedberg_1998]. This does not mean that every association without a known mechanism should be discarded. Science often proceeds under uncertainty, and plausible mechanisms are not always available in advance. It does mean, however, that variable-centered explanation should be treated as incomplete when it substitutes association for process.

**Scientific value**

These limitations do not invalidate variable-centered inquiry. On the contrary, it is often an important and productive stage of explanatory work. It is more informative than a purely predictive approach when it uses variables as operationalizations of theoretical constructs and attempts to test causal hypotheses rather than merely forecast outcomes [@shmueli_explain_2010]. In practice, variable-centered work is often most valuable when it serves as a bridge: it provides a groundwork for operationalizing constructs, identifies regularities worth explaining, constrains the space of plausible theories, and offers a formal language in which competing claims can be compared. But if the goal is a deeper understanding of how a phenomenon is generated, the inquiry must usually move beyond variables alone and toward a more explicitly analytical-mechanistic account [@Hedstrom_Swedberg_1998; @Sorensen_1998].

## The analytical-mechanistic approach

If the variable-centered approach explains a phenomenon by identifying relevant variables and estimating the relations among them, the analytical-mechanistic approach seeks a different and stronger kind of explanation. Its goal is not merely to show that one factor is associated with another, nor even only to show that the association is stable under controls. Rather, it aims to specify how the observed relation is generated, and, where possible, why this particular process or organization gives rise to the outcome in question.

This difference is easy to understate. A variable-centered model may tell us that changes in X are reliably associated with changes in Y, and this can already be scientifically useful. But an analytical-mechanistic account asks a further question: through what process does X bring about Y? In stronger cases, it also asks why that process, rather than some alternative one, is in place. This additional demand is what gives the approach its greater explanatory force.

Importantly, a mechanism is not simply any ordered description of a process. A temporally pleasing sequence of events can still leave the central explanatory question untouched: Consider the familiar molecular cascade underlying depolarization and action-potential propagation. One can recite the sequence in detail and still have learned relatively little about why that organization is used by the neuron, or what larger explanatory role it serves in neural function. 

```{figure} ../assets/fain_senstranstxtbook_fig42_2019.png
:width: 400px
:align: center

Representative pathways of metabotropic signal transduction (from [@fain_senstranstxtbook]): A long and orderly sequence of events does not, by itself, amount to a satisfying mechanistic explanation. That said, such cascades can be deeply explanatory when linked to the problem they solve. In photoreceptors, for instance, the multi-step cascade helps explain extreme sensitivity because it implements signal amplification, even near the single-quantum level.
```

Likewise, imagine having exhaustive information about every neuron in V1: its position, its connections, its transmitters, and the exact path of activity through the early visual system. That would be an extraordinary description, but it would not yet amount to an understanding of vision. Mechanistic explanation does not consist in reproducing a process at ever smaller scales. It consists in isolating those elements judged essential for the problem at hand [@Hedstrom_Swedberg_1998; @deRegt_understanding_2020].

For that reason, I prefer the term analytical-mechanistic to merely process-based or sequence-based. A good mechanistic model is not a complete mirror of reality. It is a deliberately simplified account designed to explain how a relation comes about. In that sense, it reaches beyond both description and association. It aims at a more substantive account of causal production.

The appeal of this approach is clear. It promises a more direct explanation, a better distinction between genuine causation and coincidental association, and a more satisfying understanding of why a phenomenon occurs as it does [@Hedstrom_Swedberg_1998]. It also avoids some of the comparison problems that arise in variable-centered work. It is often difficult to say whether one variable is “more important” than another when the variables differ in kind, scale, or role. It is more meaningful, however, to compare alternative mechanisms that could plausibly produce the same outcome [@Sorensen_1998]. In this way, the analytical-mechanistic approach can support a more informative form of theory comparison than a framework centered mainly on standardized coefficients or portions of variance explained.

# Summary
The analytical-mechanistic approach therefore captures one of the strongest senses in which science seeks understanding rather than only empirical adequacy. I would not say that it replaces predictive or variable-centered work. Scientific understanding often depends on all three. Predictive models may reveal patterns worth explaining, and variable-centered models may constrain the space of plausible accounts. But the analytical-mechanistic approach pushes further by demanding a generative explanation of the phenomenon itself. In that sense, it represents one of the clearest attempts to answer not just whether a relation exists, but how it is brought about and why that account should count as explanatory [@Hedstrom_Swedberg_1998; @Sorensen_1998; @keas_systematizing_2018].
