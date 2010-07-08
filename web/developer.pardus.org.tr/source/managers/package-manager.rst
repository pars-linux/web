.. _package-manager-index:

Package Manager
~~~~~~~~~~~~~~~

:Author: Gökmen Göksel

**Package Manager** is a graphical user interface for Pardus' Package
Management System Pisi_ and used to search, install or upgrade packages from
Pardus package repository. It's a handy and usable tool to manage your packages
in an easy way.

Features
--------

* Package Manager is a ``KApplication`` which means it can be integrated with other 
  KDE projects
* Python powered; all of code for Package Manager written in Python_.

Code
----

You can get and install the current version from Pardus SVN using following commands::

$ svn co https://svn.pardus.org.tr/uludag/trunk/kde/package-manager/manager
$ sudo python setup.py install

Also to use Package Manager you need following requirements.

Requirements
------------

* Pisi 2.1 or higher
* Python 2.6 or higher
* PyQt 4.5 or higher
* PyKDE 4.3 or higher

.. _Pisi: http://developer.pardus.org.tr/pisi
.. _Python: http://www.python.org
