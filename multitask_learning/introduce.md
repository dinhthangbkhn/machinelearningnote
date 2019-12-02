# Multitask learning

## 1. Recent work on MTL for Deep Learning

### 1.1 Deep Relationship Networks
matrix priors on the fully connected layers, which allow the model to learn the relationship between tasks, similar to some of the Bayesian models we have looked at before.

This approach, however, still relies on a pre-defined structure for sharing, which may be adequate for well-studied computer vision problems, but prove error-prone for novel tasks.

### 1.2 Fully-Adaptive Feature Sharing
starts with a thin network and dynamically widens it greedily during training using a criterion that promotes grouping of similar tasks

the greedy method might not be able to discover a model that is globally optimal, while assigning each branch to exactly one task does not allow the model to learn more complex interactions between tasks.

### 1.3 A Joint Many-Task Model
Building on this finding, [42] pre-define a hierarchical architecture consisting of several NLP tasks, which can be seen in Figure 6, as a joint model for multi-task learning.

### 1.4 Weighting losses with uncertainty
adjust each task's relative weight in the cost function by deriving a multi-task loss function based on maximizing the Gaussian likelihood with task-dependant uncertainty. Their architecture for per-pixel depth regression, semantic and instance segmentation can be seen in Figure 7.

