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

Annelids are a diverse group of animals thriving in a variety of lifestyles. Comparison of cell types among closely/distantly related species (or species with different lifestyles) will give insights on the evolution of cell types. Recent single cell sequencing techniques have made it possible to isolate cells and derive the transcriptome of individual cells.
I have transcriptomic data from single cell sequencing of a polychaete larvae. The dataset is from approximately 50 cells isolated from 4 day old larvae. I'm particularly interested in the photoreceptor cells. The raw data consists of reads from multiplexed samples. I will simulate a dataset similar to what I already have. There will be 20-30 samples, each sample representing an individual cell. 

# Steps

## Demultiplexing of raw data

The starting dataset is a multiplexed sample of 50 cells containing 50 unique indices. The first step is to demultiplex the sample dataset by identifying the indices and segregating the sample into 50 sets. There are tools available to demultiplex the samples. However, I will write a python script to demultiplex the dataset. 

## Mapping of reads 

The reads can be mapped either to a reference transcriptome (which is already available) or to known sequences (for desired read counts) using Bowtie aligner.

## Generating read counts


## 


## Methods

Python/Shell - Multiplexing and demultiplexing

Axe-demultiplexer - Demultiplexing of barcoded reads

Bowtie - Sequence mapping

RSEM - Quantifying genes and isoforms


## Results

# Data simulation

Using sim_reads I simulated a single sequence set containing 33610 reads (from Nasonia genome).

Four different barcodes were tagged to the reads in random using Python.

Used axe-demultiplexer to separate the reads into four datasets according to their barcode.


## Discussion

These results indicate....

The biggest difficulty in implementing these analyses was the starting point.

If I did these analyses again, I would be slightly faster.

## References


