# Contributing to `bxlogs`

## Making a release

1. Update the CHANGELOG
2. Update the version in `pyproject.toml` and in `bxlogs.py`
3. Commit
4. Push and wait for the CI job to succeed
5. Tag with `v` followed by the version (e.g. `git tag v1.1.1`)
6. Push the tag
7. Wait for the [CI job][ci] to finish

[ci]: https://github.com/Bixoto/bxlogs/actions/workflows/publish.yml
