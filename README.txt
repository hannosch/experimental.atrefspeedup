Introduction
============

At the heart of the Archetypes reference engine is the reference_catalog. This
is a set of catalog indexes used to perform the actual query lookups.

The choice of using a ZCatalog has lead to some data structures which aren't
suited for handling references.

This project tries to work around some of the short comings of the internal
implementation of the reference engine without changing the public API or
making any other changes to the stored data.
