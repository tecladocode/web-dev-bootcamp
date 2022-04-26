# Contributing guide

Create a virtual environment and install the Python dev dependencies:

```
python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

This installs Black and flake8. Use Black to format any Python code you include in your contributions, and run the code through the flake8 linter to catch any errors.

Then, set up the Vuepress project:

```
npm install
```

That should install everything.

## Run

To run the project e-book locally, you can just do:

```
npm run cur:dev
```

## How to start contributing

Please don't just submit a PR with your contributions before talking about it with the Teclado team!

First, start off by creating an [issue](/issues) with what you'd like to contribute and why. The more information you can give at this stage, the better.

Then we can talk about the contribution idea and plan in the issue itself. Once we've decided to go ahead and how to go ahead, we can begin implementing the changes.

For your changes, please use the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) standard when writing commit messages. It really helps the team understand what each commit does when going through the changes.

After the changes are implemented in a fork, you can submit a PR to the repo. At that point we would review the PR and offer feedback and suggestions, if we have any. Once we're all happy with the changes offered in the PR, we can merge it into this main repository!

Thank you very much for your support and contributions! 💪