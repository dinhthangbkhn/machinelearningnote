# Struggling with data imbalance? Semi-supervised & Self-supervised learning help

## Reference paper

NeurIPS 2020: Rethinking the Value of Labels for Improving Class-Imbalanced Learning.

## Introduction

Problem:  
the classification problem under the imbalance of data categories (also referred to as the long-tailed distribution of data)

Result:
semi-supervised and self-supervised learning can significantly improve learning performance under imbalanced data.

* Semi-supervised learning: using more unlabeled data
* Self-supervised learning: without using any extra data, just by first doing one step of self-supervised pre-training without label information on the existing imbalanced data,

## Problem of imbalanced data

### Sample of imbalanced data in real world

The amount of data of different categories will generally not be an ideal uniform distribution, but will often be imbalanced.  
If you sort the classes according to the number of samples from high to low, you will find that the data distribution has a **“long tail”**

![img](img/imbalanced%20data%20sample.png)

### What is problem with imbalanced or long-tailed data

The model will learn better on the samples of major classes, but generalize poorly on minor classes

### What are the current solutions to the imbalanced learning problem

1. Resampling
   * Over sampling the minortity samples: easy to overfit to the minor class and cannot learn more robust and generalizable features -> often perform bad on very imbalanced data
   * Under sampling the majority samples: cause serious information loss in the major class, leading to underfitting
2. Synthetic samples
   * generating “new” data similar to the minority samples
   * Ex: SMOTE uses K nearest neighbors to select similar samples for randomly selected minority samples, and obtain new samples by linear interpolation
3. Reweighting
    * Assign different weights to different categories (or even different samples)
    * The simplest is to weight according to the reciprocal of the number of categories
4. Transfer learning
    * model the majority class and the minority class separately, and transfer the learned information/representation/knowledge of the majority to the minority
5. Metric learning
    * it hopes to learn better embedding and better model the boundary/margin near the minority classes
6. Meta learning/domain adaptation
    * Different processing of the head and tail data can be used to adaptively learn how to re-weight, or formulate the problem as a domain adaptation problem.

However, under extreme data imbalance, the degradation of deep model performance is still widespread. Therefore, we need to pay attention to understand the impact of the imbalanced data label distribution 
