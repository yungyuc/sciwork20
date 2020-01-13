==============
Sprint - Uni10
==============

:date: 2019-12-17 12:00
:url: sprint/uni10.html
:save_as: sprint/uni10.html

.. _Uni10: https://gitlab.com/uni10/uni10

.. _GitLab: https://gitlab.com

.. _Git: https://git-scm.com

.. _Cmake: https://cmake.org

.. _Boost: https://www.boost.org

Uni10 sprint
============

Project site:
  https://gitlab.com/uni10/uni10

Issue tracker:
  https://gitlab.com/uni10/uni10/issues

Areas of interests:
  Quantum physics, chemistry, statistics

Hosts:
  Ying-jer Kao and Pochung Chen

Room:
  202

Introduction
------------

Uni10_ is a numerical library designed for tensor networks, which finds
applications in quantum physics, chemistry, data analysis and machine learning.
In this sprint, the participants will have the chance to work on different
parts of Uni10_ to understand and improve cross-platform build using CMake, GPU
programming using CUDA, Python binding generation using pybind11, unit testing
using gtests and writing API documentation using Doxygen.  In addition, the
participants can get familiar with git workflow and CI/CD.  Furthermore,
multi-node/multi-gpu programming paradigm will also be explored.

Objective
---------

* Enhance the new architecture with unit tests and regression tests:

  * Make test cases for inserting numpy array to C++ array.
  * Make test cases for matrix transpose/multiplication in GPU.
* Enable `llvm-tidy <https://clang.llvm.org/extra/clang-tidy/>`__ on the CI.
* Resolve other tickets.

Requirements
------------

Attendee equipment:
  Laptop running Linux or MacOS (with wifi connectivity)

Software:
  Git_, Cmake_, and Boost_

Online service:
  GitLab_ account

Other:
  Unit-testing

Optional:
  Linear algebra, matrix operation (at GPU), Hamitonian equation (physics)
