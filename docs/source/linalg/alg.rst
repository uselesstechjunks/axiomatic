################################################################################
Algebraic Structures
################################################################################

.. note::
	* Any set :math:`X` can be endowed with rich albegraic structures.
	* In the following, we assume that all the elements are in :math:`X`.
	* In each of the following operations, we assume that it creates a closure, i.e. it maps to some other element in :math:`X` itself.

********************************************************************************
Group
********************************************************************************
.. note::
	* We have an addition :math:`+` defined for :math:`X` which follows **associativity**, i.e.

		* :math:`x+(y+z)=(x+y)+z`.
	* There is a unique identity element :math:`0` w.r.t :math:`+` such that

		* :math:`x+0=0+x=x`
	* For every :math:`x`, there is a unique inverse element w.r.t :math:`+`, :math:`-x` such that

		* :math:`x+(-x)=(-x)+x=0`

.. tip::
	If we enforce group structure to the set of numbers, we extend naturals (:math:`\mathbb{N}`) to the set of integers (:math:`\mathbb{Z}`)

Abelian Group
================================================================================
.. note::
	* It is a group.
	* The addition operator has to be **commutative** so that

		* :math:`x+y=y+x`

********************************************************************************
Ring
********************************************************************************
.. note::
	* It is an Abelian group w.r.t the addition operator :math:`+`.
	* It also has a multiplication :math:`\cdot` defined so that

		* It is associative, :math:`x\cdot (y\cdot z)=(x\cdot y)\cdot z`
		* There is a unique identity element :math:`1` w.r.t :math:`\cdot` such that

			* :math:`x\cdot 1=1\cdot x=x`
		* For every :math:`x`, there is a unique inverse element w.r.t :math:`\cdot`, :math:`x^{-1}` such that

			* :math:`x\cdot x^{-1}=x^{-1}\cdot x=1`
	* Addition and multiplication follow the **distributive** property

		* :math:`x\cdot(y+z)=x\cdot y+x\cdot z`

********************************************************************************
Field
********************************************************************************
.. note::
	* It is a ring.
	* It is an Abelian group w.r.t the addition operator :math:`+` as well as the multiplication opeartor :math:`\cdot`.

.. tip::
	* If we enforce field structure to the set of numbers, we extend integers (:math:`\mathbb{Z}`) to the set of rationals (:math:`\mathbb{Q}`)
	* To extend rationals (:math:`\mathbb{Q}`) to reals (:math:`\mathbb{R}`), we need to introduce topological properties.
