About the document
==================

One of the main part of pisi package is actions.py is. It is a python script
that contains information of the operations to be executed on the source code.
This document is an overview of the Actions API library which includes the
functions that are available for use in actions.py scripts.

Actions API
-----------

Actions API has a modular structure that makes the packaging process easier for
the packager. The major modules of the Actions API are:

    * `Autotools: <http://developer.pardus.org.tr/guides/packaging/actionsapi/autotools.html>`_  Standard functions for building and installing applications.
    * `Cmaketools: <http://developer.pardus.org.tr/guides/packaging/actionsapi/cmaketools.html>`_ Functions for building the applications that are configured with cmake.
    * `Get: <http://developer.pardus.org.tr/guides/packaging/actionsapi/get.html>`_ Functions for getting information about evnironment variables or packages needed in building and installation phases.
    * `Libtools: <http://developer.pardus.org.tr/guides/packaging/actionsapi/libtools.html>`_ Pre-build and post-build operations for configuring libraries.
    * `Kde: <http://developer.pardus.org.tr/guides/packaging/actionsapi/kde.html>`_ Functions for configuring, building and installing KDE applications.
    * `Kde4: <http://developer.pardus.org.tr/guides/packaging/actionsapi/kde4.html>`_ Functions for configuring, building and installing KDE applications.
    * `Kerneltools: <http://developer.pardus.org.tr/guides/packaging/actionsapi/kerneltools.html>`_ Functions for configuring, building and installing kernel and kernel modules.
    * `Pisitools: <http://developer.pardus.org.tr/guides/packaging/actionsapi/pisitools>`_ Fundamentally used for moving files to install directory from work directory, the functions included in pisitools are convenient for most operations i.e. symlinking, file manipulation via sed, deleting files or directories.
    * `Perlmodules: <http://developer.pardus.org.tr/guides/packaging/actionsapi/perlmodules.html>`_ Functions for configuring, building and installing perl modules.
    * `Pythonmodules: <http://developer.pardus.org.tr/guides/packaging/actionsapi/pythonmodules.html>`_ Functions for configuring, building and installing python modules.
    * `Qt4: <http://developer.pardus.org.tr/guides/packaging/actionsapi/qt4.html>`_ Functions for configuring, building and installing Qt4.
    * `rubymodules: <http://developer.pardus.org.tr/guides/packaging/actionsapi/rubymodules.html>`_ Functions for configuring, building and installing ruby modules.
    * `Scons: <http://developer.pardus.org.tr/guides/packaging/actionsapi/scons.html>`_ Counterpart of autotools for the new generation building tools, scons.
    * `Shelltools: <http://developer.pardus.org.tr/guides/packaging/actionsapi/shelltools.html>`_ Functions for specific operations. Apart from pisitools, shelltools is capable of operating in absolute paths instead of relative paths. Granting the ability to operate in the darkest corners of the system to the packager shelltools has to be used responsibly.
    * `Texlivemodules: <http://developer.pardus.org.tr/guides/packaging/actionsapi/texlivemodules.html>`_ Functions for configuring, building and installing texlive modules.

