################################################################################
Sets and Functions
################################################################################

********************************************************************************
Finite, Countable, and Uncountable Sets
********************************************************************************

Preliminary Definitions Related to Functions and Cardinality
================================================================================

.. note::
    * **Function**: For non-empty sets :math:`A` and :math:`B`, a rule :math:`f:A\to B` assigning each :math:`x\in A` to a value in :math:`B`.
    * **Domain**: The set :math:`A` is the domain of :math:`f`.
    * **Values**: The associated element of :math:`B` is :math:`f(x)`.
    * **Co-domain**: The set :math:`B` is the co-domain of :math:`f`.
    * **Range**: :math:`f(A):=\{f(x)\mid x\in A\}`.
    * **Onto Mapping / Surjection**: :math:`f` is onto if :math:`f(A)=B`.
    * **Image**: For :math:`E\subseteq A`, :math:`f(E):=\{f(x)\mid x\in E\}`.
    * **Pre-image**: For :math:`E\subseteq B`,

        .. math:: f^{-1}(E):=\{x\in A\mid f(x)\in E\}.

    * **One-to-one Mapping / Injection**: For every :math:`y\in f(A)`, the set :math:`f^{-1}(\{y\})` has exactly one element.
    * **Bijection**: If there is a one-to-one mapping of :math:`A` onto :math:`B`, write :math:`A\sim B`.

.. remark::
    If :math:`A\sim B`, then :math:`A` and :math:`B` share the same cardinal number.

Finite, Countable, and Uncountable Sets
================================================================================

.. note::
    * :math:`J_n := \{1,\dots,n\}` and :math:`J := \{1,2,3,\dots\}`.
    * **Finite Set**: :math:`A` is finite if :math:`A=\varnothing` or :math:`A\sim J_n` for some :math:`n`.
    * **Infinite Set**: A set that is not finite.
    * **Countable Set**: :math:`A\sim J`.
    * **Uncountable Set**: Neither finite nor countable.
    * **Sequence**: A function :math:`f:J\to X`, written as :math:`\{x_n\}`.

Properties
================================================================================

.. note::
    * **Theorem**: Every infinite subset of a countable set is countable.
    * **Theorem**: A countable union of countable sets is countable.
    * **Theorem**: The set of all sequences whose elements come from a finite set is uncountable.

.. tip::
    When comparing cardinalities, it is often enough to build an explicit injection or bijection with :math:`J` or a subset of :math:`J`.
