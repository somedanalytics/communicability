#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Orcun Gumus
#
"""A function for calculate the communicability of two nodes of a big big graph"""

import networkx
import numpy
import math

from scipy.sparse import csr_matrix
from bigmultiplier import bigmultiplier


def communicability(network, nodes_list_1, nodes_list_2, walk=1):
    """
    A function for calculate apprx communicability of two group of node on a graph
    :param network: A giant network
    :param nodes_list_1: A group of nodes
    :param nodes_lis8t_2: A group of nodes
    :type network: networkx.Graph
    """
    walk = walk + 1

    adj_sparse = networkx.to_scipy_sparse_matrix(network, dtype=numpy.float32)
    assert isinstance(adj_sparse, csr_matrix)

    nodes = network.nodes()
    x_ = []; y_ = []
    for x in nodes_list_1:
        for y in nodes_list_2:
            x_.append(nodes.index(x))
            y_.append(nodes.index(y))

    adj_sparse_ = adj_sparse.copy()
    result_sparse = csr_matrix(adj_sparse.shape, dtype=numpy.float32)

    walk_points = []
    for i in range(1, walk):
        result_sparse = numpy.add(result_sparse, adj_sparse_ / math.factorial(i))
        walk_points.append(result_sparse[x_, y_].sum())

        adj_sparse_ = bigmultiplier(adj_sparse_, adj_sparse)
    result_sparse = numpy.add(result_sparse, adj_sparse_ / math.factorial(walk))
    walk_points.append(result_sparse[x_, y_].sum())

    points = result_sparse[x_, y_].sum()

    return points, walk_points
