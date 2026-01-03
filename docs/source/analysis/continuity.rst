################################################################################
Continuity
################################################################################

********************************************************************************
Continuous Functions
********************************************************************************

Definitions and Basic Properties
================================================================================

.. note::
    * **Function**: Let :math:`X, Y` be sets. A function :math:`f` from :math:`X` to :math:`Y` is a rule which assigns to each element :math:`x \in X` a unique element :math:`y \in Y`, denoted by :math:`y = f(x)`.

.. note::
    * **Limit of a Function**: Let :math:`X, Y` be metric spaces, :math:`E \subset X`, :math:`p` a limit point of :math:`E`, and :math:`f : E \to Y`. We say that

        .. math:: \lim_{x \to p} f(x) = q

      if for every :math:`\varepsilon > 0` there exists a :math:`\delta > 0` such that

        .. math:: d_X(x,p) < \delta,\ x \in E,\ x \ne p \implies d_Y(f(x), q) < \varepsilon.

.. remark::
    The value of :math:`f(p)` plays no role in the definition of :math:`\lim_{x \to p} f(x)`.

.. note::
    * **Continuity at a Point**: Let :math:`f : E \to Y`, where :math:`E \subset X`. The function :math:`f` is continuous at :math:`p \in E` if

        .. math:: \lim_{x \to p} f(x) = f(p).

.. tip::
    Continuity at :math:`p` means that the value of the function at :math:`p` agrees with the values arbitrarily close to :math:`p`.

.. note::
    * **Continuity on a Set**: :math:`f : E \to Y` is continuous on :math:`E` if it is continuous at every point :math:`p \in E`.

Equivalent Characterizations
================================================================================

.. note::
    * **Theorem**: Let :math:`f : E \to Y`, where :math:`E \subset X`. Then :math:`f` is continuous at :math:`p \in E` iff for every sequence :math:`\{x_n\} \subset E` such that :math:`x_n \to p`, we have

        .. math:: f(x_n) \to f(p).

.. remark::
    This is often called the sequential characterization of continuity.

.. note::
    * **Theorem**: Let :math:`f : E \to Y` be continuous at :math:`p \in E`. Then for every neighbourhood :math:`V` of :math:`f(p)`, there exists a neighbourhood :math:`U` of :math:`p` such that

        .. math:: f(U \cap E) \subset V.

.. note::
    * **Theorem**: A function :math:`f : E \to Y` is continuous on :math:`E` iff for every open set :math:`G \subset Y`, the set

        .. math:: f^{-1}(G) = \{x \in E \mid f(x) \in G\}

      is open relative to :math:`E`.

Algebra of Continuous Functions
================================================================================

.. note::
    * **Theorem**: Suppose :math:`f, g : E \to \mathbb{R}` are continuous at :math:`p \in E`. Then the functions

        .. math:: f+g,\quad f-g,\quad fg

      are continuous at :math:`p`. If :math:`g(p) \ne 0`, then :math:`\frac{f}{g}` is also continuous at :math:`p`.

.. note::
    * **Theorem**: If :math:`f : E \to Y` is continuous at :math:`p \in E` and :math:`g : f(E) \to Z` is continuous at :math:`f(p)`, then the composition

        .. math:: g \circ f : E \to Z

      is continuous at :math:`p`.

********************************************************************************
Continuous Functions on Compact Sets
********************************************************************************

Basic Results
================================================================================

.. note::
    * **Theorem**: Let :math:`K` be a compact subset of a metric space :math:`X`, and let :math:`f : K \to Y` be continuous. Then :math:`f(K)` is compact in :math:`Y`.

.. note::
    * **Corollary**: If :math:`f : K \to \mathbb{R}` is continuous on a compact set :math:`K`, then :math:`f` is bounded on :math:`K` and attains its maximum and minimum values.

.. tip::
    Continuous functions on compact sets behave like functions on closed intervals.

.. note::
    * **Extreme Value Theorem**: Let :math:`K \subset X` be compact and :math:`f : K \to \mathbb{R}` continuous. Then :math:`\exists p, q \in K` such that

        .. math:: f(p) \le f(x) \le f(q) \quad \forall x \in K.

********************************************************************************
Uniform Continuity
********************************************************************************

.. note::
    * **Uniform Continuity**: A function :math:`f : E \to Y` is uniformly continuous on :math:`E` if for every :math:`\varepsilon > 0` there exists a :math:`\delta > 0` such that

        .. math:: d_X(x,y) < \delta \implies d_Y(f(x), f(y)) < \varepsilon \quad \forall x,y \in E.

.. tip::
    Uniform continuity removes dependence on the base point.

.. note::
    * **Theorem**: Every uniformly continuous function is continuous.
    * **Theorem**: Every continuous function on a compact set is uniformly continuous.
    * **Corollary**: If :math:`f : [a,b] \to \mathbb{R}` is continuous, then :math:`f` is uniformly continuous.

********************************************************************************
Connectedness and Continuity
********************************************************************************

.. note::
    * **Theorem**: If :math:`E \subset X` is connected and :math:`f : E \to Y` is continuous, then :math:`f(E)` is connected.

.. note::
    * **Corollary** (Intermediate Value Theorem): Let :math:`f : [a,b] \to \mathbb{R}` be continuous. If :math:`f(a) < c < f(b)`, then :math:`\exists x \in (a,b)` such that

        .. math:: f(x) = c.

.. remark::
    The Intermediate Value Property characterizes connected subsets of :math:`\mathbb{R}`.

********************************************************************************
Discontinuities
********************************************************************************

.. note::
    * **Discontinuity**: A function :math:`f : E \to Y` is discontinuous at :math:`p \in E` if it is not continuous at :math:`p`.

.. note::
    * **Theorem**: Let :math:`f : \mathbb{R} \to \mathbb{R}` be monotone. Then the set of points at which :math:`f` is discontinuous is at most countable.

.. remark::
    Monotone functions can only have jump discontinuities.
