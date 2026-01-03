################################################################################
Numerical Sequences and Series
################################################################################

********************************************************************************
Sequences
********************************************************************************

.. note::
    * **Convergent Sequence**: :math:`\{p_n\}` converges to :math:`p` if for every :math:`\varepsilon>0` there exists :math:`N` such that :math:`n>N \Rightarrow d(p_n,p)<\varepsilon`.
    * **Cauchy Sequence**: Terms of the sequence eventually become arbitrarily close to one another.

.. note::
    * **Theorem**: Every Cauchy sequence in :math:`\R^k` converges.

********************************************************************************
Upper and Lower Limits
********************************************************************************

.. note::
    * Write :math:`s_n\to +\infty` if for every :math:`M\in\R` there exists :math:`N\in\Z^+` such that :math:`n>N\Rightarrow s_n>M`.
    * Write :math:`s_n\to -\infty` if for every :math:`M\in\R` there exists :math:`N\in\Z^+` such that :math:`n>N\Rightarrow s_n\le M`.
    * Difference in notation: :math:`\{s_n\}\to p` denotes convergence; :math:`s_n\to \pm\infty` denotes divergence.
    * **Upper/Lower Limits**: For a sequence :math:`\{s_n\}`, let :math:`E:=\{x\in \R\cup\{-\infty,+\infty\}\mid s_{n_k}\to x \text{ for some subsequence }\{s_{n_k}\}\}`. Define

        .. math:: s^*=\sup E,\qquad s_*=\inf E.

      Then

        .. math:: \limsup_{n\to\infty} s_n = s^*,\qquad \liminf_{n\to\infty} s_n = s_*.

.. note::
    * **Theorem**: For a sequence :math:`\{s_n\}`:

        #. :math:`s^*, s_*\in E`.
        #. If :math:`x>s^*`, then there exists :math:`N` such that :math:`n>N\Rightarrow s_n<x`.
        #. If :math:`x<s_*`, then there exists :math:`N` such that :math:`n>N\Rightarrow s_n>x`.
    * **Theorem**: If :math:`s_n\le t_n` for :math:`n>N`, then

        .. math:: \liminf_{n\to\infty} s_n \le \liminf_{n\to\infty} t_n,\qquad \limsup_{n\to\infty} s_n \le \limsup_{n\to\infty} t_n.

********************************************************************************
Some Special Sequences
********************************************************************************

The following limits are commonly used:

#. :math:`\displaystyle \lim_{n\to\infty} \frac{1}{n^p} = 0`, where :math:`p>0`.
#. :math:`\displaystyle \lim_{n\to\infty} n^{1/p} = 1`, where :math:`p>0`.
#. :math:`\displaystyle \lim_{n\to\infty} n^{1/n} = 1`.
#. :math:`\displaystyle \lim_{n\to\infty} (n!)^{1/n} = +\infty`.
#. :math:`\displaystyle \lim_{n\to\infty} a^n = 0`, where :math:`|a|<1`.
#. :math:`\displaystyle \lim_{n\to\infty} a^{1/n} = 1`.
#. :math:`\displaystyle \lim_{n\to\infty} \left(1+\frac{1}{n}\right)^n = e`.
#. :math:`\displaystyle \lim_{n\to\infty} \left(1+\frac{a}{n}\right)^{bn} = e^{ab}`.
#. :math:`\displaystyle \lim_{n\to\infty} \arctan n = \frac{\pi}{2}`.
#. :math:`\displaystyle \lim_{n\to\infty} \frac{n^\alpha}{a^n} = 0`, where :math:`a>1`.
#. :math:`\displaystyle \lim_{n\to\infty} \frac{P(n)}{e^n} = 0`, where :math:`P(n)` is a polynomial.
#. :math:`\displaystyle \lim_{n\to\infty} \frac{\log n}{n^a} = 0`, where :math:`a>0`.
#. :math:`\displaystyle \lim_{n\to\infty} \frac{a^n}{n!} = 0`.

********************************************************************************
Series
********************************************************************************

.. note::
    Content pending.

********************************************************************************
Series of Nonnegative Terms
********************************************************************************

.. note::
    Content pending.

********************************************************************************
The Number :math:`e`
********************************************************************************

.. note::
    Content pending.

********************************************************************************
The Root and Ratio Tests
********************************************************************************

.. note::
    Content pending.

********************************************************************************
Power Series
********************************************************************************

.. note::
    Content pending.

********************************************************************************
Summation by Parts
********************************************************************************

.. note::
    Content pending.

********************************************************************************
Absolute Convergence
********************************************************************************

.. note::
    Content pending.

********************************************************************************
Addition and Multiplication of Series
********************************************************************************

.. note::
    Content pending.

********************************************************************************
Rearrangements
********************************************************************************

.. note::
    Content pending.
