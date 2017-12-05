# Iteration 5 Evaluation - Group 15

**Evaluator: [Flynn, Michael](mailto:mflynn@jhu.edu)**

## Progress Comments -- on target for iteration 6?

### Size of codebase -- looking reasonable?

* Looks good.

## Code Inspection

### non-CRUD feature code inspection

* All good, looking forward to seeing your ML analysis!

### Package structure of code and other high-level organization aspects

* Overall good.

### Code inspection for bad smells anti-patterns, etc

* In the `leap_tools` module there's a lot of repetition handling your
  LeapMotion features, which closes you off if you want to add new features
  later on.
* Otherwise looks fine, good that you listed refactorings in your iteration
  update.

## Build / run / test / deploy

* Why are you calling `sudo apt-get update` *after* installing packages?
* I cannot build, run, or test your project because the setup script fails.
  Make sure that your setup script / other commands work on a fresh machine
  (I'm using an Ubuntu 14 VM).

*(-5 points)*

## Github

* Looks fine.

## Iteration Plan / Docs

* Would've liked to see more detail for what you plan for the last iteration.

## Overall Comments

Looking forward to seeing this in action!

**Grade: 95/100**
