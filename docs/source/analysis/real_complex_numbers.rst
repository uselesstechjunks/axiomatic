################################################################################
The Real and Complex Number Systems
################################################################################

********************************************************************************
Groups
********************************************************************************

.. note::
    * **Symmetry**: A symmetry is a bijection from a set to itself, :math:`s:X\to X`.

.. tip::
    Symmetry is a way of relabelling the items.

.. note::
    * **Examples** (intuition for symmetries):

        #. The trivial symmetry is the identity map that maps every element of a set onto itself.
        #. A set of 3 points arranged in a circle has a cyclic symmetry (rotate the circle :math:`1/3` of a revolution, mapping the points accordingly).
        #. The set of all permutations of a finite set define symmetries, where any element can map to any other element.
        #. :math:`\forall n \in \mathbb{Z}` define a symmetry :math:`x \in \mathbb{Z} \mapsto n + x \in \mathbb{Z}` (sliding the number line).
        #. :math:`\forall n \in \mathbb{Q}` define a symmetry :math:`x \in \mathbb{Q} \mapsto n \cdot x \in \mathbb{Q}` (stretching the number line).
        #. For a finite-dimensional vector space over :math:`\mathbb{R}`, :math:`\mathbb{R}^n`, the set of non-singular :math:`n \times n` matrices define symmetries since it maps any vector :math:`u \in \mathbb{R}^n \mapsto Au \in \mathbb{R}^n` (Generalised Linear Group of order :math:`n` or :math:`\mathrm{GL}_n(\mathbb{R})`).

.. remark::
    The idea of groups comes from symmetries, where an operator is defined to denote the composition of symmetries. Even when not explicitly specified, there is a symmetry associated with every element in a group. The associativity follows from the fact that function composition is associative. Also, since symmetries are bijections, we have inverses in each case.

.. note::
    * **Group**: A group is a set :math:`G` with a binary operation :math:`(+)` that satisfies:

        #. :math:`\forall x, y \in G, (x + y) \in G`  [Closure]
        #. :math:`\forall x, y, z \in G, ((x + y) + z) = (x + (y + z))`  [Associativity]
        #. :math:`\exists 0 \in G` such that :math:`\forall x \in G, (x + 0) = (0 + x) = x`  [Identity Element]
        #. :math:`\forall x \in G, \exists (-x) \in G` such that :math:`(x + (-x)) = ((-x) + x) = 0`  [Inverse Element]

.. remark::
    Groups are fully specified using the notation :math:`(G, +, 0)`.

.. note::
    * **Proposition**: For a group :math:`(G, +, 0)` and :math:`\forall x, y, z \in G`:

        #. :math:`(x + y = x + z) \Longrightarrow y = z`  [Cancellation Law]
        #. :math:`(x + y) = x \Longrightarrow y = 0`  [Uniqueness of Identity]
        #. :math:`(x + y) = 0 \Longrightarrow y = (-x)`  [Uniqueness of Inverse]
        #. :math:`-(-x) = x`  [Repeated Inverse]

.. remark::
    If :math:`(\cdot)` is used to denote the group operation, it is customary to express the identity element as :math:`1` and the inverse element of :math:`x` as :math:`x^{-1}`. The group is specified as :math:`(G, \cdot, 1)`.

.. note::
    * **Commutative Group** (Abelian): A group that follows the additional axiom

        .. math:: \forall x, y \in G, (x + y) = (y + x).

********************************************************************************
Fields
********************************************************************************

.. note::
    * **Field**: A field is a set :math:`F` with two binary operations, :math:`(+)` and :math:`(\cdot)`, which satisfy:

        #. :math:`(F, +, 0)` is a commutative group  [Additive Group]
        #. :math:`(F \setminus \{0\}, \cdot, 1)` is a commutative group  [Multiplicative Group]
        #. :math:`\forall x, y, z \in F, (x \cdot (y + z)) = ((x \cdot y) + (x \cdot z))`  [Distributive Property]

.. remark::
    Fields are fully specified as :math:`(F, +, 0, \cdot, 1)`.

.. note::
    * **Proposition**: For a field :math:`(F, +, 0, \cdot, 1)` and :math:`\forall x, y \in F`:

        #. :math:`(x \cdot 0) = (0 \cdot x) = 0`
        #. :math:`(x \ne 0) \wedge (y \ne 0) \Longrightarrow (x \cdot y) \ne 0`
        #. :math:`(-x) \cdot y = x \cdot (-y) = -(x \cdot y)`
        #. :math:`(-x) \cdot (-y) = x \cdot y`

********************************************************************************
Ordered Sets
********************************************************************************

.. note::
    * **Order**: For a set :math:`S`, an order :math:`(<)` is a relation such that:

        #. For all :math:`x, y \in S`, exactly one of :math:`x < y`, :math:`x = y`, :math:`y < x` is true.
        #. For all :math:`x, y, z \in S`, :math:`(x < y) \wedge (y < z) \Longrightarrow (x < z)`.

.. note::
    * **Partial Order**: A partial order :math:`(\le)` has:

        #. :math:`x \le x`  [Reflexive]
        #. :math:`(x \le y) \wedge (y \le x) \Longrightarrow (x = y)`  [Anti-symmetric]
        #. :math:`(x \le y) \wedge (y \le z) \Longrightarrow (x \le z)`  [Transitive]

      Partial order alone is not a total order. To obtain a total order, also require:

        #. :math:`\forall x, y \in S, (x \le y) \vee (y \le x)`  [Connex]
        #. :math:`\forall x, y \in S, (x \le y) \Longleftrightarrow \neg (y < x)`.

.. note::
    * **Ordered Set**: A set :math:`S` for which an order is defined.
    * **Poset**: A set :math:`S` for which a partial-order is defined.
    * **Upper Bound**: For :math:`E \subseteq S`, :math:`\beta \in S` is an upper bound if :math:`\forall x \in E, x \le \beta`.
    * **Bounded Above**: :math:`E` is bounded above if it has an upper bound.
    * **Least Upper Bound**: If :math:`\alpha` is an upper bound of :math:`E` and for every :math:`\gamma < \alpha`, :math:`\gamma` is not an upper bound of :math:`E`, then :math:`\alpha = \sup E`.
    * **Greatest Lower Bound / Infimum**: Defined similarly for sets bounded below, :math:`\alpha = \inf E`.
    * **Least Upper Bound Property (Completeness)**: An ordered set has this property if every non-empty bounded-above set :math:`E \subseteq S` has :math:`\sup E \in S`.

.. note::
    * **Theorem**: Let :math:`S` be an ordered set with the least upper bound property. Let :math:`B \subseteq S` be non-empty and bounded below. Let :math:`L` be the set of all lower bounds of :math:`B`. Then there exists :math:`\alpha \in S` such that :math:`\alpha = \sup L = \inf B`. Hence :math:`\inf B \in S`.

********************************************************************************
Ordered Field
********************************************************************************

.. note::
    * **Ordered Field**: A field :math:`F` that is also an ordered set, such that:

        #. :math:`x, y, z \in F,\ y < z \Longrightarrow x + y < x + z`
        #. :math:`x, y \in F,\ (x > 0) \wedge (y > 0) \Longrightarrow x \cdot y > 0`

********************************************************************************
The Real Field
********************************************************************************

.. note::
    * **Real Field**: There exists an ordered field :math:`\mathbb{R}` with the least upper bound property. Moreover, :math:`\mathbb{Q} \subset \mathbb{R}` is a subfield. The elements are called real numbers.

.. note::
    * **Theorem** (properties of :math:`\mathbb{R}` and :math:`\mathbb{Q}`):

        #. If :math:`x, y \in \mathbb{R},\ x > 0`, then :math:`\exists n \in \mathbb{Z}^{+}` such that :math:`n \cdot x > y`  [Archimedean property]
        #. If :math:`x, y \in \mathbb{R},\ x < y`, then :math:`\exists p \in \mathbb{Q}` such that :math:`x < p < y`  [:math:`\mathbb{Q}` dense in :math:`\mathbb{R}`]

.. note::
    * **Theorem**: For :math:`x \in \mathbb{R}^{+}` and :math:`n \in \mathbb{Z}^{+}`, there exists a unique :math:`y \in \mathbb{R}^{+}` such that :math:`y^{n} = x`.

.. note::
    * **Corollary**: For :math:`a, b \in \mathbb{R}^{+}` and :math:`n \in \mathbb{Z}^{+}`, :math:`(a \cdot b)^{1/n} = a^{1/n} \cdot b^{1/n}`.

.. note::
    * **Decimal expansion of reals**: For :math:`x \in \mathbb{R}^{+}`, let :math:`E` be the set

        .. math:: n_0 + \frac{n_1}{10} + \frac{n_2}{10^{2}} + \cdots + \frac{n_k}{10^{k}}.

      Then :math:`x = \sup E`.

********************************************************************************
Extended Real Number System
********************************************************************************

.. note::
    * **Extended reals**: :math:`\mathbb{R}` together with two symbols :math:`-\infty` and :math:`+\infty`, with :math:`\forall x \in \mathbb{R},\, -\infty < x < +\infty`.

.. remark::
    * :math:`+\infty` is an upper bound for every subset of the extended reals, so every non-empty set has a least upper bound; similarly for :math:`-\infty` and greatest lower bound.
    * The extended real number system is no longer a field.
    * Conventions:

        #. :math:`\forall x \in \mathbb{R}`, (a) :math:`x + \infty = \infty` (b) :math:`x - \infty = -\infty` (c) :math:`x/\infty = x/ -\infty = 0`.
        #. :math:`\forall x \in \mathbb{R}^{+}`, (a) :math:`x \cdot +\infty = +\infty` (b) :math:`x \cdot -\infty = -\infty`.
        #. :math:`\forall x \in \mathbb{R}^{-}`, (a) :math:`x \cdot +\infty = -\infty` (b) :math:`x \cdot -\infty = +\infty`.

********************************************************************************
The Complex Field
********************************************************************************

.. note::
    * **Complex Numbers**: Ordered pairs :math:`(a, b)` of real numbers, where for :math:`x = (a, b)` and :math:`y = (c, d)`:

        #. :math:`(x = y) \Longleftrightarrow (a = c) \wedge (b = d)`  [Equality]
        #. :math:`x + y = (a + c, b + d)`  [Addition]
        #. :math:`x \cdot y = (ac - bd, ad + bc)`  [Multiplication]

.. remark::
    For :math:`x = (a, b)`, write :math:`a = \mathrm{Re}(x)` and :math:`b = \mathrm{Im}(x)`.

.. note::
    * **Theorem**: :math:`\mathbb{C}` is a field with additive identity :math:`(0, 0)` and multiplicative identity :math:`(1, 0)`.

.. note::
    * **Proposition**: For :math:`a, b \in \mathbb{R}`:

        #. :math:`(a, 0) + (b, 0) = (a + b, 0)`
        #. :math:`(a, 0) \cdot (b, 0) = (ab, 0)`

.. remark::
    Since complex numbers in the form :math:`(a, 0)` have the same arithmetic properties as :math:`a`, we identify :math:`(a, 0)` with :math:`a`. Hence :math:`\mathbb{R}` is a subfield of :math:`\mathbb{C}`.

.. note::
    * Define :math:`i = (0, 1)`.
    * **Proposition**: :math:`i^{2} = -1`.

********************************************************************************
Euclidean Space
********************************************************************************
