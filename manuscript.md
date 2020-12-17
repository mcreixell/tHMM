---
title: A lineage tree-based hidden Markov model to quantify cellular heterogeneity
keywords:
- cancer
- heterogeneity
- lineage
- hidden Markov model
lang: en-US
date-meta: '2020-12-17'
author-meta:
- Shakthi Visagan
- Farnaz Mohammadi
- Sean M. Gross
- Luka Karginov
- JC Lagarde
- Laura M. Heiser
- Aaron S. Meyer
header-includes: |-
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta name="dc.title" content="A lineage tree-based hidden Markov model to quantify cellular heterogeneity" />
  <meta name="citation_title" content="A lineage tree-based hidden Markov model to quantify cellular heterogeneity" />
  <meta property="og:title" content="A lineage tree-based hidden Markov model to quantify cellular heterogeneity" />
  <meta property="twitter:title" content="A lineage tree-based hidden Markov model to quantify cellular heterogeneity" />
  <meta name="dc.date" content="2020-12-17" />
  <meta name="citation_publication_date" content="2020-12-17" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Shakthi Visagan" />
  <meta name="citation_author_institution" content="Department of Bioengineering, University of California, Los Angeles" />
  <meta name="citation_author_orcid" content="0000-0001-9295-2188" />
  <meta name="citation_author" content="Farnaz Mohammadi" />
  <meta name="citation_author_institution" content="Department of Bioengineering, University of California, Los Angeles" />
  <meta name="citation_author_orcid" content="0000-0002-0197-4670" />
  <meta name="citation_author" content="Sean M. Gross" />
  <meta name="citation_author_institution" content="Department of Biomedical Engineering, Oregon Health and Science University, Portland" />
  <meta name="citation_author_orcid" content="0000-0002-9621-8551" />
  <meta name="citation_author" content="Luka Karginov" />
  <meta name="citation_author_institution" content="Department of Bioengineering, University of Illinois, Urbana Champaign" />
  <meta name="citation_author_orcid" content="0000-0002-2455-1558" />
  <meta name="citation_author" content="JC Lagarde" />
  <meta name="citation_author_institution" content="Department of Bioengineering, University of California, Los Angeles" />
  <meta name="citation_author_orcid" content="0000-0002-3738-3119" />
  <meta name="citation_author" content="Laura M. Heiser" />
  <meta name="citation_author_institution" content="Department of Biomedical Engineering, Oregon Health and Science University, Portland" />
  <meta name="citation_author" content="Aaron S. Meyer" />
  <meta name="citation_author_institution" content="Department of Bioengineering, University of California, Los Angeles" />
  <meta name="citation_author_institution" content="Department of Bioinformatics, University of California, Los Angeles" />
  <meta name="citation_author_institution" content="Jonsson Comprehensive Cancer Center, University of California, Los Angeles" />
  <meta name="citation_author_institution" content="Eli and Edythe Broad Center of Regenerative Medicine and Stem Cell Research, University of California, Los Angeles" />
  <meta name="citation_author_orcid" content="0000-0003-4513-1840" />
  <meta name="twitter:creator" content="@aarmey" />
  <link rel="canonical" href="https://meyer-lab.github.io/tHMM/" />
  <meta property="og:url" content="https://meyer-lab.github.io/tHMM/" />
  <meta property="twitter:url" content="https://meyer-lab.github.io/tHMM/" />
  <meta name="citation_fulltext_html_url" content="https://meyer-lab.github.io/tHMM/" />
  <meta name="citation_pdf_url" content="https://meyer-lab.github.io/tHMM/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://meyer-lab.github.io/tHMM/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://meyer-lab.github.io/tHMM/v/6bfa2fa0c6edd1456bb057d30e65910ad795026a/" />
  <meta name="manubot_html_url_versioned" content="https://meyer-lab.github.io/tHMM/v/6bfa2fa0c6edd1456bb057d30e65910ad795026a/" />
  <meta name="manubot_pdf_url_versioned" content="https://meyer-lab.github.io/tHMM/v/6bfa2fa0c6edd1456bb057d30e65910ad795026a/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography: []
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: cache/requests-cache
manubot-clear-requests-cache: false
...



<small><em>
This manuscript
was automatically generated on December 17, 2020.
</em></small>

## Authors


+ **Shakthi Visagan**<br>
    ORCID
    [0000-0001-9295-2188](https://orcid.org/0000-0001-9295-2188)
    · Github
    [shak360](https://github.com/shak360)<br>
  <small>
     Department of Bioengineering, University of California, Los Angeles
  </small>

+ **Farnaz Mohammadi**<br>
    ORCID
    [0000-0002-0197-4670](https://orcid.org/0000-0002-0197-4670)
    · Github
    [farnazmdi](https://github.com/farnazmdi)<br>
  <small>
     Department of Bioengineering, University of California, Los Angeles
  </small>

+ **Sean M. Gross**<br>
    ORCID
    [0000-0002-9621-8551](https://orcid.org/0000-0002-9621-8551)<br>
  <small>
     Department of Biomedical Engineering, Oregon Health and Science University, Portland
  </small>

+ **Luka Karginov**<br>
    ORCID
    [0000-0002-2455-1558](https://orcid.org/0000-0002-2455-1558)
    · Github
    [lkargi](https://github.com/lkargi)<br>
  <small>
     Department of Bioengineering, University of Illinois, Urbana Champaign
  </small>

+ **JC Lagarde**<br>
    ORCID
    [0000-0002-3738-3119](https://orcid.org/0000-0002-3738-3119)
    · Github
    [jclagarde](https://github.com/jclagarde)<br>
  <small>
     Department of Bioengineering, University of California, Los Angeles
  </small>

+ **Laura M. Heiser**<br><br>
  <small>
     Department of Biomedical Engineering, Oregon Health and Science University, Portland
  </small>

+ **Aaron S. Meyer**<br>
    ORCID
    [0000-0003-4513-1840](https://orcid.org/0000-0003-4513-1840)
    · Github
    [aarmey](https://github.com/aarmey)
    · twitter
    [aarmey](https://twitter.com/aarmey)<br>
  <small>
     Department of Bioengineering, University of California, Los Angeles; Department of Bioinformatics, University of California, Los Angeles; Jonsson Comprehensive Cancer Center, University of California, Los Angeles; Eli and Edythe Broad Center of Regenerative Medicine and Stem Cell Research, University of California, Los Angeles
  </small>



## Abstract {.page_break_before}

Cell plasticity, or the ability of cells within a population to reversibly alter epigenetic state, is an important feature of tissue homeostasis during processes such as wound healing and is dysregulated in cancer. Plasticity is further linked to other sources of cell-to-cell heterogeneity, or diversity in cell state, including genetic mutations and variation in signaling during drug-resistance development. Ultimately these processes prevent most cancer therapies from being curative. The predominant methods of quantifying tumor-drug response operate on population-level measurements and therefore lack evolutionary dynamics, which are particularly critical for highly dynamic processes such as plasticity. Here, we apply a tree-based adaptation of a hidden Markov model (tHMM) that employs single-cell lineages as input, to learn the characteristic patterns of single-cell heterogeneity and state transitions in an unsupervised fashion. This model enables single-cell classification based on the phenotype of individual cells and their relatives for improved specificity when pinpointing the molecular drivers of variability in drug response. Integrating this model with a probabilistic language for defining observed phenotypes allows the model to easily be adapted to any phenotype measured in single cells. We paired cell fate with either cell lifetimes or cell cycle phase lengths (G1 and S/G2) as our observed phenotypes on synthetic data and demonstrated that the model successfully classifies cells within experimentally-tractable dataset sizes. As an application, we analyzed experimental measurements of cell fate and phase duration to determine the number of distinct subpopulations. In total, this tHMM framework allows for the flexible classification of single-cell heterogeneity of heritable traits across lineages.

## Summary points

- A lineage tree-based hidden Markov model (tHMM) quantifies cell-to-cell variability and dynamic population changes.
- Using a modular, probabilistic definition of observed phenotypes allows the model to work with a wide variety of measurements.
- The model accurately classifies cells within experimentally tractable dataset sizes.
- Classifying cells based on their phenotypic heterogeneity can uncover resistance mechanisms hidden at the population level.

## Author Summary

Heterogeneous traits, such as resistance or susceptibility to a drug, can be correlated across related cells because of partially inherited factors. These acquired traits of resistance may be the result of the microenvironment, epigenetics, or mutations. Using cell’s relationships we capture these dynamic transitions between different cell states and arrive at a more accurate quantification of cell heterogeneity within tumor populations. Our computational approach employing a modified hidden Markov model provides greater specificity by identifying intratumor resistance on a single cell level based on lineage histories and can identify dynamic changes in population structure upon treatment.


## Introduction

<!-- motivation; heterogeneity is an obstacle for chemotherapy  -->
One of the primary treatments of cancer consists of chemotherapy, mainly targeted therapies, whereby patients are administered drugs that eliminate fast-proliferating cells to stall cancer growth or eliminate the tumor. Long-term therapeutic efficacy, however, varies significantly due to the vast heterogeneity in intratumor response to therapy [@pmid:16129367; @doi:10.1016/S1470-2045(10)70130-3]. Cell variability in drug response can originate from cell-intrinsic factors, such as genomic alterations (i.e., altered nucleotide excision repair, telomere maintenance, and copy-number variation) and epigenetic mechanisms like changes in a chromatin state [@pmid:20371346], or cell-extrinsic factors such as spatial variability in the surrounding vasculature and environmental stressors [@doi:10.1038/nrg.2016.13; @pmid:25131830; @pmid:29250983]. Moreover, cell plasticity is observed more often in cancer cells where they take over the characteristics of othe cell subttypes which could directly affect their sensitivity to the therapeutic compounds [@doi:10.1038/bjc.2015.146].

<!-- literature review in conventional single-cell variability studies -->
Advances in ‘omics’ technologies have enabled detailed analysis of cell-to-cell variability [@doi:10.1016/S1470-2045(10)70130-3; @pmid:22397650], and the development of fine mapping and protein network algorithms have determined the presence of causal genetic mutations and dysregulation events that drive abnormal protein function [@doi:10.1534/genetics.114.167908; @pmid:27322546]. These modalities, however, are labor and time-intensive, do not account for environmental factors, and serve primarily as end-point analysis barring longitudinal observation of tumor evolution. In addition to 'omics' modalities, genetic _association_ studies (i.e., Cancer Cell Line Encyclopedia) are similarly able to find common risk factors with smaller effect sizes using population-level samples. The findings are valuable but fail to identify rare and meaningful transitions on the single-cell level [@pmid:22460905], in particular the stochastic changes in individual cell states that have significant effects on overall tumor resistance. Lastly, fitness markers such as cell end-of-life fate, lifetime, and population doubling time are adopted in the clinical setting to measure cell pathologies [@doi:10.1038/ni908; @pmid:8072198; @pmid:8655369; @pmid:20981102]. Recent research has made efforts to track phenotypic measurements of fitness at the single-cell level [@pmid:29381859; @pmid:22886092]; however, most efforts are not yet resolved enough to illuminate the full complexity of cancer cells due in large part to reliance on population-level analysis (i.e., IC~50~) [@pmid:25421725].  

<!-- Lineage data is special -->
Measurements accompanied by lineage relationships are uniquely valuable for studying inherited phenotypes within families of people or populations of cells. This value is well-recognized in linkage studies which use pairs of relatives to identify the genetic determinants of disease [@pmid:19136655]. Notably, linkage studies can identify genetic determinants with greater power than even much larger correlation-based studies because relatives essentially serve as internal controls (CITE REVIEW). Linkage studies also start with the phenotype of individuals, rather than grouping based on molecular differences as is most common in cells. Lineage-resolved data has demonstrated unique value in cells for uncovering heterogeneity due to transient differences [@doi:10.1101/373258; @doi:10.1073/pnas.1715639115].

<!-- tHMMs are a solution to modeling lineage data -->
Hidden Markov models (HMMs) provide a strategy to infer discrete states from measurements when a series of co-dependent observations are made. An example of this is their most widely-used application—time series data—where each measurement is dependent on what came before. Recognizing this co-dependence allows HMMs to make accurate inferences even in the presence of extremely noisy measurements since each neighboring measurement can provide accumulating evidence for a prediction. HMMs have been adapted to lineage trees (tHMMs) so that each measurement across the tree can provide accumulating evidence for a prediction. Just like with time-series data, these models can provide very accurate predictions despite noisy measurements and limited information by recognizing the co-dependence between measurements [@doi:10.1109/78.668544; @doi:10.1109/TSP.2004.832006]. tHMMs have been used in a multitude of applications, from image classification to comparative genomics [@pmid:18255546; @pmid:23762278]. In cells, these models have been fit to lineages collected from stem cells and bacteria colonies [@PMID:19628503; @doi:10.1101/488981]. Improvements in cell tracking and high-throughput imaging promise to make these models valuable techniques for studying the plasticity of heterogeneous cell populations. However, widespread use will require usable implementations that can be readily adapted to different experimental measurements, examples of unique insights they can provide, and standards for experimental validation.

<!-- Introduction to the paper -->

Here, we develop a generic implementation of tHMMs with a defined interface for integrating diverse types of measurements on binary or cell lineage trees. We use this to analyze how populations of single breast cancer cells respond to therapy with a cell cycle reporter. Single-cell measurements of the cell cycle revealed extensive variation in drug response that is not captured in population-level measurement. This model allows us to quantify the dynamics and phenotypic features of heterogeneity in drug response. Furthermore, we are able to predict the most likely number of phenotypically distinct subpopulation, cell state distribution, transition probabilities from one state to another, and each cell's expected state. This work, therefore, provides a flexible phenotype-driven route to discovering cell-to-cell variation in drug response, demonstrates an overall strategy for quantifying the dynamics of cell heterogeneity, and implements a very general software tool for widespread use of tHMM models.



## Results

### Lineage information provides unique information about the source and dynamics of heterogeneity

To illustrate the unique value of lineage measurements when analyzing heterogeneous drug responses, we plotted a series of lineages from our measurements of the breast cancer cell line AU565 treated with gemcitabine (Fig. @fig:lineage). If we consider these to be two different, hypothetical populations, there is a striking difference in the divisions that the cells undergo as well as their contribution to the population’s growth, but the starting and ending cell numbers are nearly identical. As a result, endpoint, population-level drug response measurements cannot distinguish these inner differences. Measurements that record the history of cells (e.g., CFSE staining, Luria-Delbruck experiment) can help to distinguish these two populations but make assumptions about the dynamics of heterogeneity [@DOI:10.1073/pnas.1715639115; @PMID:28607484]. Lineage measurements, by contrast, provide sufficiently rich measurements to accurately quantify the extent and dynamics of heterogeneity. By observing individual cells, a variety of phenotypic measurements such as inter-mitotic times, cell cycle phase durations, motility, cell death and division, morphology, and protein and transcription factor levels can be characterized in parallel.

![**Population-based measurements are insufficient to distinguish the dynamics of heterogeneity.**  Lineages of AU565 cells (a) treated with 5 nM gemcitabine or (b) control condition.](./output/figure1.svg){#fig:lineage}

### A tHMM infers the state of cells given measurements on lineage trees

Given the unique insights that single-cell measurements on lineage trees can provide, we wished to implement a strategy for classifying cells based on their phenotype and relationships. Given a set of measurements made across a lineage tree, we used a lineage tree-based hidden Markov model (tHMM) to fit these data (Fig. {@fig:tree}a). Just like a typical hidden Markov model, a tHMM can infer the hidden discrete states of cells given a series of measurements. This takes place using an iterative strategy wherein the states of each cell are predicted given distributions that describe the phenotype of cells in each state (“expectation” step), and then each distribution of phenotypes is fit to match the cells within that state (“maximization” step) (Fig. {@fig:tree}b). This expectation-maximization (EM) process repeats until convergence.

After fitting, the tHMM model provides a variety of information (Fig. {@fig:tree}c). First, this process provides an estimate for the starting abundance of each state and the probability of transitions between them. Second, the phenotypes of cells in each state are estimated and can be compared to distinguish how each state behaves. The state of each cell can be predicted from the fit data or new measurements. Finally, the model provides a likelihood of each cell’s observations and therefore the data overall. This last quantity can be used, for example, to estimate the number of cell states with distinguishable behavior. When implementing these processes, we ensured that a cell’s measurements are defined through a modular interface. This allows other forms of data to be easily integrated.

![**The tHMM interface.** (a) Input data takes the form of single-cell measurements, where the lineage relationship between cells is known. (b) The fitting process includes expectation and maximization steps, where model parameters are iteratively updated until convergence. (c) Output predictions of the model after fitting including the tree of inferred cell states, probabilities of transition between each state, starting abundance of each cell state, and distributions that describe the behavior of cells within each state. The model likelihood can be used to estimate the number of distinguishable cell states.](./output/figure2.svg){#fig:tree}

### Experiments of finite time necessitate data censorship corrections

Modeling the duration of each cell’s lifetime is complicated by the influence of experimental factors. Specifically, cells at the beginning or end of an experiment are cut off and so, while we observe them, we do not know the duration of their cell cycle phases. Previously, this has been addressed by simply removing incompletely-observed cells [@doi:10.7554/eLife.51002]. However, doing so results in a systematic bias, where longer-lived cells are preferentially eliminated. On the other hand, treating these truncated values like they were not truncated also creates a systematic bias; for example, it would create an upper bound on the possible cell lifetime.

To incorporate this effect into our model, we marked cells or their specific cell cycle phase that encountered the bounds of the experiment as censored. When estimating the properties of a cell’s lifetime or the probability of a cell’s observation, these cells instead used a censored estimator or the survival function of the distribution. Using synthetic data, we verified that this correction resulted in accurate phenotype estimations (Fig. @fig:censor). This ensures that we can accurately infer cell states despite this experiment effect.

![**Experiments of finite time necessitate data censorship corrections.** (a) Randomly generated uncensored two-state lineages. (b) State assignment accuracy with uncensored lineages. (c) Randomly generated censored two-state lineages. State 0 and 1 cells are shown in different colors. (d) State assignment accuracy with experiment time- and cell death-censored lineages. Scatter points represent the entire fitting process for a randomly generated population.](./output/figure4.svg){#fig:censor}

### Synthetic lineage benchmarks show a tHMM can accurately estimate population behavior

To evaluate how accurately a tHMM model could infer the behavior of multi-state cell populations, we used synthetic populations of cells in a wide variety of configurations. In each case, we determined that our implementation of a tHMM model could accurately and without bias infer the hidden states and parameters of a population given roughly 100 cells. This synthetic data included situations that were not censored (Figs. @fig:uncenSingle, @fig:uncenMulti, @fig:performUncenSingle, @fig:performUncenMulti) and censored due to cell death and experimental duration to be a valid representative of experimental lineages (@fig:performSyn, @fig:performCenMulti, @fig:cenMulti). In addition to varying the number of cells in a population, we benchmarked populations with varied percentages of cell states (Figs. @fig:prop4, @fig:real_5) and varied phenotypic differences between the states (Figs. @fig:wass1, @fig:wass2, @fig:wass). In total, this benchmarking showed that our tHMM model would provide accurate results.

More specifically, one of the benchmarking studies we performed was with data matching our measurements of AU565, where G1 and S/G2 phase periods were quantified (Fig. {@fig:performSyn}a). Although the tHMM model was fit with no information about the true underlying parameters of the simulated cells, it accurately distinguished the two underlying cell states phenotypes (Fig. {@fig:performSyn}b–d) and member cells (Fig. {@fig:performSyn}e). Note that in Fig. {@fig:performSyn}d the Wasserstein distance between the true and estimated distributions for each state is much lower than the distance for any two distributions that are considered the same (Fig. {@fig:wass}b). On the population level, the transition and starting probabilities were accurately estimated (Fig. {@fig:performSyn}f–g). Thus, we are confident that, with similar experimental data, we should derive accurate results.

![**Model performance on censored lineages of increasing breadth and depth.** (a) Two state populations of increasing breadth (increasing number of lineages or initial cells) and of increasing depth (increasing experiment time) are analyzed. The states are shown in green and blue colors and red shows cell death. The model performance is shown based on (b) state assignment accuracy, (c) the error between the estimated and the true transition rate matrix and the (d) initial probability vector. In (e-f) it shows the accuracy in estimating the Bernoulli parameters for G1 and S/G2 phase, respectively, and (g) depicts the distance between the true and estimated Gamma distributions associated with phase lengths for the two states.](./output/figure5.svg){#fig:performSyn}

### Lineage information improves cell state identification

Cells of even very distinct molecular states can have partly overlapping phenotypes. Therefore, we sought to evaluate how different two states would need to be for us to accurately identify them as distinct (Fig. {@fig:wass}a). We varied the G1 phase duration of two states from identical to very distinct (Fig. {@fig:wass}b) and quantified the accuracy of our model. While the phenotypic observation of a given state had to be different for our model to accurately assign cells, even partly overlapping phenotypes could be distinguished by using the lineage relationships of cells (Fig. {@fig:wass}c). As a baseline comparison, we used k-means clustering to cluster cells based on their phenotype without using their lineage relationships (Fig. {@fig:wass}c). A tHMM consistently out-performed this approach.  The model performance in censored and uncensored populations were similar (Fig. @fig:wass1, @fig:wass2). This shows that the heritability of a cell state can be used to more accurately identify cells with partially overlapping phenotypes.

![**Model performance versus the Wasserstein distance between states.** (a) Cartoon of how two states can vary in their phenotypic similarity. (b) The distribution of G1 duration is varied in state 1 (blue) while the other state is kept constant. (c) State assignment accuracy versus the Wasserstein distance between state phenotypes.](./output/figure6.svg){#fig:wass}

### Likelihood-based model selection can effectively identify the number of distinct states

One does not usually know the number of distinct cell states within a population. Further, the number of distinct states may depend on the environmental context of the cells, particularly because we use phenotypic measurements. To test whether we could infer the number of distinct states, we performed model selection using the Akaike information criterion (AIC) and models with varying numbers of states (Fig. @fig:sAIC). The predicted number of cell states was predominantly correct, and incorrect predictions still centered around the true answer, for both uncensored and censored lineages (Fig. @fig:sAIC). This indicates that model selection can help to identify the appropriate number of cell states for a given set of measurements.

![**Model selection effectively identifies the number of distinct states.** (a)-(d) Model AIC for uncensored lineages with 1–4 states. (e)-(h) Model AIC for censored lineages with 1–4 states. AIC values are normalized such that the optimum is equal to 0. Histograms are shown for the minimal AIC over repeated analyses.](./output/figure8.svg){#fig:sAIC}

### tHMM infers multiple distinct subpopulations in experimental drug response data

We used phenotypic measurements of the G1 and S/G2 phase durations and fates in AU565 cells upon gemcitabine and lapatinib treatment as an application of our model. First, we determined the number of distinct states the model inferred within these populations. Cells were imaged every 30 minutes for 96 hours and then tracked over time. The model was fit to the drug treatment data across all conditions, holding the initial and transition probabilities constant across concentration but allowing the phenotype emissions to independently vary in each condition. The tHMM model inferred different numbers of distinct states for each drug (Fig. {@fig:expAIC}a-b).


![**AIC-based selection inferred the likely number of phenotypically distinct subpopulations.** (a) Normalized AIC values for lapatinib-treated cells. (b) Normalized AIC values for gemcitabine-treated cells. For both drugs the AIC metric was subtracted by the minimum value observed, such that the most likely number of distinct states is equal to 0.](./output/figure9.svg){#fig:expAIC}

### Identified subpopulations own unique properties in drug-treated experimental data

Realizing the most likely number of distinct subpopulations in a data is most valuable when it is accompanied with the quality of each subpopulation. To find out what information each state holds and learning about unique properties of each subpopulation, we plotted the observed measurements for each state, separately. The following two sections discuss our findings for lapatinib and gemcitabine-treated data.

#### tHMM infers fairly stable subpopulations for lapatinib-treated data

To visualize the properties of the states that the model has identified, we plotted the distribution of average phase-specific time duration for each state and each condition. Figs. {@fig:emissionsLPT}a-d accompanied with the transition probability plot (Fig. {@fig:emissionsLPT}i) show that treatment with lapatinib leads to three fairly stable states. As expected, lapatinib mostly influences G1 phase where it extend the duration of this phase in all states (Fig. {@fig:emissionsLPT}e) and leaves G2 progression rates almost unchanged (Fig. {@fig:emissionsLPT}f). Fig. @fig:emissionsLPT e also infers extension of G1 phase mostly captured in cells of state 1 and 2, and cell death mostly happens in state3.

![**State-specific emissions of the lapatinib-treated data.** (a-d) Distribution of phase lengths for each state and for each condition in lapatinib-treated cells. (e-f) G1 and G2 progression rates for different concentrations, respectively. (e-f) G1 and G2 death rates for different concentration, respectively. (i) Transition graph showing the probability of state transition.](./output/figure11.svg){#fig:emissionsLPT}

#### Gemcitabine treatment leaves stable and cycle states in the cell population

Increasing the concentration in gemcitabine-treated trials shows a trend of extending phases and cell death in both phases, especially in G2 (Figs. {@fig:emissionsGMC}a-d). This realization is also evident in the estimated progression and death rates where we see variations between different concentrations (Figs. {@fig:emissionsGMC}e-h). From the transition graph (Fig. {@fig:emissionsGMC}i) states 1 and 3 form a cycle while state 2 is fairly stable. We can conclude that gemcitabine has cell death effects in both phases of state 2 cells, but mostly G2 cell death in state 1, and G1 cell death in state 3. 

![**State-specific emissions of the gemcitabine-treated data.** (a-d) Distribution of phase lengths for each state and for each condition in gemcitabine-treated cells. (e-f) G1 and G2 progression rates for different concentrations, respectively. (e-f) G1 and G2 death rates for different concentration, respectively. (i) Transition graph showing the probability of state transition.](./output/figure12.svg){#fig:emissionsGMC}


## Discussion

The model classified all types of synthetic populations of 2 true states with the accuracy higher than 90% for a minimum of ~50 cells in the population. In the cases with fewer number of observation types the accuracy reached almost 100%, however, slightly less accurate with phase-specific observations. The model showed relatively high sensitivity to the populations with under-represented sub-populations and proved efficacious with more distinct state features. Particularly in comparison to K-means clustering algorithm, the average accuracy of state assignment was higher by $15%$. Missing information in the form of time censorship did adversely affect the performance, however, we were able to handle the influence to be minimum. The model selection validated by AIC metric asserted the reliability of tHMM in predicting the most likely number of states within a population.

There are some lineages, however, on which the tHMM performed poorly, in particular lineages with less than 5 cells when they are evaluated for more than 3 states. Also, the model is dependent on the distance between the existing states and may perform poorly when the states are close or when the susceptible cells possessed high variance in parameter estimation. The deviations are also seen in the resistant cells, as some of the exponential estimates were orders of magnitude higher than the true value. The Gamma estimator, similar to any other lifetime distribution, suffered from survivorship bias due to removal of unfinished cells that were still alive at the end of the tracking period. Specifically, cells with longer lifetimes (i.e. higher growth rate) are more likely to live beyond the tracking period. We separated the censored and fully observed values and handled the censored values using a survival function. This unavoidable phenomenon, if not properly handled, could lead to the growth rate parameter approaching a value less than the true value and biased estimation. Although Bernoulli estimations are centered around their respective true values, they suffer from survivorship bias as well because cells with higher Bernoulli parameter divide more often and thus have a higher sample size for prediction. This leads to the resistant cell line possessing more accurate Bernoulli estimations relative to the susceptible subpopulation.

The tHMM accuracy performs maximum likelihood estimation using cell observations from each lineage in the population. Thus, the improved performance accuracy and decrease in its variance as lineage number increases validates the model architecture. Parameter estimation and initial and transition probability matrix estimations were accurate in most cases of synthetic data and the tHMM was able to better distinguish the separate subpopulations as more lineages were added. Furthermore, the model operates equally well whether the population of interest owns a pre-existing phenotypic heterogeneity or the cells acquire diverse phenotypes as a result of drug treatment.

In this work, we present a machine learning pipeline, the tHMM, that can analyze tree-structured data using any measurements from the parent and daughter nodes. In particular, we apply our algorithm to a cell imaging protocol that inputs cell fate and G1 and S/G2 phase lengths into the tHMM pipeline and can be used with time-lapsed images for real-time classification. The tHMM is able to construct and analyze cell lineage trees to properly assign cells to different states based on virtually any number of phenotypic properties of cell fitness (in the case of our data, three), and also quantify the likelihood of transitioning to a different state using emissions and the transition rate matrix. Utilizing the AIC metric, the model predicted 3 and 4 distinct subpopulations for lapatinib and gemcitabine-treated data, respectively. We are designing assays to experimentally validate the number of states predicted by tHMM. The current version of this pipeline is most accurate when populations consist of at least 50 cells per lineage. Cell transitions from therapy-susceptible to therapy-resistant states are well detected by the model, which will prove useful for identifying mutant subtypes in tumors and leading to more optimal therapies for cancer treatment. The tHMM may further be used for drug screening as a single-cell, rather than population-based, means of quantifying the potency of novel therapies in eliminating all subpopulations within a tumor. The pipeline will provide researchers and clinicians with an improved classification of heterogeneity among cells, or any other tree-structured data, and provide information about latent changes in cellular identity.



## Materials and Methods

### Lineage tree-based hidden Markov model

The core assumption of a Markov chain is that the next state and current observation (in our case cells) are only dependent on the current state. Proof of many of the expressions below can be found in prior work [@doi:10.1109/TSP.2004.832006]. With a lineage of cells and observations from each cell, we aim to use a lineage tree-based hidden Markov model to predict the specific states that each cell is in and the estimated phenotype distributions for each state. The tHMM is composed of several intermediate steps to carry out prediction and estimation.

#### Model flow

The initial probabilities of a cell being in state $k$ are represented by the vector $\pi$ that sums to 1:  
$$\pi_k = P(z_1 = k), \qquad k \in \{1, ..., K\}$$  
The probability of state $i$ transitioning to state $j$ is represented by the $K \times K$ matrix $T$ in which each row sums to 1:   
$$T_{i,j} = T(z_i \rightarrow z_j) = P(z_j \;| z_i), \qquad i,j \in \{1, ..., K\}$$  
The emission likelihood matrix $EL$ is based upon the cell observations. It is defined as the probability of an observation conditioned on the cell being in a specific state:  
$$EL(n,k) = P(x_n = x | z_n = k)$$

Separate emissions observations were assumed to be independent. Since the hidden states are unobserved, we applied an expectation-maximization (EM) algorithm, also called Baum-Welch for hidden Markov models. EM requires two steps: (1) the expectation (E) step in which given the whole tree, the probability of a cell and its parent being in specific states are calculated, so for every cell and every state we have $P(z_n = k \;| X_n)$ and $P(z_n = k,\; z_{n+1} = l \; | X_n)$, respectively. The E step is calculated using the upward and downward recursion algorithms. The second step is the M step, which fits the emissions distributions to the state-assigned cells. The process is repeated until convergence.

#### Upward and downward recursion

An _upward-downward_ algorithm for smoothed probabilities in tree hidden Markov model has been previously proposed to avoid underflow when calculating these two probability matrices [@doi:10.1109/TSP.2004.832006]. To explain we need to introduce the following definitions:

- $p(n)$ is noted as the parent cell of the cell $n$, and $c(n)$ is noted as children of cell $n$.
- $\bar{X}$ is the observation of the whole tree and $\bar{X}_a$ is a subtree of $\bar{X}$ which is rooted at cell $a$. Also, $\bar{Z}$ is the complete hidden state tree.
- $\bar{X}_{a/b}$ is the subtree rooted at $a$ except for the subtree rooted at cell $b$, if $\bar{X}_b$ is a subtree of $\bar{X}_a$.

For state prediction in tHMM model we start by calculating the marginal state distribution (MSD) matrix. MSD is an $N \times K$ matrix that for each cell is marginalizing the transition probability over all possible current states by downward traversing from root to leaf cells:  
$$MSD(n,k) = P(z_{n} = k)= \sum_{i} P(z_n = k |z_{n-1} = i)\times P(z_{n-1} = i)$$

During upward recursion, the flow of upward probabilities is calculated from leaf cells to the root cells generation by generation. For leaf cells, which are the base case to start with the $\beta$s are calculated by:  
$$\beta(n,k) = P(z_n = k\;|X_n = x_n) = \frac{EL(n,k) \times MSD(n,k)}{NF_l(n)}$$

in which $X_n$ is the leaf cell's observation, and NF (Normalizing Factor) is an $N \times 1$ matrix that is the marginal observation distribution. Since $\sum_{k} \beta_n(k) = 1$, we find the expression for NF for leaf cells is:  
$$NF_l(n) = \sum_{k} EL(n,k) \times MSD(n,k) = P(X_n = x_n)$$

For non-leaf cells the upward values are given by:  
$$ \beta(n,k) = P(z_n = k\;|\bar{X}_n = \bar{x}_n) = \frac{EL(n,k) \times MSD(n,k) \times \prod_{v \in c(n)}\beta_{n,v}(k)}{NF_{nl}(n)}$$

in which we can extract non-leaf NF such that:  
$$NF_{nl}(n) = \sum_{k} \Big[EL(n,k) \times MSD(n,k) \prod_{v \in c(n)} \beta_{n,v}(k)\Big]$$

and linking $\beta$ between parent-daughter cells is given by:  
$$ \beta_{p(n), n}(k) = P(\bar{X}_n = \bar{x}_n | z_{p(n)} = j) = \sum_{j} \frac{\beta_n(j) \times T_{k,j}}{MSD(n,j)}$$

By recursing from leaf cells to root cells, $\beta$ and NF matrices are calculated as upward recursion. Calculating the NF matrix gives a convenient expression for the log-likelihood of the observations. For the root cell we have:

$$P(\bar{X} = \bar{x}) = \prod_{n} \frac{P(\bar{X}_n = \bar{x}_n)}{\prod_{v\in c(n)} P(\bar{X}_v = \bar{x}_v)} = \sum_{n} NF(n) \qquad n \in \{1, ..., N\}$$

As a conclusion:  
$$log P(\bar{X} = \bar{x}) = \sum_{n} log NF(n)$$

This helps with keeping track of the log-likelihood which as a measure of convergence of the EM algorithm.

For computing downward recursion, we need the following definition starting from the root cells:  
$$ \gamma_1(k) = P(z_1 = k | \bar{X}_1 = \bar{x}_1) = \beta_1(k)$$

Other cells follow in a $N \times K$ matrix by writing the conditional probabilities as the summation over the joint probabilities of parent-daughter cells:  
$$\gamma_n(k) = P(z_n = k | \bar{X}_1 = \bar{x}_1) = \frac{\beta_n(k)}{MSD(n,k)} \sum_{i}\frac{T_{i,k} \gamma_{p(n)}(i)}{\beta_{p(n),n}(i)}$$

#### Viterbi algorithm

Given the sequence of observations in a hidden Markov chain the Viterbi algorithm is commonly used to find the most likely sequence of states. Equivalently, here it returns the most likely sequence of states of the cells in a lineage tree by taking advantage of upward and downward recursion [@doi:10.1109/TSP.2004.832006].

Viterbi follows from a upward recursion from leaf cells to the root, meaning we first define the values for the leaf cells and move to parent cells up to the root. We define $\delta$, an $N \times K$ matrix:

$$\delta (n,k) = \max\limits_{\bar{z}_{c(n)}}\{P(\bar{X}_n = \bar{x}_n, \bar{Z}_{c(n)} = \bar{z}_{c(n)} | z_n = j)\}$$
and the links between parent-daughter cells as:  
$$\delta_{p(n),n}(k) = \max\limits_{\bar{z}_n} \{P(\bar{X}_n = \bar{x}_n, \bar{Z}_n = \bar{z}_n | z_{p(n)} = j)\} = \max\limits_{j}\{\delta(n,j) T_{k,j}\}$$
So we initialize from the leaf cells as:  
$$\delta(n,k) = P(X_n = x_n | z_n = k) = EL(n,k)$$
and for non-leaf cells we have:  
$$\delta(n,k) =  \Big[\prod_{v \in c(n)} \delta_{n,v}(k)\Big]\times EL(n,k)$$
The probability of the optimal state tree corresponding to the observations tree, assuming root cell is noted as cell 1, is given by:
$$Z^* = \max\limits_{k}\{\delta(1,k) \pi_k \}$$
which arises from maximization over the conditional emission likelihood (EL) probabilities by factoring out the root cells as the outer maximizing step over all possible states.

#### Baum-Welch algorithm

In order to estimate the parameters corresponding to the hidden Markov models, Baum-Welch algorithm is used which employs the EM algorithm to find the maximum likelihood of the parameters. Here, we estimate $\theta = (\pi, T, p, a, s)$ the initial and transition probability matrices, the parameters of the observation distributions, namely Bernoulli parameter, shape, and scale parameter of Gamma distribution by maximizing the probability of the observations given the parameters; in other words $\theta^* = \max\limits_{\theta} P(X, Z|\theta)$, that is maximizing the joint probabilities.

$$ \xi_n(j,k) = P(z_n = j, z_{p(n)} = i | \bar{X}_1 = \bar{x}_1)$$
According to Bayes theorem, we can write the above probability in a joint form, and since $P(\bar{X}_1) = \bar{x}_1$ is the EL probabilities of the whole tree, it is just a constant coefficient and we can ignore it.  
So we could write it as:  
$$ \xi_n(j,k) = \frac{\beta(n+1, k) \times T_{j,k} \times \gamma_j(n)}{MSD(n+1, k) \times \beta_{p(n),n}(j)}$$
The maximum likelihood estimation of the initial probabilities:  
$$ \pi^*_k = \gamma_1(k)$$
The transition probability matrix would be estimated as:  
$$ T^*_{i,j} = \frac{\sum_{n=1}^{N-1} \xi_n(i,j)}{\sum_{n=1}^{N-1} \gamma_n(i)} $$

To estimate the distribution parameters after finding the most likely state for each cell, we group them and group their observations based on their estimated state and pass them to _StateDistribution_ class for maximum likelihood estimation. For estimating the Bernoulli parameter we simply find the sample mean of the observations for each state. Assuming we have $N_1$ data points estimated in state 1, the corresponding Bernoulli parameter for state 1 would be:

$$ p^*_1 = \frac{\sum_{i=1}^{N_1} x_b(i)}{N_1}$$
And for Gamma distribution parameters we use a closed-form estimation based on \cite{gamma_estimation} which has been corrected for bias:  
$$ a^* = \frac{N_1 \times  \sum_{i=1}^{N_1} x_g(i)}{\Big[N_1 \times \sum_{i=1}^{N_1} x_g(i) ln(x_g(i))\Big] - \sum_{i=1}^{N_1} ln(x_g(i)) \times \sum_{i=1}^{N_1} x_g(i)} $$
$$ s^* = \frac{1}{N_1^2} \times \Big[N_1 \times \sum_{i=1}^{N_1} x_g(i) ln(x_g(i)) - \sum_{i=1}^{N_1} ln(x_g(i)) \times \sum_{i=1}^{N_1} x_g(i) \Big]$$

### Synthetic lineage data

We generated synthetic lineage trees with $K$ discrete states and $N$ total number of cells for benchmarking. Lineages were composed of two primary data structures, the state and emissions trees. The state tree was randomly seeded with a root cell determined by the starting probabilities, then expanded by randomly sampling transitions based on the transition probability matrix. After creating the state tree with the desired number of cells, the emission tree is built upon it. Emissions were randomly sampled from the distributions for each cell’s state. Finally, the effects of the emissions were applied to the tree when necessary. If any cells died, their progeny were marked as unobserved by making their emissions NaN values. If applicable, the effects of finite-duration experiments were also applied. Cells existed outside of the experiment duration were similarly marked as unobserved, and those crossing the bounds of an experiment were marked as censored.

### Experimental single-cell lineage data

The data includes AU565 breast cancer cell line for control condition along with 7 concentrations of 2 types of targeted or chemotherapy compounds including lapatinib and gemcitabine. A fluorescent reporter was developed to translocate between the nucleus and cytoplasm to indicate the phase of the cells. Each cell is indicated as being in G1 or S/G2 phase according to the location of the reporter. When the reporter is located in the nucleus it means the cell is in G1 and when the reporter in the cytoplasm, the cell is passing through S/G2 phase. Each experiment lasts for 96 hours where the plates were being imaged every 30 minutes and each experiment was repeated three times. Single cells were manually tracked to collect cell fate in either phase or the amount of time it takes for each cell to pass through G1 and S/G2 phases.

#### Strategies to overcome model fitting to censored data

In single-cell experimental data collection, the lineages are almost never fully observed, in other words, we experience missing data for cells with time or fate censorship. Those leaf cells living at the end of the collected lineage trees, which may have been in their G1 or S/G2 exactly when the experiment was finished, experience a right-censorship, meaning, we have missing data from the future. For a cell that was in G1 at the end of the experiment, the time that the cell transitions to S/G2 is unknown, hence the cell's G1 is censored. In a similar way, almost all of the root cells appearing at the very beginning of the experiment are left-censored. This way, given a population of cells, we identify whether any of the cell's observations are censored or not. The uncensored values are passed to the estimator while the censored values will be handled by the survivor function. 
Another similar challenge is the unobserved measurements when cells die and their descendants disappear or when a leaf cell reaches the experiment end time while it is in the G1 phase such that the S/G2 phase for this cell is unobserved. We simply remove those measurements that have not been observed at all.

### Computational tools to explore the model

In this part we briefly mention the measures we used to monitor the goodness of the fit of the model. 

**AIC**  
In order to find the most likely number of states corresponding to the observations, Akaike Information Criterion (AIC) is used. This could be considered as an approach for model selection that could inform us of the most likely number of states, and also it deals with the trade off between over-fitting and under-fitting [@doi:10.1006/jmps.1999.1276].
Degrees of freedom: Our model estimate a $k \times 1$ initial probability matrix, a $k \times k$ transition matrix, and a $k \times m$ matrix of state-wise parameters where $k$ is the number of states and $m$ is the number of parameters associated with observation distributions. For the phase-specific observation sets we have a total of 6 parameters including 2 Bernoulli parameters and 2 pairs of shape and scale parameters for Gamma distribution. Since the row-sums for transition and initial probability matrices must be 1, these values are not independent. 
From distribution analysis of the phase lengths, we realized the shape parameter of the Gamma distribution remains fairly constant over different conditions, while the scale parameter changes. Removing the shape parameters of G1 and S/G2 for each states, instead of $k \times (k - 1) + (k - 1) + k \times (m)$ degrees of freedom, we will have $k \times (k - 1) + (k - 1) + k \times (m-2)$.

**Wasserstein distance**  
Wasserstein or Kantorovich–Rubinstein metric, is a measure of distance between two distributions. This metric was used to determine the difference between state emissions [@doi:10.1137/1118101]. When calculating the distance for a gamma distribution we used the analytical solution, the absolute value of the difference in distribution means.

### Model benchmarking

In this model, we use multivariate emission distributions to represent the physical characteristics of the cells within the lineages. To create our synthetic data we considered two possible options as our set of observations throughout an experiment. First, cell fate and cell lifetime, and second, phase-specific fate and time duration, for which we used Bernoulli and Gamma distributions. For the consistency of our model, we set a specific set of parameters for those mentioned distributions in each case. The following is the collection of distribution parameters for two-state synthetic data.

#### Phase non-specific observations
The parameters are reflective of fitting the model to data of 5 nM lapatinib treatment. Figures @fig:prop4, @fig:real_5, @fig:performUncenSingle, @fig:performUncenMulti, and @fig:performCenMulti are based on these parameters.

| State | Bern p | Shape | Scale |
| :---: |  :---: | :---: | :---: |
|State 1 | 0.99 | 8 | 6 |
| State 2 | 0.75 | 8 | 1 |


#### Phase specific observations
In Figures @fig:censor, @fig:performSyn, @fig:uncenSingle, @fig:uncenMulti, and @fig:cenMulti the data was created based on the following parameters. These parameters are based on estimations of 5 nM lapatinib treatment.

| State | Bern $G_1$ | Bern $G_2$ | Shape $G_1$ | Scale $G_1$ | Shape $G_2$ | Scale $G_2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| State 1 | 0.99 | 0.95 | 8 | 7 | 4 | 2 |
|State 2 | 0.95 | 0.9 | 6 | 4 | 3 | 5 |


#### Distant emissions

To create synthetic data with subpopulations of varying dissimilarity (Fig. @fig:wass), we use the phase-specific parameters set except that the values for the G1 phase Gamma shape parameter for state 1 is varied between $[4, 12]$. This results in an increase in the Wasserstein distance between the two cell states, allowing us to measure state assignment accuracy for different dissimilarity amounts between the two states.  
Likewise, for Figures @fig:wass1 and @fig:wass2, we used phase non-specific parameters and varied G1 phase Gamma scale parameter between $[1, 8]$ for state 1.

#### Emissions for AIC figures

Figure @fig:sAIC uses a unique set of values for the emissions matrix in order to simulate varying states for the AIC calculation. 


| State | Bern $G_1$ | Bern $G_2$ | Shape $G_1$ | Scale $G_1$ | Shape $G_2$ | Scale $G_2$ |
:---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| State 1 | 0.99 | 0.9 | 10 | 2 | 10 | 2 |
|State 2 | 0.9 | 0.9 | 20 | 3 | 20 | 3 |
| State 3 | 0.85 | 0.9 | 30 | 4 | 30 | 4 |
| State 4 | 0.8 | 0.9 | 40 | 4 | 40 | 5 |

 

## Acknowledgements

This work was supported by U01-CA215709 to A.S.M. **Competing financial interests:** The authors declare no competing financial interests.



## Author contributions statement

A.S.M. and L.M.H. conceived of the study; A.S.M. conceived of the model; A.S.M, F.M., S.V. designed model; A.S.M., F.M., J.L., L.K., S.V. performed computational experiments; S.M.G. performed the experiments; F.M., J.L., L.K., S.M.G. conducted data analysis; A.S.M. and L.M.H. supervised the research; all authors wrote the paper.


## Supplementary Figures

<!-- (Supp. Figure 1) -->
### Performance on uncensored single lineage of increasing size

![**Performance on uncensored single lineages of increasing size.** (a)Visual representation of cells increasing lineage size with varying states. (b) Bernoulli parameter approaches the true value as the number of cells increase for states 1 and 2. (c)-(d) Gamma shape and scale parameters approach the true value for states 1 and 2 as the number of cells increase. (e) State assignment accuracy approaches 100% as the number of cells increase. (f) Errors in estimating the transition probability matrix, T, approaches 0 as the number of cells increase.](./output/figureS01.svg){#fig:uncenSingle}

\pagebreak

<!-- (Supp. Figure 2) -->
### Performance on uncensored multiple lineages of increasing size

![**Performance on uncensored populations of lineages of increasing number.** (a) Visualization of cells increasing in size and number of lineages. (b) Bernoulli parameter approaches the true value for states 1 and 2 as the number of cells increase. (c)-(d) Gamma shape and scale parameters approach the true value as the number of cells increase for states 1 and 2. (e) State assignment accuracy approaches 100% consistently. (f) Errors in estimating the transition probability matrix, T, approaches 0 as the number of cells increase. (g) Errors in estimating the initial probability matrix, π, approaches 0 as the number of cells increase.](./output/figureS02.svg){#fig:uncenMulti}

\pagebreak

<!-- (Supp. Figure 3) -->
### Performance on censored multiple lineages of increasing size

![**Performance on censored multiple lineages of increasing size.** (a) Visualization of cells increasing in size and number of censored lineages. (b) Bernoulli parameter approaches the true value for state 1 as the number of cells increase and approaches the true value between 100 to 200 cells and deviates for larger lineages for state 2. (c) Gamma shape parameter approaches the true value as the number of cells increase for states 1 and 2. (d) Gamma scale parameter approaches the true value consistently for state 2 and as the number of cells increase for state 1. (e) State assignment accuracy approaches 100% as the number of cells increase. (f) Errors in estimating the transition probability matrix, T, approaches 0 as the number of cells increase. (g) Errors in estimating the initial probability matrix, π, approaches 0 as the number of cells increase.](./output/figureS03.svg){#fig:cenMulti}

\pagebreak

<!-- # (Supp. Figure 4) -->
### Change in model performance when varying presence of a state for uncensored population

![**Model performance relative to the presence of each state in uncensored lineages.** (a) Visualization of the distribution of cells in the lineage transitioning from state 1 to state 2. (b) Bernoulli parameter for states 1 and 2 approaches the true value as the proportion of cells in state 1 increase. The Bernoulli paramater deviates from the true value for state 2 when 60% of cells are in state 1. (c)-(d) Gamma shape and scale parameters for states 1 and 2 approach the true value when proportion of cells in state 1 increase. (e) State assignment accuracy approaches 100% consistently as the proportion of cells in state 1 increase. (f) Errors in estimating the transition probability matrix, T, approaches 0 consistently.](./output/figureS04.svg){#fig:prop4}

<!-- (Supp. Figure 5) -->
### Change in model performance when varying presence of a state for censored population 

![**Performance on populations of censored lineages of increasing number.** (a) Visualization of the proportion of cells in the censored lineage transitioning from state 1 to state 2. (b) Bernoulli parameter for states 1 and 2 approach the true value as the proportion of cells in state 1 increase. The Bernouli parameter deviates from the true value for state 2 when 60% of cells are in state 1. (c)-(d) Gamma shape and scale parameters for states 1 and 2 approach the true value as the proportion of cells in state 1 increase. (e) State assignment accuracy approaches 100% then decreases when approximately 85% of cells are in state 1. (f) Errors in estimating the transition probability matrix, T, approaches 0 consistently.](./output/figureS05.svg){#fig:real_5}

\pagebreak

<!-- (Supp. Figure 6) -->
### Change in model performance when varying state distribution similarity for uncensored populations

![**Change in model performance when varying state distribution similarity with an uncensored population of lineages.** (a) Visualization of the Wasserstein Divergence increasing as the state distribution in the lineage varies. (b) Bernoulli parameter consistently approaches the true value for states 1 and 2 as the Wasserstein Divergence increases. (c) Gamma shape parameter deviates from the true value as the Wasserstein Divergence exceeds 20. (d) Gamma scale parameter approaches the true value for states 1 and 2 as the Wasserstein Divergence increases. (e) State Assignment Accuracy approaches 100% as the Wasserstein Divergence increases. (f) Errors in estimating the transition probability matrix, T, approaches 0 as the Wasserstein Divergence increases.](./output/figureS06.svg){#fig:wass1}

\pagebreak

<!-- (Supp. Figure 7) -->
### Change in model performance when varying state distribution similarity for censored population

![**Change in model performance when varying state distribution similarity with censored lineages.** (a) Visualization of the Wasserstein Divergence increasing as the state distribution in the censored lineage varies. (b)-(d) Bernoulli, Gamma shape, and Gamma scale parameters consistently approach the true value as the Wasserstein Divergence increases. (e) State Assignment Accuracy approaches 100% as the Wasserstein Divergence increases. (f) Errors in estimating the transition probability matrix, T, approaches 0 as the Wasserstein Divergence increases.](./output/figureS07.svg){#fig:wass2}

\pagebreak

<!-- (Supp. Figure 8) -->
### Performance on uncensored single lineage of increasing size given phase specific observations

![**Performance on uncensored single lineages of increasing size.** (a) Visualization of a single lineage increasing in size. (b) Bernoulli parameter approaches the true value for states 1 and 2 as the number of cells increase in the G1 phase. (c)-(d) Gamma shape and scale parameters approach the true value for states 1 and 2 as the number of cells increase in the G1 phase. (e) Bernoulli parameter approaches the true value for states 1 and 2 as the number of cells increase in the G2 phase. (f) Gamma shape parameter consistently approaches the true value for states 1 and 2 as the number of cells increase in the G2 phase. (g) Gamma scale parameter approaches the true value for states 1 and 2 as the number of cells increase in the G2 phase. (h) State assignment accuracy approaches 100% as the number of cells increase. (i) Errors in estimating the transition probability matrix, T, approaches 0 as the number of cells increase and increases past 90 cells.](./output/figureS08.svg){#fig:performUncenSingle}

\pagebreak

<!-- (Supp. Figure 9) -->
### Performance on uncensored lineages of increasing number given phase specific observations

![**Performance on uncensored populations of lineages of increasing number.** (a) Visualization of the number of uncensored lineages within a population increasing. (b)-(d) The Bernoulli, Gamma shape, and Gamma scale parameters approach the true value for states 1 and 2 as the number of cells increase in the G1 phase. (e)-(g) The Bernoulli, Gamma shape, and Gamma scale parameters approach the true value for states 1 and 2 as the number of cells increase in the G2 phase. (h) The state assignment accuracy approaches 95% approximately as the number of cells increase. (i) Errors in estimating the transition probability matrix, T, approaches 0 as the number of cells increase. (j) Errors in estimating the initial probability matrix, π, approaches 0 as the number of cells increase.](./output/figureS09.svg){#fig:performUncenMulti}

\pagebreak

<!-- (Supp. Figure10) -->
### Performance on censored multiple lineages of increasing size given phase specific observations

![**Performance on censored multiple lineages of increasing size.** (a) Visualization of the number of censored lineages within a population increasing. (b)-(d) The Bernoulli, Gamma shape, and Gamma scale parameters approach the true value for states 1 and 2 as the number of cells increase in the G1 phase. (e)-(g) The Bernoulli, Gamma shape, and Gamma scale parameter approach the true value for states 1 and 2 as the number of cells increase in the G2 phase. (h) The state assignment accuracy approaches 95% approximately as the number of cells increases. (i) Errors in estimating the transition probability matrix, T, approaches 0 as the number of cells increases. (j) Errors in estimating the initial probability matrix, π, approaches 0 as the number of cells increase.](./output/figureS10.svg){#fig:performCenMulti}


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
