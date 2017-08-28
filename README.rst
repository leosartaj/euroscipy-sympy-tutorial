=============================
EuroSciPy 2017 SymPy Tutorial
=============================

Introduction
============

This repository contains all of the source code and Jupyter notebooks for the
EuroSciPy 2017 tutorial "Introduction to SymPy".

Software Installation
=====================

We leverage the Conda package manager for installation of the necessary
software on the three most popular platforms. Please install either Anaconda_
or Miniconda_ using the instructions provided at the download links.

.. _Anaconda: https://www.continuum.io/downloads
.. _Miniconda: https://conda.io/miniconda.html

You will need to download_ and unzip or clone_ this repository with Git so that
the files are available on your computer. For example::

   > wget https://github.com/leosartaj/euroscipy-sympy-tutorial/archive/master.zip
   > unzip master.zip

or::

   > git clone https://github.com/leosartaj/euroscipy-sympy-tutorial.git

.. _download: https://github.com/leosartaj/euroscipy-sympy-tutorial/archive/master.zip
.. _clone: https://github.com/leosartaj/euroscipy-sympy-tutorial.git

At the command line, change into the repository directory::

   > cd /path/to/euroscipy-sympy-tutorial

Creating a conda environment from ``environment.yml``
-----------------------------------------------------

Once you have conda installed, you can make a new environment. We strongly
encourage you to use ``environment.yml``. At the command line, you can create
this environment by executing e.g.::

   > conda env create -f environment.yml

When creation is complete you may activate the environment by typing::

   > activate sympytutorial

on Windows or using Bash on Linux/Mac::

   $ source activate sympytutorial

To install the necessary packages, you may run the following command::

   (sympytutorial)> conda install --file=requirements.txt
  
To check to see if everything is installed correctly type::

   (sympytutorial)> python test_installation.py

If there are no errors or warnings you have installed the software correctly.

To exit the environment you type::

   (sympytutorial)> deactivate

If you for some reason want to remove the environment you can do so after
deactivating by typing::

   > conda env remove --name sympytutorial

on windows, and::

   $ source deactivate

on Linux/Mac (using bash).

At this point you have everything installed to run the code in the tutorial.

Running the notebooks
=====================

After activating the `sympytutorial` environment start Jupyter in the `notebooks`
directory::

   (sympytutorial)> jupyter notebook

A web interface should open in your web browser (default address
http://localhost:8888). Note that Ctrl-C will stop the notebook
server.

More Resources
==============

This tutorial is based on [SymPy Tutorial (SciPy 2016)](https://github.com/sympy/scipy-2016-tutorial) and [SymPy Code Generation Tutorial (SciPy 2017)](https://github.com/sympy/scipy-2017-codegen-tutorial).
