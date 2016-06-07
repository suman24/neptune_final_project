# Neptune Computational Biology - Final Project

## Guidelines - you can delete this section before submission

This repository is a stub for your final project. Fork it, develop your project, and submit it as a pull request. Edit/ delete the text in this readme as needed.

Some guidelines and tips:

- Use the stubs below to write up your final project.

- For information on formatting text files with markdown, see https://guides.github.com/features/mastering-markdown/ . You can use markdown to include images in this document by linking to files in the repository, eg `![Figure 1](./Figure1.png?raw=true)`.

- The project must be entirely reproducible. In addition to the results, the repository must include all the data (or links to data) and code needed to reproduce the results.

- If you are working with unpublished data that you would prefer not to publicly share at this time, please contact me to discuss options. In most cases, the data can be anonymized in a way that putting them in a public repo does not compromise your other goals.

- Paste references (including urls) into the reference section, and cite them with the general format (Smith at al. 2003).

- Commit and push often as you work.

OK, here we go.

# Identifying cells of interest from single cell sequence data

## Introduction and Goals

I have transcriptomic data from single cell sequencing of a polychaete larvae. The dataset is from approximately 50 cells isolated from 4 day larvae. My cells of interest are photoreceptor cells. My first part of the project will be to go through the data and see if my cells of interest exist. Next part of the project will be to identify more cell types using additional marker genes. I will simulate a dataset similar to what I already have. There will be 20-30 samples each sample representing an individual cell. Using few marker genes, the dataset will be probed by running a BLAST. The marker genes will be chosen from the simulated dataset to achieve a working method which can be extended to my actual data at a later stage.

## Steps

Demultiplexing of raw data

The starting dataset is a multiplexed sample of 50 cells containing 50 unique indices. The first step is to demultiplex the sample dataset by identifying the indices and separating the sample into 50 sets.

Mapping to known opsin sequences







## Methods

Python/Shell?

BLAST


## Results

![Figure 1](./Figure1.png?raw=true)

In Figure 1...

## Discussion

These results indicate...

The biggest difficulty in implementing these analyses was...

If I did these analyses again, I would...

## References


