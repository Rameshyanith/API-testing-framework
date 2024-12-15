
[pytest] # type: ignore

addopts = --strict-markers --tb=short --html=reports/report.html --self-contained-html # type: ignore
markers =
  smoke: run smoke test only # type: ignore
  regression: run regression test only # type: ignore