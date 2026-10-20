"""Dataset loading and basic graph summaries for the SNA project."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import networkx as nx


BUILTIN_GRAPHS = {
    "karate": nx.karate_club_graph,
    "lesmis": nx.les_miserables_graph,
    "florentine": nx.florentine_families_graph,
}


def load_graph(source: str | Path = "karate", directed: bool = False) -> nx.Graph:
    """Load a built-in graph, edge list, or Matrix Market adjacency matrix.

    Parameters
    ----------
    source:
        One of ``karate``, ``lesmis``, or ``florentine``, or a path to an
        edge-list / ``.mtx`` file.
    directed:
        Create a directed graph for file-based input. Built-in examples remain
        in their original (undirected) form.
    """
    source_text = str(source)
    if source_text.lower() in BUILTIN_GRAPHS:
        return BUILTIN_GRAPHS[source_text.lower()]()

    path = Path(source)
    if not path.is_file():
        raise FileNotFoundError(
            f"Could not find graph data at {path}. Use a built-in graph or a valid file path."
        )

    graph_type = nx.DiGraph if directed else nx.Graph
    if path.suffix.lower() == ".mtx":
        try:
            from scipy.io import mmread
        except ImportError as exc:
            raise ImportError("Reading .mtx files requires scipy. Install it with `pip install scipy`.") from exc
        matrix = mmread(path).tocsr()
        return nx.from_scipy_sparse_array(matrix, create_using=graph_type)

    lines: list[str] = []
    with path.open(encoding="utf-8") as file:
        for line in file:
            row = line.strip()
            if row and not row.startswith(("#", "%")):
                lines.append(row.replace(",", " "))
    return nx.parse_edgelist(lines, nodetype=str, create_using=graph_type, data=False)


def network_summary(graph: nx.Graph) -> dict[str, Any]:
    """Return descriptive statistics, using the largest component for distances."""
    undirected = graph.to_undirected()
    nodes = undirected.number_of_nodes()
    if nodes == 0:
        raise ValueError("Cannot summarise an empty graph.")

    components = list(nx.connected_components(undirected))
    giant = undirected.subgraph(max(components, key=len)).copy()
    giant_nodes = giant.number_of_nodes()

    return {
        "Nodes": graph.number_of_nodes(),
        "Edges": graph.number_of_edges(),
        "Density": nx.density(graph),
        "Average degree": 2 * undirected.number_of_edges() / nodes,
        "Connected components": len(components),
        "Largest component nodes": giant_nodes,
        "Diameter (largest component)": nx.diameter(giant) if giant_nodes > 1 else 0,
        "Average shortest path (largest component)": (
            nx.average_shortest_path_length(giant) if giant_nodes > 1 else 0.0
        ),
        "Average clustering": nx.average_clustering(undirected),
        "Transitivity": nx.transitivity(undirected),
    }
