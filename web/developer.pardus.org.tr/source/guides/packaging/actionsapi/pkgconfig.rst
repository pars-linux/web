.. _pkgconfig:

Pkgconfig
========

:Author: Ozan Çağlayan
:Date: |today|
:Version: 0.1


getVariableForLibrary
----------------------------------------

::

    getVariableForLibrary(library, variable)

Executes *pkg-config --variable=<variable> <library>* and returns the output.

Example::

    getVariableForLibrary("libpcsclite", "usbdropdir") -> "/usr/lib/pcsc/drivers"


getLibraryVersion
-----------------

::

    getLibraryVersion(library)

Executes pkg-config --modversion <library> and returns the output.

Example::

    getLibraryVersion("libpng") -> "1.4"


getLibraryCFLAGS
-----------------

::

    getLibraryCFLAGS(library)

Executes *pkg-config --cflags <library>* and returns the output.

Examples::

    getLibraryCFLAGS("nss") -> "-I/usr/include/nss -I/usr/include/nspr"


getLibraryLIBADD
----------------

::

    getLibraryLIBADD(library)

Executes *pkg-config --libs <library>* and returns the output.

Examples::

    getLibraryLIBADD("atk") -> "-latk-1.0 -lgobject-2.0 -lgthread-2.0 -lpthread -lrt -lglib-2.0"


libraryExists
-------------

::

    libraryExists(library)

Executes *pkg-config --exists <library>* and returns a boolean according to the return value.

Examples::

    libraryExists("libpng") -> True

runManualCommand
-----------------

::

    runManualCommand(*args)

Executes a manual pkg-config command and returns the output.


Examples::

    runManualCommand("--libs", "--cflags", "libpng") -> "-I/usr/include/libpng14  -lpng14"
