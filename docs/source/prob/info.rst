##################################################
Information Theory
##################################################

#. Shanon Entropy
#. KL Divergence
#. Cross Entropy

*********************************************
Entropy and Mutual Information
*********************************************
.. note::
	* For a rv with PMF :math:`X\sim p_X`, the term :math:`H(X)=-\sum_x p_X(x)\lg(p_X(x))` defines entropy which is a measure of uncertainty.
	* For 2 rvs with a joint distribution :math:`p_{X,Y}(x,y)`, the term :math:`I(X,Y)=\sum_x\sum_y p_{X,Y}(x,y)\lg\left(\frac{p_{X,Y}(x,y)}{p_X(x)p_Y(y)}\right)` defines **mutual information**.
	* [Prove] Let :math:`H(X,Y)=-\sum_x\sum_y p_{X,Y}(x,y)\lg(p_{X,Y}(x,y))`. Then

		.. math:: I(X,Y)=H(X)+H(Y)-H(X,Y)
	* [Prove] Let 

		.. math:: H(X|Y)=-\sum_y p_Y(y)\sum_x p_{X|Y}(x|y)\lg(p_{X|Y}(x|y))=\mathbb{E}_Y\left[\sum_x p_{X|Y}(x|y)\lg(p_{X|Y}(x|y))\right]

	   This can be thought of as the expected conditional entropy. Then

		.. math:: I(X,Y)=H(X)-H(X|Y)

.. tip::
	* The term :math:`I(X,Y)` can be thought of as the reduction in entropy (from :math:`H(X)`) once we observe :math:`Y`. It is therefore the information about :math:`X` conveyed by :math:`Y`.
	* [Prove] If :math:`X\perp\!\!\!\perp Y`, what is the mutual information?

.. attention::
	* [Prove] Let the PMF of :math:`X=\{x_1,\cdots,x_n\}` is defined by the masses :math:`p_1,\cdots,p_n` such that :math:`\sum_{i=1}^n p_i=1`. Let us define another PMF :math:`q_1,\cdots,q_n` such that :math:`\sum_{i=1}^n q_i=1`. Then :math:`H(X)\leq-\sum_{i=1}^n p_i\lg(q_i)` and the equality holds only when :math:`p_i=q_i` for all :math:`i`.

		* [Hint] Use the inequality :math:`\ln(\alpha)=\alpha-1` for :math:`\alpha>0`.
	* As a special case of the above, :math:`H(X)\leq\lg(n)` and the equality holds when :math:`p_i=\frac{1}{n}` for all :math:`i`.


.. important::
	* Information Theory Notes from `Introduction To Renormalization <https://www.complexityexplorer.org/courses/67-introduction-to-renormalization/materials>`_
	* [SO] `Estimate the Kullback–Leibler (KL) divergence with Monte Carlo <https://stats.stackexchange.com/questions/280885/estimate-the-kullback-leibler-kl-divergence-with-monte-carlo>`_
