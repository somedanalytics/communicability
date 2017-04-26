=====================
Communicability
=====================
.. image:: https://travis-ci.org/somedanalytics/communicability.svg?branch=master
    :target: https://travis-ci.org/somedanalytics/communicability


This repository created for calculate two list of nodes communicability

The purpose is to finding different walks for information passing.


.. image:: https://snag.gy/YMubXO.jpg

Doing matrix multiplication is a massive calculation for CPU.
In this project we are using big-multiplier library in order to calculate adjacency matrix powers.
You need to give the maximum length of the walk.

Important: The longer walks are harder to compute.

Calling the method:

``result, walk_result = communicability(network, [2], [10], walk=3)``

Implementation is using networkx as graph object.

Change Log:

1.1.x: walk_results added. It is list of points in each walk.

Install
===============

``pip install communicability``

note: image does not contail all walks