"""Reusable plotting helpers for network exploration."""

from __future__ import annotations

from typing import Hashable, Mapping

import matplotlib.pyplot as plt
import networkx as nx


def graph_layout(graph: nx.Graph, seed: int = 42) -> Mapping[Hashable, tuple[float, float]]:
    """Create a reproducible spring layout for a graph."""
    return nx.spring_layout(graph, seed=seed)


def plot_network(
    graph: nx.Graph,
    position: Mapping[Hashable, tuple[float, float]] | None = None,
    title: str = "Network",
    *,
    with_labels: bool = True,
) -> plt.Axes:
    """Draw a clean network overview and return its axes."""
    if position is None:
        position = graph_layout(graph)
    _, axis = plt.subplots(figsize=(7, 6))
    nx.draw(
        graph,
        position,
        ax=axis,
        with_labels=with_labels,
        node_color="lightsteelblue",
        edgecolors="black",
        node_size=480,
        font_size=8,
        arrows=graph.is_directed(),
    )
    axis.set_title(title)
    return axis


def plot_degree_distribution(graph: nx.Graph) -> plt.Axes:
    """Plot a discrete histogram of node degrees and return its axes."""
    degrees = [degree for _, degree in graph.degree()]
    if not degrees:
        raise ValueError("Cannot plot a degree distribution for an empty graph.")
    _, axis = plt.subplots(figsize=(6, 4))
    axis.hist(
        degrees,
        bins=range(0, max(degrees) + 2),
        align="left",
        color="seagreen",
        edgecolor="black",
    )
    axis.set(xlabel="Degree", ylabel="Number of nodes", title="Degree distribution")
    return axis
