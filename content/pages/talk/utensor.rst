==================================
uTensor: Make Devices Smart Again!
==================================

:date: 2020-01-06 21:09
:url: talk/utensor.html
:save_as: talk/utensor.html

uTensor: Make Devices Smart Again!
==================================

We would like to introduce and demonstrate ``uTensor`` runtime, a neural
network inference library for microcontroller unit (MCU), and its development.
We will talk about tensor computing kernels, memory management, CLI,
applications and more.

Talk Description
================

Deploying machine-learning models on resource constrained devices like micro
controller units (MCU), require knowledge in both data science and embedded
system.  However, it’s very hard for developer to master both domains.  For
example, topics including:

* Knowledge of Machine Learning algorithm such as designing efficient neural
  network architectures, training dynamic and theoretic/numeric optimization
  techniques.
* Memory management, e.g memory allocation/planing.
* Coordinate peripheral devices on embedded system.
* And more.

These have been naturally disjointed domains which makes it difficult for any
individual or team to deploy machine learning models on MCUs.  With this in
mind, uTensor is designed as a developer-friendly neural network inference
library targeting MCU.

Speaker
=======

This talk will be presented by three speakers: Neil Tan, Kazami Hsieh, and Dboy
Liao.  They are the team members of the ``uTensor`` project.

Neil Tan, the project manager and core developer of uTensor, will talk about
the motivation of uTensor and many applications such as sensor fusion, AIoT and
robotic that could be powered by uTensor.  Kazami Hsieh, another core developer
of uTensor runtime, will talk about the design of uTensor runtime and how we
make it efficient in terms of memory usage and binary size which are critical
for MCU.  `Dboy Liao <http://cakeresume.com/dboyliao>`__, the core developer of
uTensor CLI, will give a demo on how to transforming a pre-trained model using
frameworks such as Tensorflow or PyTorch into compilable and runnable uTensor
implementation ready for MCU.
