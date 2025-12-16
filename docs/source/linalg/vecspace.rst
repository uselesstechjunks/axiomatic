################################################################################
Vector Space and Geometry
################################################################################

********************************************************************************
Vector Space
********************************************************************************
Let :math:`\mathcal{F}` be a scalar **field** (such as :math:`\mathbb{R}` or :math:`\mathbb{C}`).

.. attention::
	* Field refers to the algebraic definition with properly defined addition and multiplication operators on them. 
	* Not to be confused with **scalar fields** which represents functionals that maps vectors into scalers.

.. admonition:: [Definition] Vector Space

	:math:`V_\mathcal{F}` is a vector space over :math:`\mathcal{F}` with :math:`0\in \mathcal{F}` **iff**:

		* :math:`\forall a\in \mathcal{F},\mathbf{u}\in V_\mathcal{F}\implies a\cdot\mathbf{u}\in V_\mathcal{F}`
		* :math:`\mathbf{u},\mathbf{v}\in V_\mathcal{F}\implies \mathbf{u}+\mathbf{v}\in V_\mathcal{F}`
	
	with the following properties:

		* [Commutative Addition]: :math:`\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}`
		* [Identity Element]: :math:`\exists\mathbf{0}\in V_\mathcal{F}` such that

			* :math:`0\cdot\mathbf{u}=\mathbf{0}`
			* :math:`\mathbf{u}+\mathbf{0}=\mathbf{0}+\mathbf{u}=\mathbf{u}`
		* [Inverse Element]: :math:`\forall\mathbf{u}\in V_\mathcal{F},\exists\mathbf{v}\in V_\mathcal{F}` (represented as :math:`-\mathbf{u}`) such that

			:math:`\mathbf{u}+\mathbf{v}=\mathbf{0}`

.. attention::
	Vector spaces are Abelian groups w.r.t :math:`+` but the addition of scalar multiplication provides an even richer structure.

.. tip::	
	* Elements of vector space are called vectors.
	* We often omit the underlying scalar field :math:`\mathcal{F}` and write the vector space as :math:`V`.
	* Example of finite dimensional vectors: Euclidean vectors :math:`\mathbb{R}^n` where the scalar field is :math:`\mathbb{R}` or complex vectors :math:`\mathbb{C}^n` over the scalar field :math:`\mathbb{C}`.

Euclidean Vector Space
================================================================================
These defintions and theorems are based on Graybill.

Vector Space
-------------------------------------------------------------------------------
.. admonition:: [Definition] n-component Vector

	Let :math:`n` be a positive integer and let :math:`a_1,\cdots,a_n` be elements from :math:`\mathcal{F}`. The ordered :math:`n`-tuple :math:`\mathbf{a}=(a_1,\cdots,a_n)^T` is defined as n-component (or :math:`n\times 1` vector)

.. seealso::
	Vector spaces with :math:`n\times 1` vectors are denoted here by :math:`V_n`.

.. admonition:: Theorem

	Let :math:`R_n` be the set of all :math:`n\times 1` vectors for a fixed positive integer :math:`n`. Then :math:`R_n` is a vector space.

Vector Subspace
-------------------------------------------------------------------------------
.. admonition:: [Definition] Vector Subspace

	Let :math:`S_n` be the subset of vectors in the vector space :math:`V_n`. If the set :math:`S_n` itself is a vector space, then :math:`S_n` is called a vector subspace of :math:`V_n`.

.. admonition:: Theorem

	If :math:`S_n` is a subset of the vector space :math:`V_n` such that, for every two vectors, :math:`\mathbf{s}_1` and :math:`\mathbf{s}_2` in :math:`S_n`, :math:`a_1\mathbf{s}_1+a_2\mathbf{s}_2` is in :math:`S_n` for all real numbers :math:`a_1` and :math:`a_2`, then :math:`S_n` is a vector subspace of :math:`V_n`.

.. admonition:: Theorem

	The set :math:`\{\mathbf{0}\}` where :math:`\mathbf{0}` is the :math:`n\times 1` null-vector, is a subspace of every vector space :math:`V_n`. Every vector space :math:`V_n` is a subspace of itself.

Linear Dependence and Independence
-------------------------------------------------------------------------------
.. admonition:: [Definition] Linear Dependence and Independence

	Let :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` be a set of :math:`m` vectors each with :math:`n` components, so that :math:`\mathbf{v}_i\in R_n;i=1,\cdots,m`. This set is defined to be linearly dependent if and only if there exists a set of scalars :math:`\{c_1,\cdots,c_m\}`, at least one of which is not equal to zero, such that

	.. math:: \sum_{i=1}^m c_i\mathbf{v_i}=\mathbf{0}

	If the only set of scalars that satisfies the above is :math:`\{0,\cdots,0\}`, then the set of vectors is called linearly independent.

.. admonition:: Theorem

	If the vector :math:`\mathbf{0}` is included in a set of vectors, the set is linearly dependent.

.. admonition:: Theorem

	If :math:`m > 1` vectors are linearly dependent, it's always possible to express at least one of them as a linear combination of the others.

.. admonition:: Theorem

	In the set of :math:`m` vectors :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}`, if there are :math:`s` vectors, :math:`s\le m`, that are linearly dependent, then the entire set of vectors is linearly dependent.

.. admonition:: Theorem

	If the set of :math:`m` vectors :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` is a linearly independent set, while the set of :math:`m+1` vectors :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_{m+1}\}` is a linearly dependent set, then :math:`\mathbf{v}_{m+1}` can be expressed as a linear combination of :math:`\mathbf{v}_1,\cdots,\mathbf{v}_m`.

.. admonition:: Theorem

	A necessary and sufficient condition for thet set of :math:`n\times 1` vectors :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` to be linearly dependent set is that the rank of the matrix formed by the vectors (as columns) is less than the number of vectors :math:`m`; that is :math:`r < m`.

.. admonition:: Theorem

	If the rank of the matrix of a set of :math:`n\times 1` vectors :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` is :math:`r`, then :math:`r` must be less than or equal to :math:`m`, and if :math:`r > 0`, theree exists exactly :math:`r` of those vectors that are linearly independent, while each of the other :math:`m-r` (if :math:`m-r > 0`) vectors expressible as a linear combination of these :math:`r` vectors.

.. admonition:: Theorem

	The set of :math:`n\times 1` vectors :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` is always linearly independent if :math:`m > n`.

Basis of a Vector Space
-------------------------------------------------------------------------------
.. admonition:: Theorem

	Let :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` be a set of vectors in :math:`V_n` and let :math:`V` be the set of vectors defined by

	.. math:: V=\left\{\mathbf{v}:\mathbf{v}=\sum_{i=1}^m c_i\mathbf{v}_i; c_i\in\mathbb{R} \right\};

	then :math:`V` is a subspace of :math:`V_n`.

.. admonition:: [Definition] Generating (or Spanning) Vectors

	Let :math:`V_n` be a vector space. If each vector in :math:`V_n` can be obtained from a linear combination of the vectors in the set :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}`, then the set of vectors :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` is said to generate (or span) :math:`V_n`.

.. admonition:: [Definition] Basis

	Let :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` be a set of linearly independent set of vectors that spans :math:`V_n`. Then this set is called a basis of :math:`V_n`. For the special vector space :math:`\{\mathbf{0}\}`, we shall say that :math:`\mathbf{0}` is the basis (even though it's not linearly independent). 

.. admonition:: Theorem

	If :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}`, :math:`\{\mathbf{u}_1,\cdots,\mathbf{u}_q\}` are two bases for :math:`V_n`, then :math:`m=q`.

.. admonition:: [Definition] Dimensions

	Let :math:`V_n` be any vector space except :math:`\{\mathbf{0}\}`. Let the number of vectors in the basis of :math:`V_n` be :math:`m`. Then :math:`m` is defined to be the dimension of :math:`V_n`. The dimension of :math:`\{\mathbf{0}\}` is defined to be 0.

.. admonition:: Theorem

	Let :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` be a basis for the vector space :math:`V_n` (\neq :math:`\{\mathbf{0}\}`). Let :math:`\mathbf{v}` be any vector in :math:`V_n`. There is oen and only one ordered set of scalars :math:`\{c_1,\cdots,c_m\}` such that

	.. math:: \mathbf{v}=\sum_{i=1}^m c_i\mathbf{v}_i

	In other words, :math:`\mathbf{v}` is a unique linear combination of a given basis.

.. admonition:: Theorem

	If :math:`r` is the rank of the matrix of vectors :math:`\mathbf{v}_1,\cdots,\mathbf{v}_m` that span the vector space :math:`V_n`, then there are exactly :math:`r` independent vectors in that set  and every vector in :math:`V_n` can be expressed uniquely as a linear combination of these :math:`r` vectors.

.. admonition:: Theorem

	If the vector space :math:`V_n` is spanned by a set of :math:`m` vectors, and if the matrix of those vectors has a rank :math:`r`, then any set of :math:`r+1` vectors in :math:`V_n` is linearly dependent.

.. admonition:: Theorem

	Let :math:`\mathbf{V}=\begin{bmatrix}\mathbf{v}_1&\cdots&\mathbf{v}_m\end{bmatrix}` be a matrix containing a set of vectors that is a basis for :math:`V_n`, and let :math:`\mathbf{U}=\begin{bmatrix}\mathbf{u}_1&\cdots&\mathbf{u}_q\end{bmatrix}` be a matrix that is any set of vectors in :math:`V_n`. The set of vectors in :math:`\mathbf{U}` is a basis set for :math:`V_n` if and only if :math:`m=q` and there exists a non-singular :math:`m\times m` matrix :math:`\mathbf{A}` such that :math:`\mathbf{U}=\mathbf{V}\mathbf{A}`.

.. admonition:: Theorem

	Let :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}`, :math:`m > 1`, be a basis for the vector space :math:`V_n` and let :math:`\mathbf{v}` be any vector in :math:`V_n` such that :math:`\mathbf{v}=\sum_{i=1}^m c_i\mathbf{v}_i`. If :math:`c_t\neq 0` for some :math:`t`, then the set :math:`\{\mathbf{v}_1,\cdots\mathbf{v}_{t-1},\mathbf{v},\mathbf{v}_{t+1},\cdots\mathbf{v}_m\}` is a basis for :math:`V_n`. However, if :math:`c_t=0`, then the set :math:`\{\mathbf{v}_1,\cdots\mathbf{v}_{t-1},\mathbf{v},\mathbf{v}_{t+1},\cdots\mathbf{v}_m\}` is a linearly dependent set and hence not a basis for :math:`V_n`.

.. admonition:: Theorem

	Let :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_q\}` be a linearly independent vectors of :math:`V_n`. Then this set is a subset of a basis for :math:`V_n`.

Inner Product and Orthogonality of Vectors
-------------------------------------------------------------------------------
.. admonition:: [Definition] Inner Product

	Let :math:`\mathbf{x}` and :math:`\mathbf{y}` be two vectors in :math:`V_n`. The inner product of :math:`\mathbf{x}` and :math:`\mathbf{y}`, :math:`\mathbf{x}\cdot\mathbf{y}` is defined to be the scalar :math:`\sum_{i=1}^nx_iy_i`. It is the scalar that is the element in the :math:`1\times 1` matrix :math:`\mathbf{x}^T\mathbf{y}`.

.. admonition:: [Definition] Orthogonal Vectors

	Let :math:`\mathbf{x}` and :math:`\mathbf{y}` be two vectors in :math:`V_n`. :math:`\mathbf{x}` and :math:`\mathbf{y}` are defined to be orthogonal if and only if the inner product is 0.

.. tip::
	:math:`\mathbf{0}` vector is orthogonal to every vector in :math:`V_n`.

.. admonition:: [Definition] Normal Vectors

	A vector :math:`\mathbf{x}` in :math:`V_n` is defined to be a normal vector if and only if the inner product of :math:`\mathbf{x}` with itself is equal to :math:`+1`. 

.. admonition:: [Definition] Orthogonal and Orthonormal Basis

	If :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` is a basis for :math:`V_n` such that :math:`\mathbf{v}_i^T\mathbf{v}_j` for all :math:`i\neq j=1,\cdots m`, then the basis is defined to be orthogonal basis for :math:`V_n`. If in addition, :math:`\mathbf{v}_i^T\mathbf{v}_i=1` for all :math:`i=1,\cdots m`, the basis is defined to be orthonormal basis.

.. admonition:: Theorem

	Every vector space has an orthogonal basis.

.. admonition:: Theorem

	Every vector space except :math:`\{\mathbf{0}\}` has an orthonormal basis.

.. admonition:: Theorem

	Let :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_m\}` be a set of vectors in :math:`V_n` such that each and every distinct pair of vectors is orthogonal; that is :math:`\mathbf{v}_i^T\mathbf{v}_j=0` for all :math:`i\neq j`. If none of the vectors is the zero vector, then the set of vectors is a linearly independent set.

.. admonition:: Theorem

	Any set of :math:`q` nonzero pairwise orthogonal vectors in :math:`V_n` is a subset of a basis for :math:`V_n`.

.. admonition:: Theorem

	Let :math:`\{\mathbf{v}_1,\cdots,\mathbf{v}_q\}` be the set of basis for the vector space :math:`V_n (\neq \{\mathbf{0}\})`. Then the set of :math:`q` vectors :math:`\{\mathbf{z}_1,\cdots,\mathbf{z}_q\}` is also a basis vector for :math:`V_n` and they are an orthonormal set where they are defined as

	.. math:: \begin{matrix}\mathbf{y}_1=\mathbf{v}_1;&\mathbf{z}_1=\frac{\mathbf{y}_1}{\sqrt{\mathbf{y}_1^T\mathbf{y}_1}} \\ \mathbf{y}_2=\mathbf{v}_2-\frac{\mathbf{y}_1^T\mathbf{v}_2}{\mathbf{y}_1^T\mathbf{y}_1}\mathbf{y}_1;&\mathbf{z}_2=\frac{\mathbf{y}_2}{\sqrt{\mathbf{y}_2^T\mathbf{y}_2}} \\ \vdots&\vdots\\ \mathbf{y}_q=\mathbf{v}_q-\frac{\mathbf{y}_1^T\mathbf{v}_q}{\mathbf{y}_1^T\mathbf{y}_1}\mathbf{y}_1-\frac{\mathbf{y}_2^T\mathbf{v}_q}{\mathbf{y}_2^T\mathbf{y}_2}\mathbf{y}_2-\cdots-\frac{\mathbf{y}_{q-1}^T\mathbf{v}_q}{\mathbf{y}_{q-1}^T\mathbf{y}_{q-1}}\mathbf{y}_{q-1};&\mathbf{z}_q=\frac{\mathbf{y}_q}{\sqrt{\mathbf{y}_q^T\mathbf{y}_q}} \end{matrix}

********************************************************************************
Affine Sets in Euclidean Vector Space
********************************************************************************

Line
================================================================================

Plane
================================================================================

********************************************************************************
Orthogonal Projections
********************************************************************************
