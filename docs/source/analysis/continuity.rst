################################################################################
Continuity
################################################################################

********************************************************************************
Continuity
********************************************************************************

.. note::
    * **Continuity**: :math:`f:X\to Y` is continuous at :math:`p` if for every :math:`\varepsilon>0` there exists :math:`\delta>0` such that :math:`d_X(x,p)<\delta \Rightarrow d_Y(f(x),f(p))<\varepsilon`.

.. note::
    * **Intermediate Value Theorem**: A continuous function on an interval attains every intermediate value.
    * **Theorem**: A continuous function on a compact set is uniformly continuous.

********************************************************************************
Limit of a Function
********************************************************************************

.. note::
    * **Limit of a Function**: For :math:`E\subset X`, :math:`f:E\to Y`, and :math:`p\in E^\uparrow`, if there exists :math:`q\in Y` such that for every :math:`\varepsilon>0` there exists :math:`\delta>0` with

        .. math:: 0 < d_X(x,p) < \delta \Rightarrow d_Y(f(x),q) < \varepsilon,

      then :math:`\lim_{x\to p} f(x)=q`.

.. remark::
    * The point :math:`p` need not belong to the domain of :math:`f`.
    * Even if :math:`f(p)` exists, it is possible that :math:`\lim_{x\to p} f(x)\ne f(p)`.
    * If :math:`E^\uparrow=\varnothing`, then :math:`f` has no limits.

.. note::
    * **Sequential Criterion**: :math:`\lim_{x\to p} f(x)=q` iff for every sequence :math:`\{p_n\}\subset E` with :math:`p_n\ne p` and :math:`p_n\to p`, we have :math:`f(p_n)\to q`.

********************************************************************************
Continuity (Revisited)
********************************************************************************

.. note::
    * **Continuity**: :math:`f:E\to Y` is continuous at :math:`p\in E` if for every :math:`\varepsilon>0` there exists :math:`\delta>0` such that

        .. math:: d_X(x,p)<\delta \Rightarrow d_Y(f(x),f(p))<\varepsilon.

    * **Theorem**: If :math:`p` is a limit point of :math:`E`, then :math:`f` is continuous at :math:`p` iff :math:`\lim_{x\to p} f(x)=f(p)`.

********************************************************************************
Continuity and Compactness
********************************************************************************

.. note::
    * **Theorem**: If :math:`f:X\to Y` is continuous and :math:`X` is compact, then :math:`f(X)` is compact.
    * **Theorem**: If :math:`f:X\to Y` is a continuous bijection and :math:`X` is compact, then :math:`f^{-1}` is continuous.
    * **Theorem**: If :math:`f:X\to\R` is continuous and :math:`X` is compact, then :math:`f` attains its maximum and minimum.

********************************************************************************
Uniform Continuity
********************************************************************************

.. note::
    * **Uniform Continuity**: :math:`f:X\to Y` is uniformly continuous if for every :math:`\varepsilon>0` there exists :math:`\delta>0` such that

        .. math:: d_X(p,q)<\delta \Rightarrow d_Y(f(p),f(q))<\varepsilon

      for all :math:`p,q\in X`.
    * **Theorem**: If :math:`X` is compact, then every continuous function :math:`f:X\to Y` is uniformly continuous.

********************************************************************************
Lipschitz Continuity
********************************************************************************

.. note::
    * **Lipschitz Continuity**: :math:`f:X\to Y` is Lipschitz if there exists :math:`K>0` such that

        .. math:: d_Y(f(p),f(q))\le K\,d_X(p,q)

      for all :math:`p,q\in X`.
    * **Theorem**: Every Lipschitz continuous function is uniformly continuous.

********************************************************************************
Connectedness
********************************************************************************

.. note::
    * **Theorem**: If :math:`f:X\to Y` is continuous and :math:`E\subset X` is connected, then :math:`f(E)` is connected.
    * **Intermediate Value Theorem** (interval form): If :math:`f:[a,b]\to\R` is continuous, then it attains every value between :math:`f(a)` and :math:`f(b)`.

********************************************************************************
Monotonic Functions
********************************************************************************

.. note::
    * **Theorem**: If :math:`f:(a,b)\to\R` is monotonic, then the set of its discontinuities is at most countable.
