#######################################################################################
Probability Axioms (Kolmogorov Axioms)
#######################################################################################

Let the set of all possible outcomes of an experiment be :math:`\Omega`, and let **events** be defined as measurable subsets, :math:`\omega\subset\Omega`. Then a measure :math:`\mu:2^{|\Omega|}\mapsto\mathbb{R}` is called a **probability measure** iff

#. **Non-negativity**: :math:`\mu(\omega)\ge 0` for any :math:`\omega\subset\Omega`.
#. **Unitarity**: :math:`\mu(\Omega)=1`.
#. :math:`\sigma`-**Additivity**: For :math:`A_1,A_2,\cdots\subset\Omega` such that :math:`A_i\cap A_j=\emptyset` for :math:`i\neq j`

	.. math:: \mu(\bigcup_{i=1}^\infty A_i)=\sum_{i=1}^\infty \mu(A_i).

.. tip::
	It is customary to represent probability measure as :math:`\mathbb{P}`.
