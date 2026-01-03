################################################################################
Numerical Sequences and Series
################################################################################

********************************************************************************
Convergent Sequences
********************************************************************************

.. note::
    * **Definition (Convergent Sequence)**: A sequence :math:`\{p_n\}` in a metric space :math:`X` is convergent if :math:`\exists p \in X` such that :math:`\forall \varepsilon > 0, \exists N` with :math:`n \ge N \implies d(p_n,p) < \varepsilon`. We write :math:`p_n \to p` or :math:`\lim_{n\to\infty} p_n = p`.

.. tip::
    With every step you take, you get closer to your destination. After a certain number of steps, you are guaranteed to be within :math:`\varepsilon` of the destination. The destination is within reach.

.. remark::
    If :math:`\{p_n\}` does not converge, it is said to diverge.

.. remark::
    Since convergence requires the point :math:`p` to be in :math:`X`, the same sequence might converge in one metric space but not in another if the other space does not contain :math:`p`.

.. note::
    * **Definition (Range of a Sequence)**: The set of all points :math:`p_n` is the range of :math:`\{p_n\}`.

.. remark::
    :math:`\{p_n\}` is bounded if its range is bounded.

Sequences in general metric space
================================================================================

.. note::
    * **Theorem**: Let :math:`\{p_n\}` be a sequence in a metric space :math:`X`.

        #. :math:`\{p_n\} \to p \in X` iff every neighbourhood of :math:`p` contains :math:`p_n` for all but finitely many :math:`n`.
        #. :math:`(\{p_n\} \to p)\wedge(\{p_n\} \to p') \implies p=p'`.
        #. If :math:`\{p_n\}` converges, then :math:`\{p_n\}` is bounded.
        #. If :math:`E \subseteq X` and :math:`p` is a limit point of :math:`E`, then there exists a sequence :math:`\{p_n\}` in :math:`E` such that :math:`\{p_n\} \to p`.

Sequences in :math:`\mathbb{C}`
================================================================================

.. note::
    * **Theorem**: Let :math:`\{s_n\}` and :math:`\{t_n\}` be complex sequences such that :math:`\{s_n\}\to s` and :math:`\{t_n\}\to t`. Then

        #. :math:`\{s_n+t_n\} \to s+t`.
        #. :math:`\{s_n\cdot t_n\} \to s\cdot t`.
        #. :math:`\{c\cdot s_n\} \to c\cdot s`.
        #. :math:`\{1/s_n\} \to 1/s` where :math:`s_n\neq 0` and :math:`s\neq 0`.

Sequences in :math:`\mathbb{R}^k`
================================================================================

.. note::
    * **Theorem**: Let :math:`x_n\in \mathbb{R}^k` and :math:`x_n=(\alpha_{1,n},\cdots,\alpha_{k,n})` and :math:`x=(\alpha_1,\cdots,\alpha_k)`. Then :math:`\{x_n\}\to x` iff :math:`\alpha_{j,n}\to \alpha_j` for :math:`1\le j\le k`.

.. note::
    * **Theorem**: Suppose :math:`\{x_n\}` and :math:`\{y_n\}` are sequences in :math:`\mathbb{R}^k` and :math:`\{\beta_n\}` is a sequence of real numbers such that :math:`\{x_n\}\to x`, :math:`\{y_n\}\to y`, :math:`\{\beta_n\}\to \beta`. Then

        #. :math:`\{x_n+y_n\}\to x+y`.
        #. :math:`\{x_n\cdot y_n\}\to x\cdot y`.
        #. :math:`\{\beta_n\cdot x_n\}\to \beta\cdot x`.

********************************************************************************
Subsequences
********************************************************************************

.. note::
    * **Definition (Subsequence)**: Given a sequence :math:`\{p_n\}`, consider a sequence of positive integers :math:`\{n_k\}` with :math:`n_1<n_2<\cdots`. Then :math:`\{p_{n_k}\}` is a subsequence of :math:`\{p_n\}`.

.. tip::
    Imagine someone tracing your steps but choosing to hop and skip a few footprints as they wish.

.. note::
    * **Definition (Subsequential limit)**: If :math:`\{p_{n_k}\}\to p`, then :math:`p` is a subsequential limit of :math:`\{p_n\}`.

.. remark::
    :math:`\{p_n\}\to p \iff` every subsequential limit of :math:`\{p_n\}` is :math:`p`.

.. note::
    * **Theorem**: Every sequence in a compact metric space :math:`K` has a subsequence which converges to some point in :math:`K`.
    * **Theorem**: Every bounded sequence in :math:`\mathbb{R}^k` has a subsequence which converges to some point in :math:`\mathbb{R}^k`.
    * **Theorem**: The subsequential limits of a sequence :math:`\{p_n\}` in a metric space :math:`X` form a closed subset of :math:`X`.

********************************************************************************
Cauchy Sequences
********************************************************************************

.. note::
    * **Definition (Cauchy Sequence)**: A sequence :math:`\{p_n\}` in a metric space :math:`X` is Cauchy if :math:`\forall \varepsilon>0,\ \exists N` such that :math:`\forall n,m\ge N,\ d(p_n,p_m)<\varepsilon`.

.. tip::
    With every step you take, your step-size gets smaller. After enough steps, any two future steps are within :math:`\varepsilon` of each other. The final destination may still be out of reach.

.. note::
    * **Definition (Diameter)**: For :math:`E\subset X,\ E\neq \varnothing`, :math:`\mathrm{diam}\,E := \sup\{d(p,q)\mid p,q\in E\}`.

.. remark::
    Let :math:`\{p_n\}` be a sequence in :math:`X` and :math:`E_n` consist of the points :math:`p_N,p_{N+1},\cdots`.

    .. math:: \{p_n\}\ \text{is Cauchy} \Longleftrightarrow \mathrm{diam}\,E_N \to 0.

.. note::
    * **Theorem**: Let :math:`E^{\circ}` be the closure of a set :math:`E\subset X`, where :math:`X` is a metric space. Then :math:`\mathrm{diam}\,E^{\circ}=\mathrm{diam}\,E`.
    * **Theorem**: Let :math:`K_n` be a sequence of compact sets in :math:`X` such that :math:`K_n \supset K_{n+1}`.

        .. math:: \mathrm{diam}\,K_n \to 0 \ \Longrightarrow\ \bigcap_{n=1}^{\infty} K_n\ \text{is singleton.}

    * **Theorem**: In any metric space :math:`X`, :math:`\{p_n\}` convergent :math:`\Longrightarrow` :math:`\{p_n\}` is Cauchy.
    * **Theorem**: Every Cauchy sequence in a compact metric space :math:`K` converges to some point in :math:`K`.
    * **Theorem**: Every Cauchy sequence in :math:`\mathbb{R}^k` converges to some point in :math:`\mathbb{R}^k`.

.. note::
    * **Definition (Complete Metric Space)**: A metric space where every Cauchy sequence converges to some point is complete.

.. note::
    * **Definition (Monotonic)**: A sequence :math:`\{s_n\}` of real numbers is

        #. monotonically increasing if :math:`s_n \le s_{n+1}`,
        #. monotonically decreasing if :math:`s_n \ge s_{n+1}`.

.. note::
    * **Theorem**: Suppose :math:`\{s_n\}` is monotonic. :math:`\{s_n\}` converges :math:`\Longleftrightarrow` :math:`\{s_n\}` is bounded.

********************************************************************************
Upper and Lower Limits
********************************************************************************

.. note::
    * **Definition** (:math:`s_n\to +\infty`): Let :math:`\{s_n\}` be a sequence of real numbers, such that :math:`\forall M\in\mathbb{R},\exists N\in \mathbb{Z}^{+}` with :math:`n\ge N \implies s_n\ge M`. Write :math:`s_n\to +\infty`.
    * **Definition** (:math:`s_n\to -\infty`): Let :math:`\{s_n\}` be a sequence of real numbers, such that :math:`\forall M\in\mathbb{R},\exists N\in \mathbb{Z}^{+}` with :math:`n\ge N \implies s_n\le M`. Write :math:`s_n\to -\infty`.

.. remark::
    Difference in notation between :math:`\{s_n\}\to p` and :math:`s_n\to +\infty`.

.. remark::
    :math:`\{s_n\}\to p` is convergent whereas :math:`s_n\to +\infty` or :math:`s_n\to -\infty` are divergent.

.. note::
    * **Definition (Upper and Lower Limits)**: Let :math:`\{s_n\}` be a sequence of real numbers. Let :math:`E` be the set of numbers :math:`x\in \mathbb{R}_{\{-\infty,+\infty\}}` such that :math:`s_{n_k}\to x` for some subsequence :math:`\{s_{n_k}\}`. This set :math:`E` contains all subsequential limits and possibly :math:`-\infty` and :math:`+\infty`. Define :math:`s^{*}=\sup E` and :math:`s_{*}=\inf E` as the upper-limit and lower-limit of :math:`\{s_n\}`:

        .. math:: \limsup_{n\to\infty} s_n = s^{*}

        .. math:: \liminf_{n\to\infty} s_n = s_{*}.

.. note::
    * **Theorem**: For a sequence of real numbers :math:`\{s_n\}`:

        #. :math:`s^{*}, s_{*}\in E`.
        #. If :math:`x>s^{*}`, :math:`\exists N\in \mathbb{Z}^{+}` such that :math:`n\ge N \implies s_n < x`.
        #. If :math:`x<s_{*}`, :math:`\exists N\in \mathbb{Z}^{+}` such that :math:`n\ge N \implies s_n > x`.

.. note::
    * **Theorem**: If :math:`s_n \le t_n` for :math:`n\ge N` (some fixed :math:`N`), then

        #. :math:`\displaystyle \liminf_{n\to\infty} s_n \le \liminf_{n\to\infty} t_n`,
        #. :math:`\displaystyle \limsup_{n\to\infty} s_n \le \limsup_{n\to\infty} t_n`.

********************************************************************************
Some Special Sequences
********************************************************************************

The following limits are commonly used:

#. :math:`\displaystyle \lim_{n\to\infty}\frac{1}{n^{p}}=0`, where :math:`p>0`.
#. :math:`\displaystyle \lim_{n\to\infty} n^{1/p}=1`, where :math:`p>0`.
#. :math:`\displaystyle \lim_{n\to\infty} n^{1/n}=1`.
#. :math:`\displaystyle \lim_{n\to\infty} (n!)^{1/n}=+\infty`.
#. :math:`\displaystyle \lim_{n\to\infty} a^{n}=0`, where :math:`|a|<1`.
#. :math:`\displaystyle \lim_{n\to\infty} a^{1/n}=1`.
#. :math:`\displaystyle \lim_{n\to\infty} \left(1+\frac{1}{n}\right)^{n}=e`.
#. :math:`\displaystyle \lim_{n\to\infty} \left(1+\frac{a}{n}\right)^{bn}=e^{ab}`.
#. :math:`\displaystyle \lim_{n\to\infty} \arctan(n)=\pi/2`.
#. :math:`\displaystyle \lim_{n\to\infty} \frac{n^{\alpha}}{a^{n}}=0`, where :math:`a>1` and :math:`\alpha\in\mathbb{R}`.
#. :math:`\displaystyle \lim_{n\to\infty} \frac{P(n)}{e^{n}}=0`, where :math:`P(n)` is a polynomial.
#. :math:`\displaystyle \lim_{n\to\infty} \frac{\log(n)}{n^{a}}=0`, where :math:`a>0`.
#. :math:`\displaystyle \lim_{n\to\infty} \frac{a^{n}}{n!}=0`.

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
Summation By Parts
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
