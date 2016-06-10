# Neptune Computational Biology - Final Project


OK, here we go.

# Identifying cells of interest from single cell sequence data

## Introduction and Goals

Annelids are a diverse group of animals thriving in a variety of lifestyles. Comparison of cell types among closely/distantly related species (or species with different lifestyles) will give insights on the evolution of specific cell types. Recent single cell sequencing techniques have made it possible to isolate cells and derive the transcriptome of individual cells.
I have transcriptomic data from single cell sequencing of a polychaete larvae. The dataset is from approximately 50 cells isolated from 4 day old larvae. I'm particularly interested in the photoreceptor cells. The raw data consists of reads from multiplexed samples. I will simulate a multiplexed dataset similar to what I already have. Then I will demultiplex the data into 50 sets each representing an individual cell. 

# Steps

## Creating multiplexed data

Since I do not have access to my data I will generate reads from the Nasuia deltocephalinicola genome. I will not use Public RNAseq data as the files are very large. I will use Python scripting to add barcodes to the reads in a random manner.  

## Demultiplexing of raw data

The starting dataset is a multiplexed sample of 50 cells containing 50 unique indices. The first step is to demultiplex the sample dataset by identifying the indices and segregating the sample into 50 sets. There are tools available to demultiplex the sample.  

## Mapping of reads 

The reads can be mapped either to a reference transcriptome (which is already available) or to known sequences (for desired read counts) using Bowtie aligner.

## Generating read counts


## 


# Methods

Python scripting - Multiplexing and demultiplexing

Axe-demultiplexer - Demultiplexing of barcoded reads

Bowtie - Sequence mapping

RSEM - Quantifying genes and isoforms


# Results

## Data simulation

Using sim_reads I simulated a single sequence set containing 33610 single reads (from Nasuia deltocephalinicola genome).

Four different barcodes were tagged to the reads in random using Python.

Used axe-demultiplexer to separate the reads into four datasets according to their barcode.


## Discussion

These results indicate....

The biggest difficulty in implementing these analyses was the starting point.

If I did these analyses again, I would be slightly faster.

## References


