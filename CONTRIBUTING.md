# Contribution workflow

This project uses one focused pull request per analysis part.

## Before opening a pull request

1. Fork the repository on GitHub, or create a branch if you have write access.
2. Create the assigned branch from the latest `main` branch.
3. Work only on the files listed in the project README for your part.
4. Run the relevant notebook from top to bottom and run `pytest -q` when changing `src/`.
5. Commit with a clear message such as `Add centrality validation notebook`.
6. Open a pull request describing the research question, methods, output, and verification performed.

## Pull-request review checklist

- The notebook runs from a fresh kernel.
- Random experiments specify a seed.
- Figures have readable titles and axis labels.
- Claims in markdown are supported by the displayed results.
- New reusable algorithm code has a matching test.

Use GitHub's review interface: one teammate requests a change, the author addresses it in a follow-up commit, and the maintainer merges the PR only after the checklist is satisfied.
