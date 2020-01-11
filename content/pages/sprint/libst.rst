==============
Sprint - libst
==============

:date: 2019-12-17 12:00
:url: sprint/libst.html
:save_as: sprint/libst.html

.. _libst: https://github.com/yungyuc/turgon

.. _SOLVCON: https://github.com/solvcon/solvcon

.. _Git: https://git-scm.com

.. _Cmake: https://cmake.org

.. _Python: https://python.org

.. _Pybind11: https://pybind11.readthedocs.io/en/stable/

.. _py.test: https://docs.pytest.org/en/latest/

.. _xtl: https://github.com/xtensor-stack/xtl

.. _xsimd: https://github.com/xtensor-stack/xsimd

.. _xtensor: https://github.com/xtensor-stack/xtensor

.. _xtensor-python: https://github.com/xtensor-stack/xtensor-python

libst sprint
============

Project site:
  https://github.com/yungyuc/turgon

Issue tracker:
  https://github.com/yungyuc/turgon/issues

Chatroom (gitter):
  https://gitter.im/yyc-turgon/community

Areas of interests:
  Conservation laws

Host:
  Yung-Yu Chen `@yungyuc <https://twitter.com/yungyuc>`__

Room:
  201

Introduction
------------

Numerical simulation of partial differential equations is a powerful tool for
studying complex problems.  The simulation is too specialized to use general
software, and we have to pursue custom code that takes a lot of time to
develop.  libst_ is such a custom code, but it attempts to employ the modern
tool chain that allows customization without impacting runtime performance.
The kernel uses modern C++, and provides Python interface for easy scripting.
We would like to keep both flexibility and performance.

Another goal is to handle complex geometry.  It is required for industry
application.  The challenge is to avoid ad hoc code.  At the moment, libst_
has only one-dimensional grid.  Meshes in multi-dimensional space will follow
by porting from its predecessor SOLVCON_.

The target users will be both academic and industry.  It is open-source for
productivity and frictionless utilization.  It uses mainstream practices for
build system, version control, unit testing, continuous integration, and other
engineering infrastructure.

Objective
---------

The sprint will focus more on the (software) engineering.  We will try to
improve the following aspects of the code:

* Release process and scripts.
* Enable GitHub Actions for continuous integration (Travis CI is already
  enabled).
* Add build instructions.
* Add documentation structure.
* One-dimensional grid.
* Element abstraction for `the space-time conservation element and solution
  element (CESE) <http://www.grc.nasa.gov/WWW/microbus/>`__ method.
* Develop validating unit-tests cases for the two model problems:

  - Linear wave
  - Inviscid Burgers' equation
* Make a prototype to allow writing solvers in Python.

We are not limited to the above topics.  New ideas are welcome.

Requirements
------------

Equipment:
  Laptop running Linux or MacOS (with wifi connectivity)

Software:
  Git_, Cmake_, Python_, Pybind11_, py.test_

Good to know:
  Conservation laws
