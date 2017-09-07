r"""
Implementing a new parent: a (draft of) tutorial


The easiest approach for implementing a new parent is to start from a
close example in sage.categories.examples. Here, we will get through
the process of implementing a new finite semigroup, taking as starting
point the provided example::

    sage: S = FiniteSemigroups().example()
    sage: S
    An example of a finite semigroup: the left regular band generated by ('a', 'b', 'c', 'd')

You may lookup the implementation of this example with::

    sage: S??                               # not tested

Or by browsing the source code of
:class:`sage.categories.examples.finite_semigroups.LeftRegularBand`.

Copy-paste this code into, say, a cell of the notebook, and replace
every occurrence of ``FiniteSemigroups().example(...)`` in the
documentation by ``LeftRegularBand``. This will be equivalent to::

    sage: from sage.categories.examples.finite_semigroups import LeftRegularBand

Now, try::

    sage: S = LeftRegularBand(); S
    An example of a finite semigroup: the left regular band generated by ('a', 'b', 'c', 'd')

and play around with the examples in the documentation of ``S`` and of
:class:`FiniteSemigroups`.

Rename the class to ``ShiftSemigroup``, and modify the product to
implement the semigroup generated by the given alphabet such that `au
= u` for any `u` of length `3`.

Use ``TestSuite`` to test the newly implemented semigroup; draw its
Cayley graph.

Add another option to the constructor to generalize the construction
to any u of length `k`.

Lookup the Sloane for the sequence of the sizes of those semigroups.


Now implement the commutative monoid of subsets of `\{1,\dots,n\}`
endowed with union as product. What is its category? What are the
extra functionalities available there? Implement iteration and
cardinality.

TODO: the tutorial should explain there how to reuse the enumerated
set of subsets, and endow it with more structure.

"""
