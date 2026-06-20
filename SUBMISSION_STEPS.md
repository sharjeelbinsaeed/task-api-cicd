# What's done for you vs. what you must do

## Already done (these files are ready to push)
- `main.py` ............... Task Manager API (starter, unmodified)
- `test_main.py` ......... 4 tests, all implemented and PASSING locally
- `requirements.txt` ..... app + test + lint dependencies
- `.flake8` .............. keeps flake8 and black in agreement (no conflicts)
- `.github/workflows/ci.yml` ... complete CI + gated deploy workflow (all blanks filled)
- `REFLECTION.md` ........ the 3 wrap-up answers

Verified locally before delivery:
- `black --check .`  -> clean
- `flake8 .`         -> clean
- `pytest -v`        -> 4 passed

## You must do (needs YOUR GitHub account — cannot be done for you)

1. Create a new GitHub repo (public is fine).
2. Put these files in it and push to the `main` branch:
   git init
   git add .
   git commit -m "CI/CD assignment: app, tests, workflow"
   git branch -M main
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin main

3. Open the **Actions** tab — confirm the workflow runs and is GREEN.

4. Do the required break-then-fix cycle (this is the graded part):
   - Break a test: in test_main.py change `assert response.status_code == 200`
     to `== 500`, then commit + push. Watch the run go RED. -> screenshot #1
   - Fix it back to `== 200`, commit + push. Watch it go GREEN. -> screenshot #2
   (A formatting break also works: add bad spacing so `black --check` fails.)

5. Confirm in the Actions tab that `deploy` runs only AFTER `test` passes
   (and is skipped when `test` fails).

6. Submit: the repo link + the two screenshots (red run, green run).

## Optional: run it locally first to see it work
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --reload        # open http://127.0.0.1:8000/docs
   pytest -v                        # in a second terminal
