#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Orcun Gumus
#
"""A function for calculate the communicability of two nodes of a big big graph"""

import networkx
import numpy
import math

from scipy.sparse import csr_matrix, lil_matrix
from bigmultiplier import bigmultiplier


def communicability(network, nodes_list_1, nodes_list_2, walk=1):
    """
    A function for calculate apprx communicability of two group of node on a graph

    total_point: Total point within two list of nodes
    walk_total_points: Total points at the end of the walks
    points: Distribution of points at the end

    :param walk: Total walk lenth, longer walks are harder to compute
    :type walk: int

    :param network: A giant network
    :type network: networkx.Graph

    :param nodes_list_1: A group of nodes
    :type nodes_list_1: list(int)

    :param nodes_list_2: A group of nodes
    :type nodes_list_2: list(int)

    :rtype total_point: float
    :rtype walk_total_points: list(float)
    :rtype points: list(float)
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
    result_sparse = lil_matrix(adj_sparse.shape, dtype=numpy.float32)

    walk_total_points = []
    for i in range(1, walk):
        result_sparse = result_sparse + adj_sparse_ / math.factorial(i)
        walk_total_points.append(result_sparse[x_, y_].sum())
        print("Matrix multiplication...")
        adj_sparse_ = bigmultiplier(adj_sparse_, adj_sparse)
        print("Walk completed")
    result_sparse = result_sparse + adj_sparse_ / math.factorial(walk)
    walk_total_points.append(result_sparse[x_, y_].sum())

    assert isinstance(result_sparse, csr_matrix)
    assert isinstance(adj_sparse_, lil_matrix)

    total_point = float(result_sparse[x_, y_].sum())
    points = [item for sublist in result_sparse[x_, y_].tolist() for item in sublist]

    return total_point, walk_total_points, points
