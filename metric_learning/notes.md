# Take note

## What affect metric learning

* **Sampling method**
* **Loss function**

## Problem of each loss function

**Contrastive loss problem:**

* positive points always collapse
* use margin D for all class distance cause space distortion

**Triple loss problem:**

* So many triplet --> huge dataset
* Positvie points always collapse. Because loss function always chooses to decrease positive distance than negative distance.

## Problem of sampling

**Random sampling:** choose insignificant pairs to training --> slow converge, terrible performance

**Hard negative sampling:** choose so few pairs --> cannot describe all datasets

**Semi-hard negative sampling:**
(TO DO)

## How create data in triplet loss learning

Offline sampling: create triplet after several eppchs

Online sampling: create triplet in a batch 