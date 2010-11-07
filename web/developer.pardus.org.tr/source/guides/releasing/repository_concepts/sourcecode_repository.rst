.. _sourcecode-repository:

Source Code Repository
======================

:Author: Semen Cirit
:Date: |Today|
:Version: 0.1

Pardus developers may be located all around the world. We keep the source code in
an internet-accessible version control system called Subversion `SVN`, in order
to enable our developers to work together on Pardus Distribution.

Pardus has source code repositories and use SVN for source of packages,
technologies and web pages. See `Pardus svn web page`.


Before explaining Pardus repositories structures, we need to explain first
general subversion branch maintainance:

The **trunk** is the main line of development in a SVN repository.

A **branch** is a side-line of development created to make larger, experimental
or disrupting work without annoying users of the trunk version. Also, branches
can be used to create development lines for multiple versions of the same product,
like having a place to backport bugfixes into a stable release.

Finally, **tags** are markers to highlight notable revisions in the history of
the repository..

Special folder names can also be used as trunk, branch, or tags that can be more
meaningful to use.

Package Source Repository
-------------------------

Each developed Pardus distribution has a special folder name in Pardus
`package source repository` and these folders are used as trunks. Each distribution
on this `package source repository` has a specific folder tree.





.. _SVN: http://subversion.tigris.org/
.. _Pardus svn web page: http://svn.pardus.org.tr/
.. _package source repository: http://svn.pardus.org.tr/pardus/
.. _playgound: 
