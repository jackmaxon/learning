
# Machine Learning Notes

Jack Maxon's notes on Aurélien Géron's *Hands-On Machine learning with Scikit-Learn, Keras & TensorFlow (3rd ed.)*. 
 

## Chapter I - The Machine Learning Landscape

> A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E. 

Tom Mitchell, 1997.

Some basic parameters: 
- Supervised, unsupervised, semi-supervised, self-supervised
- Online versus batch learning

### Training Supervision

In supervised learning, the training set you feed to the algorithm includes the desired solutions, called labels.

In unsupervised learning, the training data is unlabeled. 

Visualization algorithms are fed complex and unlabeled data, and they output a 2D or 3D representation. 

Anomaly detection algorithms are fed mostly normal instances during training, so it learns to recognize them; then, when it sees a new instance, it can tell whether it looks like a normal one or whether it is likely an anomaly. 

Novelty detection algorithms try to detect new instances that look different from all instances in the training set. 

Association rule learning algorithms find connections between events (e.g., people who buy X often also purchase Y).

Semi-supervised learning algorithms take in partially labeled data (discover groups X_i and label each group).

Self-supervised learning involves generating a fully labeled dataset from a fully unlabeled one (mask part of input data, ask it to generate unmasked data, and use the original data as a label).


> Transferring knowledge from one task to another is called *transfer learning*.

Reinforcement learning has an *agent* observe the environment, select and perform actions, and get rewards in return (or penalties). It must learn the best strategy (*policy*) to get the most reward over time. 

### Batch Versus Online Learning 

In *batch learning*, the system is incapable of learning incrementally: it must be trained using all the available data. This computing is typically done offline. When the system is trained, it is deployed into production without learning anymore. This is called *offline learning*.

A models performance tends to decay after time as the world evolves outside of its learning. This is called *model rot* or *data drift*. 

If you want to update a batch learning system, you must start training over from scratch. 

---
In *online learning* (*incremental learning*) you train the system incrementally by feeding it data instances sequentially, either individually or in small groups called *mini-batches*.

Besides being good for limiting compute environments, online learning algorithms can be used to train models on huge datasets that cannot fit in memory (*out-of-core learning*).

An important parameter of online learning systems is how fast they should adapt to changing data: this is called the *learning rate*. 

Feeding bad data into a system will cause the quality of the model to decline.

### Instance-Based Versus Model-Based Learning

In *instance-based learning*, the system learns the examples by hearts (stores them), then generalizes to new cases by using a similarity measure to compare them to the learned examples.

In *model-based learning*, we generalize from a set of examples and then use the model to make *predictions* (i.e., with hard-coded parameters). 

### Challenges

Since our main task is to select a model and train it on data, the two things that can go wrong are "incorrect model" or "bad data". 

We need large data-sets to learn generalization and recognition. We also want this data to be representative of the new cases we want to generalize to. 

If our sample is too small, we will encounter *sampling noise* (non-representative data as a result of chance). If our sampling method is flawed, it doesn't matter how much data we have--this is called *sampling bias*.

If our data is full of errors, outliers, and noise (due to poor quality measurements), it will make it harder for the system to detect the underlying patterns. 

We want our training data to contain enough relevant features and not too many irrelevant ones. *Feature engineering* involves *feature selection*, *feature extraction*, and creating new features by gathering new data. 

### Overfitting, Underfitting

Our model is *overfitted* if it performs well on the training set, but does not generalize well (i.e., a high order polynomial where a linear model would suffice).

We can combat overfitting by:
- Selecting fewer parameters, by reducing the number of attributes in the data, or by constraining the model,
- Gathering more training data,
- Reduce the noise in the data (e.g., fix data errors and remove outliers).

Constraining a model to make it simpler and reduce the risk of overfitting is called *regularization*. 

The amount of regularization can be controlled by a *hyperparameter*, which is a parameter of the learning algorithm itself, not the model. 

A model is *underfitted* if the model is too simple to learn the underlying structure of the data. 

We can combat underfitting by:
- Selecting a more powerful model with more parameters,
- Feed better features to the learning algorithm,
- Reduce the constraints on the model (e.g., reducing the regularization hyperparameter).


### Testing and Validation
Instead of testing our model in production, we can split our data into two sets: the *training set* and the *test set*. The error rate on the test set is called the *generalization error* (or *out-of-sample error*).

It is common to use 80% of data on training, and test on the remaining 20%, though actual amounts depend on the size of the data set. 

Suppose we tune our hyperparameters to minimize error on the test set, but we deploy our model to find it performs poorly. A solution to this is called *holdout validation*, where we hold our part of the training set to evaluate candidate models. The new held-out set is called the *validation set* (or *dev-set*).

This is to say that we train multiple models on the full training set minus the validation set, and we select the model that performs best on the validation set. After this holdout validation, you train the best model on the full training set, yielding the final model. 

Choosing a validation set can pose issues. So we can repeatedly *cross-validate*, using many small validation sets. Each model is trained once per validation set after it is trained on the rest of the data. This slows training time by a factor of validation sets. 

### Data Mismatch
Sometimes the data available to us isn't a good representation of the data that would be used in production. 

If this is the case, the best thing we can do is make sure the validation set and test set are as representative as possible. But if our model does poorly on the validation set, we will not know if we've overfitted to the training set, or if the model struggles with data-mismatch. 

One solution is to create a *train-dev set*. After the model is trained on the training set, to evaluate it on the train-dev set. If the model performed poorly, it must have overfit the training set. If it performs well, you can evaluate it on the dev set. If it performs poorly there, the problem must be coming from the data mismatch. 

We could tackle this issue by pre-processing our data to look more like the production data (e.g., cropping, filtering, downscaling images).

Once the model performs well on the train-dev and dev set, we can evaluate it on the test set. 

## Chapter II - End-to-End Machine Learning Project
