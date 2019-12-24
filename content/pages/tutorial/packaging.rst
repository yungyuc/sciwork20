=======================================================
Tutorial - Packaging: Share your code for pip and Conda
=======================================================

:date: 2019-12-18 12:00
:url: tutorial/packaging.html
:save_as: tutorial/packaging.html

Tutorial - Packaging: Share your code for pip and Conda
=======================================================

Python packages are reusable code that can be fetched, installed, and then
imported by another program. Their contents are exactly the same as any Python
project, only contains some extra configuration, so they can be bundled and
uploaded to a shared place, for users to download from. This tutorial will
teach you how to generate said metadata, so you can bundle your code into a
"distributable," for others to install with either pip or Conda.

Goal
====

Attendees will be able to produce a Python package using Setuptools's PEP 517
backend, ready to be published to both a Python Package Index (PyPI) and a
community Conda repository (conda-forge). The package will contain both
importable Python files (pure modules and packages) and non-code data files.

Attendees will also be able to familiarize themselves with commonly-used
project management tools, and be ready to understand workflows of popular
packages, and to make contributions for them.

Target audience
---------------

Python users that already understand Python modules, and want to package such
code so they can use them with ``pip install`` or ``conda install``.

Atendees are encouraged to bring their own modules to package, and explore how
they can be converted into an installable format.


Speaker introduction
====================

Tzu-Ping Chung (`@uranusjr <https://twitter.com/uranusjr>`__)

TP builds his career around open source software, and enjoys committing his
efforts to help make the world better. He builds all kinds of software for a
living, from embedded system to single-page web applications, and contributes
to the community when he can.

He served as chairperson during 2017–2018, and performed various other roles
for PyCon Taiwan. These days, he spends most of his free time contributing to
core Python packaging tools such as pip, and involving in packaging-related
architectural design discussions as a member of the Python Packaging Authority
(PyPA).

Detail description
==================

TBD

Requirement
-----------

Attendees should know how to write Python modules (files that can be imported
by another file). They should have basic understandings to the command line,
and know how to create, rename, and edit files in a text editor or the command
line, on their own computers.

Please have the followings ready before the tutorial:

* Any Python installation with either virtualenv or venv available.
* (optional) Conda, if the attendee wants to package for ``conda install``.
