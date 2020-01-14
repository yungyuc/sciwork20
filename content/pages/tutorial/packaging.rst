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

Attendees are encouraged to bring their own modules to package, and explore how
they can be converted into an installable format.


Speaker introduction
====================

Tzu-Ping Chung (`@uranusjr`_)

.. _`@uranusjr`: https://twitter.com/uranusjr

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

We will be following the *Packaging Python Projects* tutorial from the
`Python Packaging User Guide`_ for ``setup.py`` and PyPI, and
*Building conda packages from scratch* from the `Conda-build documentation`_
for ``conda-build`` and conda-forge. Some additional topics not able to fit
into the conference schedule will be covered in slides for future reference.

.. _`Python Packaging User Guide`: https://packaging.python.org/
.. _`Conda-build documentation`: https://docs.conda.io/projects/conda-build/

* 13:30–13:50: Overview and setup troubleshooting.
* 13:50–14:15: Create a Python package with Setuptools and ``setup.py``.
* 14:15–14:45: Upload to the package index (PyPI).
* 14:45–15:30: Excersise and Q&A.
* 14:45–15:00: Break.
* 15:00–15:15: Package for Conda with ``conda-build``.
* 15:15–15:45: Excersise and Q&A.
* 15:45–16:00: Upload to conda-forge.
* 16:00–16:30: Miscellaneous topics: binary packages, continuous integration,
  and other useful tools (as time permits).


Requirement
-----------

Attendees should know how to write Python modules (files that can be imported
by another file). They should have basic understandings to the command line,
and know how to create, rename, and edit files in a text editor or the command
line, on their own computers.

Please have the followings ready before the tutorial:

* Any Python installation with pip, and either virtualenv or venv available.
* Conda from either Miniconda_ or Anaconda.
* (Optional) Some Python code you want to package and publish as a Python
  and/or Conda package.

.. _Miniconda: https://conda.io/en/latest/miniconda.html
