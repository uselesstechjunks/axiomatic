################################################################################
Linear Transform
################################################################################
********************************************************************************
Linear Transform in Vector Space
********************************************************************************
.. note::
	* Let :math:`U` and :math:`W` be two vector spaces over the same scalar field :math:`\mathcal{F}`.
	* A linear transform is a function :math:`T:U\mapsto W` if 

		* :math:`\forall\mathbf{u},\mathbf{v}\in U, T(\mathbf{u}+\mathbf{v})=T(\mathbf{u})+T(\mathbf{v})`
		* :math:`\forall c\in\mathcal{F},\forall\mathbf{u}\in U, T(c\cdot\mathbf{u})=c\cdot T(\mathbf{u})`
	* This means, if we want to add or scale vecetors, it doesn't matter whether we do it in the domain space before the mapping or in the range space after the mapping.

.. tip::
	A linear transform is one-to-one when it's onto.

Linear Operator
================================================================================
.. tip::
	* Linear transforms from :math:`U` to :math:`U` are called Linear Operators.
	* The set of all linear operators :math:`T:U\mapsto U` is represented as :math:`L(U)`.

Space of Linear Transforms
================================================================================
.. tip::
	The set of all linear transforms :math:`T:U\mapsto W` is represented as :math:`L(U,W)`.

As a Vector Space over Addition? Always.
--------------------------------------------------------------------------------
.. seealso::
	* Let's consider :math:`A,B\in L(U,W)`.
	* We can define a commutative addition in :math:`L(U,V)` with the same scalar multiplication of :math:`W`.

		* Let :math:`C=(a\cdot A+b\cdot B)` where for any :math:`a,b\in\mathcal{F}` we have

			.. math:: \forall\mathbf{u}\in U, C(\mathbf{u})=(a\cdot A+b\cdot B)(\mathbf{u})=a\cdot A(\mathbf{u})+b\cdot B(\mathbf{u})
		* We note that :math:`C\in L(U,W)`.
	* We also define an identity operator :math:`0_L\in L(U,W)` such that :math:`\forall \mathbf{u}, 0_L(\mathbf{u})=\mathbf{0}`.

		* We note that :math:`A+0_L=0_L+A=A`.
	* We can define a unique additive inverse :math:`-A:U\mapsto W`.

		.. math:: A(\mathbf{u})+-A(\mathbf{u})=-A(\mathbf{u})+A(\mathbf{u})=0_L(\mathbf{u})=\mathbf{0}

Composition of Linear Transforms
================================================================================
.. note::
	* We can define composite linear transforms in the usual way.
	* Let :math:`A:U\mapsto V` and :math:`B:V\mapsto W`.
	* Then :math:`(B\circ A)\in L(U,W)` where :math:`\forall\mathbf{u}\in U, (B\circ A)(\mathbf{u})=B(A(\mathbf{u}))`.

As a Vector Space over Composition? Not Guaranteed.
--------------------------------------------------------------------------------
.. seealso::
	* Let's consider :math:`A,B\in L(U)`.
	* We can consider :math:`\circ` as an "addition" in :math:`L(U,V)` with the same scalar multiplication of :math:`U`.

		* Let :math:`C=((b\cdot B)\circ (a\cdot A))\in L(U)` where for any :math:`a,b\in\mathcal{F}` we have

			.. math:: \forall\mathbf{u}\in U, C(\mathbf{u})=((b\cdot B)\circ (a\cdot A))(\mathbf{u})=ab\cdot B(A(\mathbf{u}))
	* We define the identity operator :math:`I:U\mapsto U` such that :math:`\forall \mathbf{u}, I(\mathbf{u})=\mathbf{u}`.

		We note that :math:`A\circ I = I\circ A = A`
	* If the transform is **onto**, then we can define a unique composition inverse :math:`A^{-1}:U\mapsto U` such that

		.. math:: (A\circ A^{-1})(\mathbf{u}) = (A^{-1}\circ A)(\mathbf{u}) = I(\mathbf{u}) = \mathbf{u}

.. warning::
	* HOWEVER, The composition operator is not always **commutative**.
	
		* It is generally NOT true that :math:`(A\circ B)(\mathbf{u})=(B\circ A)(\mathbf{u})`.
	* Example where it IS commutative:

		* Let :math:`\mathbf{A}` and :math:`\mathbf{B}` be matrices with the same eigenvectors and possibly different eigenvalues.
		* In this case, the composition is commutative.
		* We note that this is a sufficient but not a necessary condition.

.. attention::
	* The composition operator, therefore, is better thought of as a **multiplication**.
	* Together with the addition and multiplication, the space of linear operators follows the structure of a **ring**.

Examples
================================================================================
Scalar Multiplication as a Linear Transform
--------------------------------------------------------------------------------
.. tip::
	* For every scalar :math:`\alpha\in\mathbb{R}`, we can define a unique linear operator in :math:`L(\mathbb{R})` with its already defined multiplication operator as :math:`\alpha:\mathbb{R}\mapsto\mathbb{R}` where :math:`\forall x\in\mathbb{R}, \alpha(x)=\alpha\cdot x`.
	* We note that

		* :math:`\forall u,v\in \mathbb{R}, \alpha(u+v)=\alpha(u)+\alpha(v)`
		* :math:`\forall c\in\mathbb{R},\forall u\in \mathbb{R}, \alpha(c\cdot u)=c\cdot\alpha(u)`

Matrix-Vector Multiplication as Linear Transform
--------------------------------------------------------------------------------
.. tip::
	* The matrix :math:`\mathbf{A}` is a linear transform which maps :math:`\mathbb{C}^n` dimensional vectors to :math:`\mathbb{C}^m` dimensional vectors.

		.. math:: \mathbf{A}:\mathbb{C}^n\mapsto\mathbb{C}^m
	* The range of this transform is the **column space** of this transform

		.. math:: C(\mathbf{A})=\{\mathbf{A}\mathbf{x}\mathop{|}\forall \mathbf{x}\in\mathbb{C}^n\}
	* The transposed matrix :math:`\mathbf{A}^\top` does the mapping the other way around (but it's not necessarily the inverse transform)

		.. math:: \mathbf{A}^\top:\mathbb{C}^m\mapsto\mathbb{C}^n
	* The range of the transpose transform is the **row space** of :math:`\mathbf{A}`

		.. math:: C(\mathbf{A}^\top)=\{\mathbf{A}^\top\mathbf{y}\mathop{|}\forall \mathbf{y}\in\mathbb{C}^m\}

Differentiation as a Linear Transform
--------------------------------------------------------------------------------
.. tip::
	* Let :math:`X` and :math:`Y` be two vector spaces over :math:`\mathbb{R}`.
	* Let :math:`\mathcal{F}=\{f\mathop{|} f:X\mapsto Y\}` be the set of all function from :math:`X` into :math:`Y`.
	* Let :math:`\mathcal{D}=\{g\mathop{|} g:X\mapsto Y\}` be the set of all **differentiable functions**.
	* The differentiation operator :math:`D=\frac{\mathop{d}}{\mathop{dx}}(\cdot)` on its own defines a function :math:`D:\mathcal{G}\mapsto\mathcal{F}`.

		.. math:: D(g\in\mathcal{G})=g'\in\mathcal{F}

		* Here :math:`g'(x)=\frac{\mathop{d}}{\mathop{dx}}(g)(x)`.
	* :math:`D` applied on some specific function :math:`g` (ready to be evaluated on any :math:`x`) defines a linear transform :math:`D(g)\in\mathcal{F}:X\mapsto Y` since

		* :math:`\forall g_1,g_2\in \mathcal{G}, D(g_1+g_2)=D(g_1)+D(g_2)`
		* :math:`\forall c\in \mathbb{R},\forall g\in \mathcal{G}, D(c\cdot g)=c\cdot D(g)`

Integration as a Linear Transform
--------------------------------------------------------------------------------
.. tip::
	* Let :math:`X` and :math:`Y` be two vector spaces over :math:`\mathbb{R}`.
	* Let :math:`\mathcal{F}=\{f\mathop{|} f:X\mapsto Y\}` be the set of all function from :math:`X` into :math:`Y`.
	* Let :math:`\mathcal{I}=\{g\mathop{|} g:X\mapsto Y\}` be the set of all **integrable functions**.
	* The integration operator :math:`I=\int(\cdot)\mathop{dx}` on its own defines a function :math:`I:\mathcal{I}\mapsto\mathcal{F}`.

		.. math:: I(g\in\mathcal{I})=G\in\mathcal{F}

		* Here :math:`G(x)=\int g(x)\mathop{dx}`.
	* :math:`I` applied on some specific function :math:`g` (ready to be evaluated on any :math:`x`) defines a linear transform :math:`I(g)\in\mathcal{F}:X\mapsto Y` since

		* :math:`\forall g_1,g_2\in \mathcal{I}, I(g_1+g_2)=I(g_1)+I(g_2)`
		* :math:`\forall c\in \mathbb{R},\forall g\in \mathcal{I}, I(c\cdot g)=c\cdot I(g)`

********************************************************************************
Matrix-vector multiplication
********************************************************************************
Let :math:`\mathbf{A}` be a :math:`m\times n` matrix. 

* Column view: :math:`\mathbf{a}_k\in\mathbb{R}^m` are column vectors

	.. math:: \mathbf{A}=\begin{bmatrix} | & \cdots & |\\ \mathbf{a}_1 & \cdots & \mathbf{a}_n\\ | & \cdots & |\\ \end{bmatrix}

* Row view: :math:`(\mathbf{a}^*_k)^\top\in\mathbb{R}^n` are row vectors

	.. math:: \mathbf{A}=\begin{bmatrix}-&\mathbf{a}^*_1&-\\&\vdots&\\-&\mathbf{a}^*_m&-\end{bmatrix}

Let :math:`\mathbf{x}\in\mathbb{R}^n` be a column vector which can also be thought of as a :math:`n\times 1` matrix

	.. math:: \mathbf{x}=(x_1,\cdots,x_n)^\top=\begin{bmatrix} x_1\\ \vdots\\ x_n \end{bmatrix}

.. note::
	* Column view: The multiplication :math:`\mathbf{A}\mathbf{x}` is a combination of the column vectors of :math:`\mathbf{A}`, where each vector :math:`\mathbf{a}_k` is scaled as per :math:`x_k`.

		.. math:: \mathbf{A}\mathbf{x}=\begin{bmatrix} | & \cdots & |\\ \mathbf{a}_1 & \cdots & \mathbf{a}_n\\ | & \cdots & |\\ \end{bmatrix}\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}=x_1\begin{bmatrix}|\\ \mathbf{a}_1\\|\end{bmatrix}+\cdots+x_n\begin{bmatrix}|\\ \mathbf{a}_n\\|\end{bmatrix}

	* Row view: It can also be thought of the collection of inner products with each row vectors

		.. math:: \mathbf{A}\mathbf{x}=\begin{bmatrix}\langle(\mathbf{a}^*_1)^\top,\mathbf{x}\rangle\\\vdots\\\langle(\mathbf{a}^*_m)^\top,\mathbf{x}\rangle\end{bmatrix}

.. attention::
	The equation :math:`\mathbf{A}\mathbf{x}=\mathbf{b}` has a unique solution if :math:`\mathbf{b}\in C(\mathbf{A})`.

********************************************************************************
Matrix-matrix multiplication
********************************************************************************
Let :math:`\mathbf{A}` be the matrix as before and let :math:`\mathbf{B}` be a :math:`n\times p` matrix written as a collection of rows similar to a vector

	.. math:: \mathbf{B}=\begin{bmatrix}-&\mathbf{b}^*_1&-\\&\vdots&\\-&\mathbf{b}^*_n&-\end{bmatrix}

where :math:`\mathbf{b}^*_k\in\mathbb{R}^p` are the row vectors.

.. note::
	The multiplication :math:`\mathbf{A}\mathbf{B}` is the sum of outer products :math:`\mathbf{u}\mathbf{v}^\top=\mathbf{a}_k \mathbf{b}^*_k`

		.. math:: \mathbf{A}\mathbf{B}=\begin{bmatrix} | & \cdots & |\\ \mathbf{a}_1 & \cdots & \mathbf{a}_n\\ | & \cdots & |\\ \end{bmatrix}\begin{bmatrix}-&\mathbf{b}^*_1&-\\&\vdots&\\-&\mathbf{b}^*_n&-\end{bmatrix}=\begin{bmatrix}|\\ \mathbf{a}_1\\|\end{bmatrix}\begin{bmatrix}-&\mathbf{b}^*_1&-\end{bmatrix}+\cdots+\begin{bmatrix}|\\ \mathbf{a}_n\\|\end{bmatrix}\begin{bmatrix}-&\mathbf{b}^*_n&-\end{bmatrix}

********************************************************************************
Independence, Rank, Inverse Mapping, Basis and Fundamental Subspaces
********************************************************************************
Independence
================================================================================
.. note::
	* Vector :math:`\mathbf{u}` is linearly independent of vector :math:`\mathbf{v}` if they are not in the same direction.

		* There is no scalar :math:`a\in\mathbb{R}` such that :math:`\mathbf{u}=a\mathbf{v}`
	* Vector :math:`\mathbf{w}` is linearly independent of vectors :math:`\mathbf{u}` and :math:`\mathbf{v}` if it is not in the same place spanned by these.

		* There are no scalars :math:`a,b\in\mathbb{R}` such that :math:`\mathbf{w}=a\mathbf{u}+b\mathbf{v}`
	* Extends naturally for more dimensions.

Rank
================================================================================
Rank determines whether the linear transform :math:`\mathbf{A}` defines a mapping which is **onto** or **into**.

.. note::
	* The number of independent column vectors in a matrix :math:`\mathbf{A}` is the **column-rank**.
	* The number of independent row vectors in a matrix :math:`\mathbf{A}` is the **row-rank**.

.. attention::
	* For any matrix :math:`\mathbf{A}`, column-rank and row-rank are the same, and it is called the **rank of a matrix**, :math:`r\leq m` and :math:`r\leq n`.
	* :math:`r` is the dimensionality of the column-space :math:`C(\mathbf{A})` as well as the row-space :math:`C(\mathbf{A}^\top)`.
	* If :math:`m=n=r`, then the matrix is **full-rank**.

Inverse Mapping
================================================================================
.. note::
	* A full rank matrix :math:`\mathbf{A}:\mathbb{R}^n\mapsto\mathbb{R}^n` defines a **onto** mapping, i.e. it spans the entire range.
	* In such cases, the operation is **one-to-one** as well. There are no two vectors in the domain which maps to the same vector in the range space.
	* We can define an inverse transform in this case as :math:`\mathbf{A}^{-1}:\mathbb{R}^n\mapsto\mathbb{R}^n`.

Basis
================================================================================
.. note::
	* For a matrix :math:`\mathbf{A}` of rank :math:`r`, there are :math:`r` independent column vectors which span :math:`\mathbb{R}^r`.
	* These column vectors form **one** basis of the column space.
	* We note that these don't necessarily have to be orthogonal.

.. attention::
	* There can be multiple basis vectors for a matrix which span the same column space.

Fundamental Subspaces
================================================================================
.. note::
	* We define the **null-space** of :math:`\mathbf{A}:\mathbb{R}^n\mapsto\mathbb{R}^m` as the subspace in the domain :math:`\mathbb{R}^n` which maps to :math:`\mathbf{0}` in the range :math:`\mathbb{R}^m`.

		.. math:: N(\mathbf{A})\subseteq \mathbb{R}^n
	* The vectors in the null-space span a :math:`n-r` dimensional space where :math:`r` is the rank of the matrix.

		* We prefer the basis for the null-space to be orthogonal although it's not a necessity.
	* The **right-null-space** is defined as the null-space of the transposed transform :math:`\mathbf{A}^\top`.

.. attention::
	* :math:`\dim(C(\mathbf{A}))=r` and :math:`\dim(N(\mathbf{A}^\top))=m-r`
	* :math:`\dim(C(\mathbf{A}^\top))=r` and :math:`\dim(N(\mathbf{A}))=n-r`

********************************************************************************
Orthogonality
********************************************************************************
Orthogonal vectors
================================================================================
.. note::
	Two vectors :math:`\mathbf{u}` and :math:`\mathbf{v}` are orthogonal if :math:`\mathbf{u}^\top\mathbf{v}=0`.

.. tip::
	* Pythagoras: For :math:`\mathbf{x}\mathop{\bot}\mathbf{y}`

		.. math:: ||\mathbf{x}-\mathbf{y}||=(\mathbf{x}-\mathbf{y})^\top(\mathbf{x}-\mathbf{y})=\mathbf{x}^\top\mathbf{x}+\mathbf{y}^\top\mathbf{y}-\mathbf{x}^\top\mathbf{y}-\mathbf{y}^\top\mathbf{x}=\mathbf{x}^\top\mathbf{x}+\mathbf{y}^\top\mathbf{y}=||\mathbf{x}||+||\mathbf{y}||
	* In general, :math:`\mathbf{x}^\top\mathbf{y}=||\mathbf{x}||\cdot||\mathbf{y}||\cdot\cos\theta`

.. attention::
	* If :math:`\mathbf{x}\in N(\mathbf{A})`, then for any :math:`k`, :math:`\mathbf{a}^*_k\mathop{\bot}\mathbf{x}` as :math:`(\mathbf{a}^*_k)^\top\mathbf{x}=0`.
	* Therefore, any vector in the null-space cannot be spanned by the row-space of :math:`\mathbf{A}`.

Orthonormal vectors
================================================================================
.. note::
	Orthogonal vectors such that :math:`||\mathbf{u}||=1`.

Matrix with orthonormal columns
================================================================================
.. note::
	* Written as :math:`\mathbf{Q}`.
	* We note that :math:`\mathbf{Q}^\top\mathbf{Q}=\mathbf{I}`.
	* **Doesn't change the length:** :math:`||\mathbf{Q}\mathbf{x}||=||\mathbf{x}||` but might lose/gain a few dimensions though based on the dimensionality of :math:`\mathbf{Q}`.

		.. math:: ||\mathbf{Q}\mathbf{x}||=(\mathbf{Q}\mathbf{x})^\top(\mathbf{Q}\mathbf{x})=\mathbf{x}^\top(\mathbf{Q}^\top\mathbf{Q})\mathbf{x}=\mathbf{x}^\top\mathbf{x}=||\mathbf{x}||
	* If :math:`\mathbf{Q}_1` and :math:`\mathbf{Q}_2` are matrices with orthonormal columns, then :math:`\mathbf{Q}=\mathbf{Q}_1\mathbf{Q}_2` is also a matrix with orthonormal columns.

		.. math:: \mathbf{Q}^\top\mathbf{Q}=(\mathbf{Q}_1\mathbf{Q}_2)^\top(\mathbf{Q}_1\mathbf{Q}_2)=\mathbf{Q}_2^\top(\mathbf{Q}_1^\top\mathbf{Q}_1)\mathbf{Q}_2=\mathbf{Q}_2^\top\mathbf{Q}_2=\mathbf{I}

Projection matrices
================================================================================
.. note::
	* Any matrix that can be factorised as :math:`\mathbf{P}=\mathbf{Q}\mathbf{Q}^\top` is a projection matrix. 
	* For any vector :math:`\mathbf{v}`, :math:`\mathbf{P}\mathbf{v}` is the orthogonal projection onto the column space of :math:`\mathbf{P}`.
	* Any vector :math:`\mathbf{v}` can be broken into two parts

		* Projection :math:`\mathbf{P}\mathbf{v}`
		* Error :math:`\mathbf{v}-\mathbf{P}\mathbf{v}`

.. attention::
	* **Repeated projection doesn't change anything**

		.. math:: \mathbf{P}^2=(\mathbf{Q}\mathbf{Q}^\top)(\mathbf{Q}\mathbf{Q}^\top)=\mathbf{Q}(\mathbf{Q}^\top\mathbf{Q})\mathbf{Q}^\top=\mathbf{Q}\mathbf{Q}^\top=\mathbf{P}
	* **Projection matrices are symmetric**

		.. math:: \mathbf{P}^\top=(\mathbf{Q}\mathbf{Q}^\top)^\top=(\mathbf{Q}^\top)^\top\mathbf{Q}^\top=\mathbf{Q}\mathbf{Q}^\top=\mathbf{P}

Orthogonal matrices
================================================================================
.. note::
	Square matrices with orthonormal columns.

.. attention::
	* We have :math:`\mathbf{Q}^\top=\mathbf{Q}^{-1}` since

		.. math:: \mathbf{Q}^\top\mathbf{Q}=\mathbf{Q}\mathbf{Q}^\top=\mathbf{I}
	* They represent a **pure rotation** or **reflection** in :math:`\mathbb{R}^n` as neither the length or the dimensionality changes of any vector under this transformation.

		* Positive determinant implies rotation, negative determinant implies reflection (as the orientation changes).

Orthonormal basis
================================================================================
.. note::
	* Standard co-ordinate vectors are an example of orthonormal basis.
	* It's not necessary for basis vectors to be orthonormal but it's desired.
	* For orthonormal basis, we can obtain the scalar along each component independently.

		* Let the orthogonal basis vectors are :math:`\mathbf{q}_1,\cdots,\mathbf{q}_n`. Then any vector :math:`\mathbf{v}\in\mathbb{R}^n` can be expressed as

			.. math:: \mathbf{v}=c_1\mathbf{q}_1+\cdots+c_n\mathbf{q}_n
		* The scalar along any :math:`\mathbf{q}_k` can be obtained as :math:`c_k=\mathbf{q}_k^\top\mathbf{v}` since

			.. math:: \mathbf{q}_k^\top\mathbf{v}=c_1\mathbf{q}_k^\top\mathbf{q}_1+\cdots+c_k\mathbf{q}_k^\top\mathbf{q}_k+\cdots+c_n\mathbf{q}_k^\top\mathbf{q}_n=c_1\cdot0+\cdots+c_k\cdot1+\cdots+c_n\cdot0=c_k

.. tip::
	* We can create an orthogonal matrix :math:`\mathbf{Q}` with the basis vectors as columns. Then all these coefficients can be found using :math:`\mathbf{Q}\mathbf{v}`.

Orthogonal subspace
================================================================================
.. attention::
	* :math:`C(\mathbf{A})\mathop{\bot} N(\mathbf{A}^\top)` and :math:`C(\mathbf{A}^\top)\mathop{\bot} N(\mathbf{A})`
	* :math:`\mathbf{A}:\text{span}\left(C(\mathbf{A}^\top)\mathop{\cup} N(\mathbf{A})\right)=\mathbb{R}^n\mapsto \text{span}\left(C(\mathbf{A})\mathop{\cup} N(\mathbf{A}^\top)\right)=\mathbb{R}^m`
