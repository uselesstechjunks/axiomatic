################################################################################
Sets and Functions
################################################################################

********************************************************************************
Finite, Countable, and Uncountable Sets
********************************************************************************

Preliminary Definitions Related to Functions and Cardinality
================================================================================

.. note::
    * **Function**: For two non-empty sets :math:`A` and :math:`B`, if each element :math:`x` of :math:`A` is associated with an element of :math:`B`, then this association is a function (or a mapping) from :math:`A` to :math:`B`, written as :math:`f : A \to B`.

.. tip::
    Imagine packing when relocating, putting items inside boxes before moving all those boxes inside your truck. A function is a rule which says which item goes inside which box. You can put two items in the same box but cannot put the same item into two different boxes. Your truck may have some leftover space when you're done packing.

.. note::
    The following definitions are for a function :math:`f : A \to B`.
    * **Domain**: The set :math:`A` is the domain of :math:`f`.
    * **Values**: The element in :math:`B` associated with :math:`x \in A` is the value of :math:`x`, written as :math:`f(x)`.
    * **Co-Domain**: The set :math:`B` is the co-domain of :math:`f`.
    * **Range**: The set of all values,

        .. math:: f(A) := \{ f(x) \mid x \in A \},

      is the range of :math:`f`.

.. note::
    * **Remark**: :math:`f(A) \subseteq B`.
    * **Onto Mapping/Surjection**: If :math:`f(A) = B`, then :math:`f` is a mapping of :math:`A` onto :math:`B` (instead of into) or a surjection.
    * **Image**: For :math:`E \subseteq A`,

        .. math:: f(E) := \{ f(x) \mid x \in E \}

      is the image of :math:`E` under :math:`f`.
    * **Pre-Image**: For :math:`E \subseteq B`,

        .. math:: f^{-1}(E) := \{ x \mid f(x) \in E \}

      is the pre-image of :math:`E` under :math:`f`.
    * **1-1 Mapping/Injection**: If :math:`\forall y \in f(A)`, the pre-image of :math:`\{y\}`,

        .. math:: f^{-1}(\{y\}) := \{ x \mid f(x) = y \},

      consists of just one element (a singleton), then :math:`f` is a 1-1 mapping or injection of :math:`A` into :math:`B`.
    * **1-1 Correspondence/Bijection**: If there exists a 1-1 mapping of :math:`A` onto :math:`B`, then :math:`A` and :math:`B` are in 1-1 correspondence and :math:`f` is a bijection. :math:`A` and :math:`B` are called equivalent and written as :math:`A \sim B`.

.. note::
    * **Remark**: If :math:`A \sim B`, then :math:`A` and :math:`B` have the same cardinal number.
    * **Remark**: The relation :math:`A \sim B` has the following properties:

        * :math:`A \sim A`  [Reflexive]
        * :math:`A \sim B \Rightarrow B \sim A`  [Symmetric]
        * :math:`A \sim B \wedge A \sim C \Rightarrow A \sim C`  [Transitive]

Finite, Countable, Uncountable Sets and Sequences
================================================================================

.. note::
    From now on, for some positive integer :math:`n`, let

    .. math:: J_n := \{1, \cdots, n\} \quad \text{and} \quad J := \{1, \cdots\} \ \text{(set of all positive integers)}.

    * **Finite Set**: :math:`A` is finite iff (a) :math:`A = \varnothing` or (b) :math:`A \sim J_n` for some :math:`n`.
    * **Infinite Set**: If :math:`A` is not finite, it is infinite.
    * **Countable Set**: If :math:`A \sim J`, then :math:`A` is countable.
    * **Remark**: Countable sets are also called enumerable or denumerable.
    * **Uncountable Set**: If :math:`A` is neither finite nor countable, it is uncountable.
    * **At-most Countable Set**: If :math:`A` is either finite or countable, it is at-most countable.
    * **Remark**: :math:`\mathbb{Z} \sim J`.
    * **Remark**: A set :math:`A` is infinite if :math:`A` is equivalent to one of its proper subsets.
    * **Sequence**: A function :math:`f : J \to X` is a sequence. If :math:`f(n) = x_n`, the sequence is written as :math:`\{x_n\}`.
    * **Insight**: A sequence is a never-ending labelling of items in a set in an orderly fashion.
    * **Remark**: If :math:`\forall n \in J`, :math:`x_n \in A`, then :math:`\{x_n\}` is a sequence in :math:`A`.
    * **Remark**: Every countable set can be arranged in a sequence.

Properties involving Finite, Countable, and Uncountable Sets
================================================================================

.. note::
    * **Theorem**: Every infinite subset of a countable set is countable.
    * **Remark**: Countable sets represent the smallest kind of infinity.
    * **Theorem**: Countable union of countable sets are countable. Let :math:`\{E_n\}` be a sequence of countable sets. Then

        .. math:: \bigcup_{n=1}^{\infty} E_n

      is countable.
    * **Theorem**: Set of tuples whose elements are taken from a countable set is countable. For :math:`A`, a countable set, let

        .. math:: B_n := \{(a_1, \cdots, a_n)\}

      where every :math:`a_k \in A`, not necessarily distinct. Then :math:`B_n` is countable.
    * **Remark**: :math:`\mathbb{Q}` is countable.
    * **Theorem**: Set of sequences whose elements are taken from a finite set is uncountable. For :math:`A`, a finite set, let

        .. math:: B := \bigl\{ \{x_n\} \mid \{x_n\} \text{ is a sequence in } A \bigr\}

      (i.e. :math:`B` is the set of all sequences whose elements are chosen, with repetition, from :math:`A`). :math:`B` is uncountable.
