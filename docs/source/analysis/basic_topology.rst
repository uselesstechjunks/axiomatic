################################################################################
Basic Topology
################################################################################

********************************************************************************
Metric Spaces
********************************************************************************

.. note::
    * **Metric Space**: A set :math:`X` is a metric space if there exists a function :math:`d : X \times X \to \mathbb{R}^{+}_{0}` such that for any :math:`p, q, r \in X`:

        #. :math:`d(p, q) = 0 \iff p = q`
        #. :math:`d(p, q) = d(q, p)`
        #. :math:`d(p, q) \le d(p, r) + d(r, q)`

      The function :math:`d` is called a metric/distance-function.

.. note::
    * **Points**: The elements of a metric space are called points.

.. remark::
    Every :math:`Y \subseteq X` is also a metric space with the same metric.

Useful definitions for Euclidean Space
================================================================================

.. note::
    * **Segment and Interval in :math:`\mathbb{R}`**: For :math:`a, b \in \mathbb{R}` with :math:`a < b`,

        .. math:: (a, b) := \{x \mid a < x < b\}

        .. math:: [a, b] := \{x \mid a \le x \le b\}.

.. remark::
    The notion of half-open intervals (such as :math:`(a, b]` or :math:`[a, b)`) are sometimes useful.

.. note::
    * **:math:`k`-cells in :math:`\mathbb{R}^k`**: For :math:`a_i, b_i \in \mathbb{R}` with :math:`a_i < b_i` for all :math:`i \in \{1, \dots, k\}`, a :math:`k`-cell is

        .. math:: \{x \mid a_i \le x_i \le b_i\}

      where :math:`x = (x_1, \dots, x_k)^{T} \in \mathbb{R}^k`.

.. note::
    * **Open/Closed-Balls in :math:`\mathbb{R}^k`**: For :math:`x \in \mathbb{R}^k`, an open ball (or closed ball) centered at :math:`x` with radius :math:`r > 0` is

        .. math:: B_r(x) := \{y \in \mathbb{R}^k \mid |x-y| < r\}

        .. math:: \overline{B}_r(x) := \{y \in \mathbb{R}^k \mid |x-y| \le r\}.

.. note::
    * **Convex Sets in :math:`\mathbb{R}^k`**: :math:`E \subseteq \mathbb{R}^k` is convex iff :math:`\forall x, y \in E` and :math:`\forall \lambda \in (0,1)`,

        .. math:: \lambda x + (1-\lambda)y \in E.

.. note::
    * **Theorem**: :math:`k`-cells and open/closed balls are convex sets in :math:`\mathbb{R}^k`.

Useful definitions for General Metric Space
================================================================================

.. note::
    * **Neighbourhood**: For :math:`p \in X` and :math:`r > 0`,

        .. math:: N_r(p) := \{q \in X \mid d(p,q) < r\}.

.. note::
    * **Bounded Set**: :math:`E \subseteq X` is bounded iff :math:`\exists p \in X` and :math:`\exists M > 0` such that

        .. math:: E \subseteq N_M(p).

.. note::
    * **Limit Points**: :math:`p \in X` is a limit-point of :math:`E \subseteq X` iff every neighbourhood of :math:`p` contains at least one point from :math:`E` other than :math:`p` itself:

        .. math:: \forall r>0,\ \exists q \ne p \in N_r(p)\ \text{such that } q \in E.

.. tip::
    Limit point of a set :math:`E` (which may or may not be inside :math:`E`) means we can get arbitrarily close to that point without stepping outside of :math:`E`. Limit points also form the border of :math:`E`.

.. note::
    * **Interior Points**: :math:`p \in E` is an interior point of :math:`E` iff :math:`\exists r>0` such that

        .. math:: N_r(p) \subseteq E.

.. tip::
    Interior point of a set :math:`E` (which has to be inside :math:`E`) means we have a little breathing space around that point without crossing the border of :math:`E`.

.. remark::
    The set of all limit points of :math:`E \subseteq X` is denoted :math:`E^{\uparrow}`.

.. remark::
    The set of all interior points of :math:`E \subseteq X` is denoted :math:`E^{0}`.

.. note::
    * **Isolated Points**: Points :math:`p \in E` that are not limit points of :math:`E` (:math:`p \in E \wedge p \notin E^{\uparrow}`) are isolated points of :math:`E`.

.. tip::
    Can't get close to those points without crossing :math:`E`'s border.

.. note::
    * **Closed Set**: :math:`E \subseteq X` is closed if it contains all of its own limit points (:math:`p \in E^{\uparrow} \implies p \in E`).

.. tip::
    All of :math:`E`'s border belongs to :math:`E`.

.. remark::
    A closed set can contain any number of isolated points. Since those are not limit points of that set, this does not violate the definition.

.. remark::
    A set with no limit points (:math:`E^{\uparrow} = \varnothing`) is closed by definition.

.. note::
    * **Perfect Set**: If all points of a closed set :math:`E` are limit points (:math:`p \in E \implies p \in E^{\uparrow}`), then :math:`E` is perfect.

.. tip::
    Every point in :math:`E` is reachable without stepping outside of :math:`E`.

.. remark::
    Perfect sets are not allowed to contain isolated points.

.. note::
    * **Open Set**: If all points of :math:`E` are interior points, :math:`E` is open. Symbolically,

        .. math:: p \in E \implies p \in E^{0}.

.. tip::
    Every point in :math:`E` has a little breathing space around it within :math:`E`.

.. note::
    * **Closure**: The set

        .. math:: \overline{E} := E \cup E^{\uparrow}

      is the closure of :math:`E`.

.. note::
    * **Dense Set**: :math:`E` is dense in :math:`X` iff every point in :math:`X` lies within the closure of :math:`E` (:math:`p \in X \implies p \in \overline{E}`).

Properties involving Metric Spaces
================================================================================

.. note::
    * **Theorem**: Every neighbourhood is an open set.
    * **Theorem**: If :math:`p` is a limit point of :math:`E`, then every neighbourhood of :math:`p` contains infinitely many points of :math:`E`.
    * **Corollary**: A finite set has no limit points.
    * **Theorem**: :math:`F` is closed :math:`\iff` :math:`F^{c}` is open.
    * **Theorem** (open/closed sets):

        #. For a collection of open sets :math:`\{G_{\alpha}\}`, :math:`\bigcup_{\alpha} G_{\alpha}` is open.
        #. For a collection of closed sets :math:`\{F_{\alpha}\}`, :math:`\bigcap_{\alpha} F_{\alpha}` is closed.
        #. For a finite collection of open sets :math:`\{G_i\}_{i=1}^{n}`, :math:`\bigcap_{i=1}^{n} G_i` is open.
        #. For a finite collection of closed sets :math:`\{F_i\}_{i=1}^{n}`, :math:`\bigcup_{i=1}^{n} F_i` is closed.

    * **Theorem**: For :math:`E \subseteq X`:

        #. :math:`\overline{E}` is closed.
        #. :math:`E = \overline{E}` iff :math:`E` is closed.
        #. For every closed set :math:`F \subseteq X`, :math:`E \subseteq F \implies \overline{E} \subseteq F`.

    * **Theorem**: Let :math:`E` be a nonempty set of real numbers bounded above. If :math:`y = \sup E`, then :math:`y \in \overline{E}` (and :math:`y \in E` if :math:`E` is closed).

.. note::
    * **Relatively Open**: Suppose :math:`E \subset Y \subset X`. :math:`E` is open relative to :math:`Y` if :math:`\forall p \in E`, :math:`\exists r>0` such that

        .. math:: \exists q \in Y\ \text{for which } d(p,q) < r \implies q \in E.

.. note::
    * **Example**: A set :math:`E` can be relatively open to :math:`Y` without being open in :math:`X`. For example, the segment :math:`(a,b)` is not open in :math:`\mathbb{R}^2` (any neighbourhood in :math:`\mathbb{R}^2` around a point in the segment contains orthogonal points not in the segment). However, it is relatively open to :math:`\mathbb{R}`.

.. note::
    * **Theorem**: For :math:`E \subset Y \subset X`, :math:`E` is open relative to :math:`Y` :math:`\iff E = Y \cap G` for some open set :math:`G \subset X`.

********************************************************************************
Compact Sets
********************************************************************************

Useful Definitions
================================================================================

.. note::
    * **Open Cover**: A collection of open sets :math:`\{G_{\alpha}\}` is an open cover of :math:`E \subseteq X` iff

        .. math:: E \subset \bigcup_{\alpha \in A} G_{\alpha}

      for some index set :math:`A`.

.. note::
    * **Compactness**: :math:`K \subseteq X` is compact iff every open cover of :math:`K` contains a finite subcover. Formally, for any open cover of :math:`K`, :math:`\{G_{\alpha}\}`, :math:`\exists \alpha_1, \dots, \alpha_n` for some :math:`n>0` such that

        .. math:: K \subset \bigcup_{i=1}^{n} G_{\alpha_i}.

.. note::
    * **Sequential Compactness**: :math:`K \subset X` is sequentially compact if every infinite subset :math:`E \subset K` has a limit point in :math:`K`, or equivalently, every sequence in :math:`K` has a subsequence converging to some point in :math:`K`.

Properties Related to General Metric Space
================================================================================

.. note::
    * **Theorem**: For :math:`K \subset Y \subset X`, :math:`K` is compact relative to :math:`X` :math:`\iff` :math:`K` is compact relative to :math:`Y`.

.. remark::
    This allows us to focus on a compact set without paying attention to any embedding space. Therefore, compact sets can be considered as "spaces" of their own rights.

.. note::
    * **Theorem**: Every compact set is closed.
    * **Theorem**: Every closed subset of a compact set is compact.
    * **Corollary**: If :math:`F \subset X` is closed and :math:`K \subset X` is compact :math:`\implies F \cap K` is compact.
    * **Theorem**: For a collection of compact sets :math:`\{K_{\alpha}\}`, if :math:`\bigcap_{i=1}^{n} K_{\alpha_i} \ne \varnothing` for every finite subcollection :math:`\{K_{\alpha_i}\}_{i=1}^{n}`, then

        .. math:: \bigcap_{\alpha} K_{\alpha} \ne \varnothing.

    * **Corollary**: For a sequence of non-empty compact sets :math:`\{K_n\}`, :math:`\forall n>0,\ K_n \supset K_{n+1} \implies \bigcap_{i=1}^{\infty} K_i \ne \varnothing`.
    * **Theorem**: For metric spaces, compactness :math:`\iff` sequential-compactness.

Properties Related to Euclidean Space
================================================================================

.. note::
    * **Theorem** (:math:`\mathbb{R}`): For a sequence of intervals :math:`\{I_n\}` with :math:`I_n \supset I_{n+1}` for all :math:`n>0`, we have :math:`\bigcap_{i=1}^{\infty} I_i \ne \varnothing`.

.. note::
    * **Theorem** (:math:`\mathbb{R}^k`): For a sequence of :math:`k`-cells :math:`\{I_n\}` with :math:`I_n \supset I_{n+1}` for all :math:`n>0`, we have :math:`\bigcap_{i=1}^{\infty} I_i \ne \varnothing`.

.. note::
    * **Theorem** (:math:`\mathbb{R}^k`): Every :math:`k`-cell is compact.

.. note::
    * **Theorem** (:math:`\mathbb{R}^k`): For any :math:`E \subset \mathbb{R}^k`, the following are equivalent:

        #. :math:`E` is closed and bounded.
        #. :math:`E` is compact.
        #. :math:`E` is sequentially compact.

.. remark::
    Equivalence of 1 and 2 is called the Heine-Borel theorem.

.. remark::
    Equivalence of 1 and the others is not true for general metric spaces.

.. note::
    * **Theorem** (:math:`\mathbb{R}^k`): Every bounded, infinite subset of :math:`\mathbb{R}^k` has a limit point in :math:`\mathbb{R}^k` [Bolzano-Weierstrass].

********************************************************************************
Perfect Sets
********************************************************************************

.. note::
    * **Theorem**: If :math:`P` is a nonempty, perfect set in :math:`\mathbb{R}^k`, then :math:`P` is uncountable.

.. note::
    * **Corollary**: Every interval :math:`[a,b]` is uncountable.

********************************************************************************
Connected Sets
********************************************************************************

.. note::
    * **Separated Sets**: :math:`A, B \subset X` are separated if

        .. math:: A \cap \overline{B} = \varnothing \ \wedge\ \overline{A} \cap B = \varnothing.

.. tip::
    Cannot hop off of one and hop on to another without stepping in something in between.

.. note::
    * **Connected Set**: :math:`E \subset X` is connected if it is not a union of nonempty separated sets.

.. remark::
    Separated :math:`\implies` disjoint. Converse does not hold. For example, :math:`[0,1]` and :math:`(1,2)` are disjoint but not separated.

.. note::
    * **Theorem**: For a set :math:`E \subset \mathbb{R}`,

        .. math:: E \text{ is connected } \iff (\forall x,y \in E,\ (x<z<y) \implies z \in E).
