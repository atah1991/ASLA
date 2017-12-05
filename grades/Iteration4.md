# Iteration 4 Evaluation - Group 15

**Evaluator: [Flynn, Michael](mailto:mflynn@jhu.edu)**

## Positive Points

* Looks like it's coming along!
* Thanks for providing detail about your ML algo.

## Needs work issues

* Make sure you're continually using GitHub issues. A lot of your iteration 4
  issues are still open.
* Why are you talking about `.exe`s if this is a Linux project? (All of your
  instructions use apt)

*(-2 points)*

## Code

Looks fine, not a lot of OO design going on. Some of your UI code is a huge
wall of text though.

## Tests

###  Good code coverage?

Looks good, it's great that you're quantifying it.

### Travis works?

Yep!

*(+5 points)*

## Build / run / deploy

### Clear scripts for both build/run and deploy?

Some of your instructions are a little off. For example, you install Python
packages with pip before installing Python and pip themselves via apt. If I
didn't have Python already this wouldn't work

Please create install/deploy scripts to run everything with one click. I can't
just copy/paste your instructions (esp. with things like `<project_root>`).

*Pretend I don't know anything.*

*(-3 points)*

### Grader could fire up and run project?

Nope. I can't find asla.exe or figure out how to build your frontend or your
server.

*(-5 points)*

## Github

### Good use of git branch?

It looks like you're using feature-level branches, but you also seem to be
writing to master a lot as well. Make sure there's a development process in
place.

*(-2 points)*

## Iteration Plan

Looks fine, but don't leave the last iteration to just "fix issues".

## Code Docs

Looks good.

## Machine Learning

The metrics you provided look very suspicious. Think about how you're
partitioning your data into folds to train and evaluate on. Because your data
is only from two people, it's going to be very homogeneous, especially if the
way you collected data was to repeat the same letter over and over 30 times --
if you did that, each sample is going to look extremely similar to one another,
so when you evaluate it would be as if you're evaluating on training data. This
is probably why you have such good numbers but report that it performs much
worse in practice.

A better experiment would be to have you all record data, then partition your
data so that you train on gestures from three of you, and evaluate on gestures
made by someone outside the set (so 4 folds made up of gestures from only one
person).

## Overall Comments

Looks like you're coming along, but please provide clearer instructions on how
to run everything.

**Grade: 93/100**
