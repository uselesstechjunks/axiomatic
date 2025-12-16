#########################################
Pre-requisite
#########################################

***********************************************
Binomial and Multinomial Theorem
***********************************************

(MISSISSIPPI problem): Number of ways to arrange the letters is :math:`\frac{11!}{1!4!4!2!}` (M=1,I=4,S=4,P=2).

.. note::
	* There are items of :math:`r` kinds, and within each kind they are indistinguishable. Say, we have :math:`k_i` items of :math:`x_i` kind, and so on. The number of ways of arranging a total of :math:`n` such items (i.e. :math:`\sum_{i=1}^r k_i=n`)

		.. math:: {n\choose k_1\cdots k_r}=\frac{n!}{k_1!\cdots k_r!}
	* This is also the number of ways a set of :math:`n` indistinguishable items can be partitioned into :math:`r` subsets. To see why, think about the process where we do the partitioning first (say, :math:`C` is the number of ways we can partition) and then we rearrange each subset (:math:`k_i!` ways for subset :math:`i`) put the items in a sequence. The result is just a rearrangement of the entire sequence of :math:`n` items.

Binomial theorem: 
==============================================
* For evaluating the expression :math:`(x+y)^n=(x+y)\cdots(x+y)` (:math:`n`-times), the process involves choosing either :math:`x` or :math:`y` from each of the :math:`n`-terms. 
* We can choose :math:`x` from 0 terms to :math:`n` terms. Every time we choose :math:`x` from :math:`k` such terms, we're left with no choice but to take :math:`y` from  the remaining :math:`(n-k)` terms.
* The number of ways we can choose :math:`x` from any :math:`k` of such terms is :math:`{n\choose k}`. This is how many times we have :math:`x^k y^{n-k}`.
* Therefore

	.. math:: (x+y)^n=\sum_{k=0}^n {n\choose k} x^k y^{n-k}

.. tip::
	* :math:`\sum_{k=0}^n {n\choose k}=2^n` (setting :math:`x=1` and :math:`y=1`).
	* :math:`\sum_{k=0}^n (-1)^k {n\choose k}=0` (setting :math:`x=-1` and :math:`y=1`).
	* (Vandermonde Identity) :math:`{m+n\choose k}=\sum_{i=0}^k {m\choose i}{n\choose k-i}`.
	* :math:`{n\choose k}={n-1\choose k-1}+{n-1\choose k}`.

Multinomial theorem:
==============================================
* For evaluating the expression :math:`(x_1+x_2+\cdots+x_r)^n=(x_1+x_2+\cdots+x_r)\cdots(x_1+x_2+\cdots+x_r)` (:math:`n`-times), the process involves choosing :math:`x_1` from :math:`k_1` such terms, :math:`x_2` from :math:`k_2` such terms, and so on.
* Regardless of how we choose, the :math:`\sum_{i=1}^r k_i=n`.
* For each values of :math:`0\leq k_1,k_2,\cdots k_r\leq n`, this correspond to the to term :math:`x_1^{k_1}\cdots x_r^{k_r}`.
* Therefore

	.. math:: (x_1+x_2+\cdots+x_r)^n=\sum_{\sum_{i=1}^r k_i=n} {n\choose k_1\cdots k_r} x_1^{k_1}\cdots x_r^{k_r}

Binomial theorem for fractional and negative powers: 
===============================================================
* For evaluating expressions where the power is fractional or negative, we can use the following infinite series expansion

	.. math:: (1+\delta)^\alpha=1+\alpha\delta+\frac{\alpha(\alpha-1)}{2!}\delta^2+\frac{\alpha(\alpha-1)(\alpha-2)}{3!}\delta^3+\cdots
* This series converges only when :math:`|\delta|< 1`

***********************************************
Geometry
***********************************************
.. important::
	* On the general equation of second degree: `Notes at IMSc <https://www.imsc.res.in/~svis/eme13/kesavan-new.pdf>`_.
	* [mathguy.us] `Math Handbook: Geometry <https://mathguy.us/Handbooks/GeometryHandbook.pdf>`_

***********************************************
Lagrange polynomial
***********************************************
.. note::
	* Given two points in :math:`\mathbb{R}^2`, :math:`(x_1,y_1)` and :math:`(x_2,y_2)`, the equation of a line passing through these two points is given by

		.. math:: y-y_1=\frac{y_2-y_1}{x_2-x_1}(x-x_1)

		* We can represent this in the normal :math:`y=ax+b` format as

			.. math:: y=\frac{y_2-y_1}{x_2-x_1}x+\left(y_1-\frac{y_2-y_1}{x_2-x_1}x_1\right)
	* We can represent this in Lagrange's polynomial form as the following:

		* We form Lagrange basis by taking

			* :math:`l_0(x)=\frac{x-x_1}{x_2-x_1}`
			* :math:`l_1(x)=\frac{x-x_2}{x_1-x_2}`
		* The final polynomial is formed by 

			.. math:: L(x)=y_1 l_0(x)+y_2 l_1(x)=y_1\frac{x-x_1}{x_2-x_1}+y_2\frac{x-x_2}{x_1-x_2}
	* TODO Extend to higher dimensions

Wavy Curve Method
===============================================================

***********************************************
Resources
***********************************************
.. note::
	* [math.brown.edu] `Beyond the Third Dimension <https://www.math.brown.edu/tbanchof/Beyond3d/index.html>`_
