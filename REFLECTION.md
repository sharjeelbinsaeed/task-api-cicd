# Reflection

**What does each stage protect against?**
The **lint** stage protects against messy, inconsistent, or stylistically broken
code — `black` enforces one consistent format and `flake8` catches unused
imports, undefined names, and style violations before they spread. The **test**
stage protects against broken behaviour: it proves the endpoints still return the
right status codes and data, so a change that quietly breaks the API is caught
automatically. The **deploy** stage protects the production environment by making
shipping a deliberate, gated step rather than something that happens by accident.

**Why does the order matter?**
`deploy` uses `needs: test`, so it only runs if the test job passes first. If
`deploy` ran before `test`, a broken or failing build could be shipped to
production before anyone knew it was broken — exactly the outcome a pipeline is
meant to prevent. Testing first means only verified code is ever deployed.

**One thing to make this closer to production**
Add a real deployment target (e.g. a free-tier host like Render or Railway)
triggered by a deploy hook stored as a GitHub Secret, plus a branch-protection
rule that blocks merging to `main` until CI passes. A Python test matrix
(3.10 / 3.11 / 3.12) would also catch version-specific issues.
