################################################################################
Continuity
################################################################################

.. note::
    * Throughout, :math:`X` and :math:`Y` are metric spaces with metrics :math:`d_X` and :math:`d_Y`, respectively.

********************************************************************************
Limit of a Function
********************************************************************************

.. note::
    * **Definition (Limit of a Function)**: Let :math:`E \subset X`, :math:`f : E \to Y` and :math:`p \in E^{\uparrow}`. If

        .. math:: \exists q \in Y.\ \forall \varepsilon > 0.\ \exists \delta > 0.\ \forall x \in E.\ \bigl(0 < d_X(x,p) < \delta \Longrightarrow d_Y(f(x),q) < \varepsilon\bigr),

      then the limit of :math:`f` at :math:`p` is :math:`\displaystyle \lim_{x\to p} f(x)=q`.

.. tip::
    As you move close to a point, your shadow also moves close to some point in the shadow-verse.

.. remark::
    * :math:`p` does not have to be in the domain (in which case :math:`f(p)` is not even defined). We can still have :math:`f`'s limit defined at :math:`p`.
    * Even if :math:`p` is within the domain and :math:`f(p)` exists, it is possible that :math:`\displaystyle \lim_{x\to p} f(x) \ne f(p)`.
    * :math:`q` does not have to be inside the range of :math:`f`.
    * If :math:`E` is a set of isolated points, i.e. :math:`E^{\uparrow}=\varnothing`, then any function :math:`f:E\to Y` would not have limits defined at any point.

.. note::
    * **Theorem**: Consider every sequence of points :math:`\{p_n\}` in :math:`E` converging towards :math:`p` (with :math:`p_n \ne p`). Then their images in :math:`Y` under :math:`f`, :math:`p_n \mapsto f(p_n)`, also converge towards some :math:`q \in Y` iff the limit of :math:`f` at :math:`p` is :math:`q`. Symbolically,

        .. math:: \lim_{x\to p} f(x)=q \iff \forall\{p_n\}\in E,\ p_n\ne p,\ \bigl(\lim_{n\to\infty} p_n=p \Longrightarrow \lim_{n\to\infty} f(p_n)=q\bigr).

.. remark::
    * If :math:`f` has a limit at :math:`p`, it is unique.

Limits of Real and Complex Valued Functions
================================================================================

Let :math:`E \subset X` be a metric space and :math:`f:E\to \mathbb{C}` and :math:`g:E\to\mathbb{C}` be two complex valued functions.

.. note::
    * **Definition**: Define

        #. :math:`f+g:E\to\mathbb{C}` as :math:`(f+g)(x)=f(x)+g(x)`
        #. :math:`f-g:E\to\mathbb{C}` as :math:`(f-g)(x)=f(x)-g(x)`
        #. :math:`fg:E\to\mathbb{C}` as :math:`(fg)(x)=f(x)g(x)`
        #. :math:`f/g:E\to\mathbb{C}` as :math:`(f/g)(x)=f(x)/g(x)` where :math:`g(x)\ne 0`

.. note::
    * **Theorem**: Let :math:`p \in E^{\uparrow}` and :math:`\displaystyle \lim_{x\to p} f(x)=s` and :math:`\displaystyle \lim_{x\to p} g(x)=t`. Then

        #. :math:`\displaystyle \lim_{x\to p} (f+g)(x)=s+t`
        #. :math:`\displaystyle \lim_{x\to p} (f-g)(x)=s-t`
        #. :math:`\displaystyle \lim_{x\to p} (fg)(x)=st`
        #. :math:`\displaystyle \lim_{x\to p} (f/g)(x)=s/t` where :math:`t\ne 0`

Limits of Euclidean Vector Valued Functions
================================================================================

Let :math:`E \subset X` be a metric space and :math:`f:E\to\mathbb{R}^k` and :math:`g:E\to\mathbb{R}^k` be Euclidean vector valued functions.

.. note::
    * **Definition**: Define

        #. :math:`f+g:E\to\mathbb{R}^k` as :math:`(f+g)(x)=f(x)+g(x)`
        #. :math:`f\cdot g:E\to\mathbb{R}` as :math:`(f\cdot g)(x)=f(x)\cdot g(x)`

.. note::
    * **Theorem**: Let :math:`p \in E^{\uparrow}` and :math:`\displaystyle \lim_{x\to p} f(x)=u` and :math:`\displaystyle \lim_{x\to p} g(x)=v`. Then

        #. :math:`\displaystyle \lim_{x\to p} (f+g)(x)=u+v`
        #. :math:`\displaystyle \lim_{x\to p} (f\cdot g)(x)=u\cdot v`

********************************************************************************
Continuity
********************************************************************************

.. note::
    * **Definition (Continuity)**: Let :math:`E \subset X`, :math:`f:E\to Y` and :math:`p\in E`. If

        .. math:: \forall \varepsilon>0.\ \exists \delta>0.\ \forall x\in E.\ \bigl(d_X(x,p)<\delta \Longrightarrow d_Y(f(x),f(p))<\varepsilon\bigr),

      then :math:`f` is continuous at :math:`p`.

.. tip::
    As you move close to a point, your shadow moves close to the shadow of that point.

.. note::
    * **Definition (Continuous on :math:`E`)**: :math:`f` is continuous on :math:`E` if it is continuous :math:`\forall p\in E`.

.. tip::
    If you are neighbours, you would end up as neighbours.

.. remark::
    * The function can only be continuous at points within its domain.
    * If :math:`p` is an isolated point in :math:`E`, then every :math:`f:E\to Y` is continuous at :math:`p`.

.. note::
    * **Theorem**: If :math:`p` is a limit point of :math:`E`, then :math:`f` is continuous at :math:`p` :math:`\iff \displaystyle \lim_{x\to p} f(x)=f(p)`.

.. remark::
    * Unlike limits, where a point :math:`p` outside of the domain can have limits defined, continuity concerns only points inside the domain. So instead of subsets :math:`E\subset X`, we can talk about continuous functions mapping from a metric space :math:`X` to another :math:`Y`.

Continuity of Function Composition
================================================================================

Let :math:`X,Y,Z` be metric spaces. For :math:`E\subset X`, let :math:`f:E\to Y` and :math:`g:f(E)\to Z`.

.. note::
    * **Theorem**: If :math:`f` is continuous at :math:`p\in E` and :math:`g` is continuous at :math:`f(p)`, then :math:`g\circ f` is continuous at :math:`p`.

Continuity of Functions on Open/Closed Sets
================================================================================

.. note::
    * **Theorem**: For :math:`f:X\to Y`, :math:`f` is continuous iff for every open set :math:`V\in Y`, the inverse image :math:`f^{-1}(V)` is open in :math:`X`.

.. note::
    * **Corollary**: In the above case, for every closed set :math:`C\in Y`, :math:`f^{-1}(C)` is closed in :math:`X`.

.. tip::
    Continuous maps preserve openness/closeness.

Continuity of Real and Complex Valued Functions
================================================================================

Let :math:`f:X\to\mathbb{C}` and :math:`g:X\to\mathbb{C}` be complex valued functions.

.. note::
    * **Theorem**: If :math:`f` and :math:`g` are continuous on :math:`X`, then :math:`f+g`, :math:`f-g`, :math:`fg` and :math:`f/g` are continuous on :math:`X`.

Continuity of Euclidean Vector Valued Functions
================================================================================

Let :math:`f_1:X\to\mathbb{R}, \cdots, f_k:X\to\mathbb{R}` be real valued functions and let :math:`f:X\to\mathbb{R}^k` be defined as :math:`f(x)=(f_1(x),\cdots,f_k(x))` for :math:`x\in X`.

.. note::
    * **Theorem**: :math:`f` is continuous :math:`\iff` each of :math:`f_1,\cdots,f_k` is continuous.
    * **Theorem**: If :math:`f:X\to\mathbb{R}^k` and :math:`g:X\to\mathbb{R}^k` are continuous, then :math:`f+g` and :math:`f\cdot g` are continuous.

********************************************************************************
Continuity and Compactness
********************************************************************************

Generic Functions on Compact Domain
================================================================================

.. note::
    * **Theorem**: Let :math:`f:X\to Y` be a continuous map where :math:`X` is compact. Then :math:`f(X)` is compact.
    * **Theorem**: Let :math:`f:X\to Y` be a continuous bijection where :math:`X` is compact. Then the inverse map :math:`f^{-1}(f(x))=x` for :math:`x\in X` is a continuous mapping of :math:`Y` onto :math:`X`.

Euclidean Vector Valued Functions on Compact Domain
================================================================================

.. note::
    * **Definition (Bounded Function)**: :math:`f:E\to\mathbb{R}^k` is bounded iff :math:`\exists M>0` such that :math:`\forall x\in E,\ |f(x)|\le M`.

.. note::
    * **Theorem**: Let :math:`f:X\to\mathbb{R}^k` be continuous where :math:`X` is compact. Then (a) :math:`f(X)` is closed and bounded and (b) :math:`f` is bounded.

Real Valued Functions on Compact Domain
================================================================================

.. note::
    * **Theorem**: Let :math:`f:X\to\mathbb{R}` be continuous where :math:`X` is compact. Then :math:`\exists p,q\in X` such that

        .. math:: f(p)=\sup_{x\in X} f(x) \qquad f(q)=\inf_{x\in X} f(x).

Uniform Continuity and Compactness
================================================================================

.. note::
    * **Definition (Uniform Continuity)**: :math:`f:X\to Y` is uniformly continuous on :math:`X` iff

        .. math:: \forall \varepsilon>0.\ \exists \delta>0.\ \forall p,q\in X.\ d_X(p,q)<\delta \Longrightarrow d_Y(f(p),f(q))<\varepsilon.

.. tip::
    There is a mandate on how far your neighbours can relocate from you.

.. remark::
    * The difference between continuous on :math:`X` and uniformly continuous on :math:`X` is that, for the continuous case, :math:`\delta` may depend on the point and on :math:`\varepsilon`; for uniform continuity, for every :math:`\varepsilon`, there is a single :math:`\delta` that works for every point.

.. note::
    * **Theorem**: If :math:`X` is compact, then every continuous map :math:`f:X\to Y` is uniformly continuous.

Lipschitz Continuity
================================================================================

.. note::
    * **Definition (Lipschitz Continuity)**: :math:`f:X\to Y` is Lipschitz continuous on :math:`X` iff

        .. math:: \exists K>0.\ \forall p,q\in X.\ d_Y(f(p),f(q))\le K\cdot d_X(p,q)

      where :math:`K\in\mathbb{R}` is the Lipschitz constant.

.. remark::
    * Lipschitz continuous functions have bounded difference quotients (slopes of any line joining two points on the graph are bounded by the Lipschitz constant).

.. note::
    * **Theorem**: Let :math:`f:[a,b]\to\mathbb{R}` be continuous on :math:`[a,b]`, differentiable in :math:`(a,b)`. If :math:`f'` is bounded, then :math:`f` is Lipschitz continuous.
    * **Theorem**: Every Lipschitz continuous function is uniformly continuous.

.. remark::
    * The converse is not true. For example, :math:`f:[0,1]\to\mathbb{R}`, :math:`f(x)=\sqrt{x}` is uniformly continuous but not Lipschitz (unbounded derivative near :math:`0`).

.. tip::
    Having steeper and steeper derivative need not be an issue for uniform continuity, but it kills Lipschitz continuity.

********************************************************************************
Continuity and Connectedness
********************************************************************************

.. note::
    * **Theorem**: Let :math:`f:X\to Y` be continuous. If :math:`E\subset X` is connected, then :math:`f(E)` is connected.

.. note::
    * **Theorem (Intermediate Value Theorem)**: Let :math:`f:[a,b]\to\mathbb{R}` be continuous. Then :math:`f` attains all intermediate values between :math:`f(a)` and :math:`f(b)`. If :math:`f(a)<f(b)`, then :math:`\forall c` with :math:`f(a)<c<f(b)` there exists :math:`x\in(a,b)` such that :math:`f(x)=c`.

.. remark::
    * Attaining all intermediate values does not imply that the function is continuous on :math:`[a,b]`.

.. note::
    * **Corollary (Bolzano's theorem)**: If a continuous function has values of opposite sign inside an interval, then it has a root in that interval.
    * **Theorem (Fixed Point Theorem)**: Let :math:`f:[a,b]\to[a,b]` be continuous. Then :math:`\exists x\in[a,b]` such that :math:`f(x)=x`.

********************************************************************************
Discontinuities
********************************************************************************

.. note::
    * **Definition**: If :math:`f:X\to Y` is not continuous at some :math:`x\in X`, then :math:`f` is discontinuous at :math:`x`.

.. note::
    The following definitions and properties apply to functions defined on an interval :math:`(a,b)\in\mathbb{R}` or a segment :math:`[a,b]\in\mathbb{R}`.

.. note::
    * **Definition (Left-hand limit)**: Let :math:`f:(a,b)\to Y`. For :math:`x\in(a,b]`, let :math:`\{t_n\}` be a sequence in :math:`(a,x)` such that

        .. math:: \lim_{n\to\infty} t_n=x \Longrightarrow \lim_{n\to\infty} f(t_n)=q.

      Then :math:`f(x-)=q`.

.. remark::
    * Left-hand limit is well defined at the right endpoint :math:`b` even when the function is not defined there.

.. note::
    * **Definition (Right-hand limit)**: Let :math:`f:(a,b)\to Y`. For :math:`x\in[a,b)`, let :math:`\{t_n\}` be a sequence in :math:`(x,b)` such that

        .. math:: \lim_{n\to\infty} t_n=x \Longrightarrow \lim_{n\to\infty} f(t_n)=q.

      Then :math:`f(x+)=q`.

.. remark::
    * Right-hand limit is well defined at the left endpoint :math:`a` even when the function is not defined there.
    * At any :math:`x\in(a,b)`, :math:`\displaystyle \lim_{t\to x} f(t)` exists iff :math:`f(x-)=\displaystyle \lim_{t\to x} f(t)=f(x+)`.

.. note::
    * **Definition (Discontinuity of First Kind)**: If :math:`f:(a,b)\to Y` is discontinuous at :math:`x\in(a,b)` but :math:`f(x+)` and :math:`f(x-)` exist, then :math:`f` has a discontinuity of first kind (simple discontinuity) at :math:`x`.
    * **Definition (Discontinuity of Second Kind)**: If :math:`f:(a,b)\to Y` is discontinuous at :math:`x\in(a,b)` and the discontinuity is not simple, it has a discontinuity of second kind at :math:`x`.

.. remark::
    * Discontinuity of first kind can occur in two ways:

        #. :math:`f(x+) \ne f(x-)`
        #. :math:`f(x+)=f(x-) \ne \displaystyle \lim_{t\to x} f(t)`

.. note::
    * **Definition**: If :math:`f(x-)=f(x)` we say that :math:`f` is continuous from the left at :math:`x`.
    * **Definition**: If :math:`f(x+)=f(x)` we say that :math:`f` is continuous from the right at :math:`x`.

The following sections apply to real valued functions :math:`f:X\to\mathbb{R}`.

********************************************************************************
Monotonic Functions
********************************************************************************

.. note::
    * **Definition (Monotonically Increasing)**: :math:`f:(a,b)\to\mathbb{R}` is monotonically increasing on :math:`(a,b)` if

        .. math:: a<x<y<b \Longrightarrow f(x)\le f(y).

.. remark::
    * Monotonically decreasing functions are defined similarly with :math:`a<x<y<b \Longrightarrow f(x)\ge f(y)`.

.. note::
    * **Theorem**: Let :math:`f:(a,b)\to\mathbb{R}` be monotonically increasing. Then :math:`\forall x\in(a,b)`, :math:`f(x+)` and :math:`f(x-)` exist and

        .. math:: \sup_{a<t<x} f(t)=f(x-)\le f(x)\le f(x+)=\inf_{x<t<b} f(t).

      Also, :math:`a<x<y<b \Longrightarrow f(x+)\le f(y-)`.

.. remark::
    * Analogous results follow for monotonically decreasing functions.
    * Monotonic functions do not have discontinuities of second kind.

.. note::
    * **Theorem**: Let :math:`f:(a,b)\to\mathbb{R}` be monotonic. The set of points in :math:`(a,b)` at which :math:`f` is discontinuous is at most countable.

********************************************************************************
Infinite Limits and Limits at Infinity
********************************************************************************

.. note::
    * **Definition**: The neighbourhood of :math:`x` is any segment :math:`(x-\delta,x+\delta)`.
    * **Definition**: For :math:`c\in\mathbb{R}`, the set :math:`(c,+\infty):=\{x\mid x>c\}` is the neighbourhood of :math:`+\infty` and :math:`(-\infty,c):=\{x\mid x<c\}` is the neighbourhood of :math:`-\infty`.

.. note::
    * **Definition**: Let :math:`E\subset \mathbb{R}`. For :math:`f:E\to \mathbb{R}\cup\{+\infty,-\infty\}`, :math:`\displaystyle \lim_{x\to p} f(x)=q` iff

        .. math:: \forall N_Y(q).\ \exists N_X(p).\ x\in N_X^{*}(p)\cap E \Longrightarrow f(x)\in N_Y(q)

      where :math:`N_X(p)\cap E\ne\varnothing`.

.. note::
    * **Theorem**: Let :math:`f` and :math:`g` be defined on :math:`E\subset \mathbb{R}` and :math:`\displaystyle \lim_{t\to x} f(t)=A` and :math:`\displaystyle \lim_{t\to x} g(t)=B`.

        #. :math:`f(t)\to A' \Longrightarrow A'=A`
        #. :math:`(f+g)(t)\to A+B`
        #. :math:`(fg)(t)\to AB`
        #. :math:`(f/g)(t)\to A/B`.
