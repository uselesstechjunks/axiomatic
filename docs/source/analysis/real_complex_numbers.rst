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
        #. A set of 3 points arranged in a circle has a cyclic symmetry (rotate the circle by :math:`1/3` of a revolution, mapping the points accordingly).
        #. The set of all permutations of a finite set defines symmetries, where any element can map to any other element.
        #. :math:`\forall n \in \mathbb{Z}` define a symmetry :math:`x \in \mathbb{Z} \mapsto n + x \in \mathbb{Z}` (sliding the number line).
        #. :math:`\forall n \in \mathbb{Q}` define a symmetry :math:`x \in \mathbb{Q} \mapsto n \cdot x \in \mathbb{Q}` (stretching the number line).
        #. For a finite-dimensional vector space over :math:`\mathbb{R}`, :math:`\mathbb{R}^n`, the set of non-singular :math:`n \times n` matrices define symmetries since it maps any vector :math:`u \in \mathbb{R}^n \mapsto Au \in \mathbb{R}^n` (Generalised Linear Group of order :math:`n` or :math:`\mathrm{GL}_n(\mathbb{R})`).

.. remark::
    The idea of groups comes from symmetries, where an operator is defined to denote the composition of symmetries. The associativity follows from the fact that function composition is associative. Also, since symmetries are bijections, we have inverses.

.. note::
    * **Group**: A group is a set :math:`G` with a binary operation :math:`(+)` that satisfies:

        #. :math:`\forall x,y \in G,\ (x+y) \in G`  [Closure]
        #. :math:`\forall x,y,z \in G,\ ((x+y)+z) = (x+(y+z))`  [Associativity]
        #. :math:`\exists 0 \in G` such that :math:`\forall x \in G,\ (x+0)=(0+x)=x`  [Identity]
        #. :math:`\forall x \in G,\ \exists (-x) \in G` such that :math:`(x+(-x))=(( -x)+x)=0`  [Inverse]

.. remark::
    Groups are fully specified using the notation :math:`(G,+,0)`.

.. note::
    * **Proposition**: For a group :math:`(G,+,0)` and :math:`\forall x,y,z \in G`:

        #. :math:`(x+y=x+z) \Rightarrow y=z`  [Cancellation Law]
        #. :math:`(x+y)=x \Rightarrow y=0`  [Uniqueness of Identity]
        #. :math:`(x+y)=0 \Rightarrow y=-x`  [Uniqueness of Inverse]
        #. :math:`-(-x)=x`  [Repeated Inverse]

.. remark::
    If :math:`(\cdot)` denotes the group operation, the identity is written as :math:`1` and the inverse of :math:`x` as :math:`x^{-1}`. The group is written as :math:`(G,\cdot,1)`.

.. note::
    * **Commutative Group**: A commutative (Abelian) group satisfies the additional axiom:

        .. math:: \forall x,y \in G,\ x+y=y+x.

********************************************************************************
Fields
********************************************************************************

.. note::
    * **Field**: A field is a set :math:`F` with two binary operations :math:`(+)` and :math:`(\cdot)` such that:

        #. :math:`(F,+,0)` is a commutative group
        #. :math:`(F\\setminus\\{0\\},\cdot,1)` is a commutative group
        #. :math:`\forall x,y,z \in F,\ x\cdot(y+z)=(x\cdot y)+(x\cdot z)`

.. remark::
    Fields are fully specified as :math:`(F,+,0,\cdot,1)`.

.. note::
    * **Proposition**: For a field :math:`(F,+,0,\cdot,1)` and :math:`\forall x,y \in F`:

        #. :math:`x\cdot 0 = 0\cdot x = 0`
        #. :math:`(x \neq 0)\wedge(y \neq 0) \Rightarrow x\cdot y \neq 0`
        #. :math:`(-x)\cdot y = x\cdot(-y) = -(x\cdot y)`
        #. :math:`(-x)\cdot(-y)=x\cdot y`

********************************************************************************
Ordered Sets
********************************************************************************

.. note::
    * **Order**: For a set :math:`S`, an order :math:`(<)` satisfies:

        #. For all :math:`x,y \in S`, exactly one of :math:`x<y`, :math:`x=y`, :math:`y<x` holds
        #. :math:`(x<y)\wedge(y<z) \Rightarrow x<z`

.. note::
    * **Partial Order**: A partial order :math:`(\leq)` satisfies:

        #. :math:`x\leq x`  [Reflexive]
        #. :math:`(x\leq y)\wedge(y\leq x)\Rightarrow x=y`  [Anti-symmetric]
        #. :math:`(x\leq y)\wedge(y\leq z)\Rightarrow x\leq z`  [Transitive]

      Additionally, a total order requires connexity.

.. note::
    * **Ordered Set**: An ordered set is a set on which an order is defined.
    * **Upper Bound**: For :math:`E\subset S`, :math:`\beta\in S` is an upper bound if :math:`\forall x\in E,\ x\leq \beta`.
    * **Least Upper Bound**: If :math:`\alpha` is an upper bound of :math:`E` and no smaller element is an upper bound, then :math:`\alpha=\sup E`.
    * **Least Upper Bound Property**: An ordered set has the least upper bound property if every nonempty bounded-above subset has a supremum.

.. note::
    * **Theorem**: If :math:`S` has the least upper bound property and :math:`B\subset S` is nonempty and bounded below, then :math:`\inf B` exists in :math:`S`.

********************************************************************************
Ordered Field
********************************************************************************

.. note::
    * **Ordered Field**: An ordered field is a field :math:`F` such that:

        #. :math:`y<z \Rightarrow x+y < x+z`
        #. :math:`(x>0)\wedge(y>0) \Rightarrow x\cdot y>0`

********************************************************************************
The Real Field
********************************************************************************

.. note::
    * **Real Field**: There exists an ordered field :math:`\mathbb{R}` with the least upper bound property such that :math:`\mathbb{Q}\subset\mathbb{R}` is a subfield.

.. note::
    * **Theorem**:

        #. :math:`\forall x,y\in\mathbb{R},\ x>0 \Rightarrow \exists n\in\mathbb{Z}^+` such that :math:`nx>y`
        #. :math:`\forall x<y` in :math:`\mathbb{R},\ \exists p\in\mathbb{Q}` such that :math:`x<p<y`

.. note::
    * **Theorem**: For :math:`x\in\mathbb{R}^+` and :math:`n\in\mathbb{Z}^+`, there exists a unique :math:`y\in\mathbb{R}^+` such that :math:`y^n=x`.

.. note::
    * **Corollary**: :math:`(ab)^{1/n}=a^{1/n}b^{1/n}` for :math:`a,b>0`.

.. note::
    * **Decimal Expansion**: For :math:`x\in\mathbb{R}^+`, let

        .. math:: E=\left\{n_0+\frac{n_1}{10}+\cdots+\frac{n_k}{10^k}\right\}.

      Then :math:`x=\sup E`.

********************************************************************************
Extended Real Number System
********************************************************************************

.. note::
    * The extended real number system is :math:`\mathbb{R}\cup\{-\infty,+\infty\}`.

.. remark::
    Every nonempty set has a supremum and infimum in the extended reals.

********************************************************************************
The Complex Field
********************************************************************************

.. note::
    * **Complex Numbers**: Complex numbers are ordered pairs :math:`(a,b)\in\mathbb{R}^2` with

        .. math:: (a,b)+(c,d)=(a+c,b+d),\quad (a,b)\cdot(c,d)=(ac-bd,ad+bc).

.. note::
    * **Theorem**: :math:`\mathbb{C}` is a field with identities :math:`(0,0)` and :math:`(1,0)`.

.. note::
    * :math:`i=(0,1)`.

.. note::
    * **Proposition**: :math:`i^2=-1`.

********************************************************************************
Euclidean Space
********************************************************************************
