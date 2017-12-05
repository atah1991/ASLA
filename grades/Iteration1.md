# Iteration 1 Evaluation - Group 15

**Evaluator: [Flynn, Michael](mailto:mflynn@jhu.edu)**


## Positive Points:

* Very novel concept and I'm interested to see how you handle software
  engineering for machine learning.


## Things to Improve:

### Use cases are not correct

Each of your use cases are supposed to describe how different processes happen,
please follow the format [described in class](Use case format).

*(-15 points)*

### What's the point of your backend?

You note that gesture recognition is going to be done client-side, and that
your app is going to be operational offline. What is the point of your backend
then, except for updating models? The core algorithms and technology you're
using is complex, but this not a machine learning, NLP, or hardware course. As
a software system, this really isn't complex enough if it's just going to be a
frontend app.

*(-2 points)*

### No use cases or UI for the "Expert" role

One of your user roles is the "Admin", who is an ASL expert who can update new
gesture models. However, you do not provide any use cases or provide UIs for
this user type at all, even though they will use your application much
differently than a normal user would. You need to detail this.

*(-4 points)*

### Architecture is not detailed enough

You have a few sneaky features that you don't talk about much when you really
need to. One of your features is live voice -- what text-to-speech library are
you going to use? How do you know when a word is finished and should be spoken?
You also include a 3D graphic -- again, what software are you going to use for
it? Is there software that will help you create joint animations from the
LeapMotion, or are you going to be doing this all yourself? What libraries are
you going to use to do machine learning? These things *need* to be detailed in
your architecture section.

*(-4 points)*

### Is this going to work?

I'm assuming this is a web app, because all of the technologies you list are
web technologies. Do you know if your web app is going to be able to access the
LeapMotion device? Is there a process for installing drivers and such? I'm not
convinced just by glancing at their SDK documentation.


## Suggestions:

### Make sure you're doing proper engineering for machine learning

You didn't mention anything about *how* you system is actually going to
recognize gestures with this. Since machine learning is core to your project
and this is an **engineering** course, make sure that you're also describing
which algorithms you're going to use and how they differ in accuracy, latency,
hardware requirements, etc.

### Please start prototyping this earlier rather than later

This is a tricky project, and if this fails you will not have a project. Make
sure this is feasible earlier rather than later.

### Why JHED log in?

Why not just a normal email/password login?


## Overall:

A solid start, but make sure that you're first and foremost doing a *software
engineering* project, and not a science project. Please remember that you can
get points back next iteration for fixing these things!

** Grade: 75/100 **

[Use case format]: http://pl.cs.jhu.edu/oose/lectures/requirements.shtml#usecaseformat

