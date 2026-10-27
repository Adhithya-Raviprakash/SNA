# Data directory

This folder is for optional network datasets used by the notebooks.

The default analysis uses NetworkX's built-in **Zachary's Karate Club** graph, so
the project runs without downloading any data. To analyse another network, put
an edge-list or Matrix Market (`.mtx`) file in this folder and pass its relative
path to `load_graph`, for example:

```python
G = load_graph("data/example_edges.txt")
```

Supported edge-list rows are `source target` or `source,target`. Blank lines and
lines beginning with `#` or `%` are ignored. Use `directed=True` for follower,
reply, or citation networks where edge direction matters.

Do not commit data that is private, licensed for restricted use, or too large
for GitHub. Record the source, licence, collection date, and any preprocessing
in this file when adding a dataset.

## Included datasets

| File | Description | Source |
| --- | --- | --- |
| `facebook_combined.txt` | 4,039 nodes, 88,234 undirected friendship edges (space-separated edge list). Used to exercise the dashboard's large-network mode. | SNAP `ego-Facebook` — J. McAuley and J. Leskovec, *Learning to Discover Social Circles in Ego Networks*, NIPS 2012. https://snap.stanford.edu/data/ego-Facebook.html |
| `les_miserables.dot` | Character co-appearance network from *Les Misérables* in Graphviz DOT format, with `weight` edge attributes. Nodes are numbered rather than named. | D. E. Knuth, *The Stanford GraphBase* (1993). Download location and collection date: TODO — confirm with the contributor who added it. |

Neither file has been preprocessed beyond removing a leading blank line from the DOT file.
