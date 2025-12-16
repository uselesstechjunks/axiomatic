################################################################################
Matrix Factorisation
################################################################################

********************************************************************************
A=CR
********************************************************************************
This factorisation keeps the columns of the original matrix intact.

.. note::
	* Let the column matrix be :math:`\mathbf{C_0}=[]`
	* For :math:`i=1` to :math:`r`:

		* Select column :math:`\mathbf{a}_i` if :math:`\mathbf{a}_i\notin\text{span}(C_i)`
		* Update :math:`\mathbf{C_i}=\begin{bmatrix}\mathbf{C_{i-1}}\\ \mathbf{a}_i\end{bmatrix}`
	* To find :math:`R`:

		* For the columns of :math:`\mathbf{A}` that are already in :math:`\mathbf{C}`, the row would have a 1 to select that column and 0 everywhere else.
		* For the dependent columns, we put the right coefficients which recreates the column from others above it.

.. attention::
	* The column vectors in :math:`\mathbf{C}` create one of the basis for :math:`C(\mathbf{A})`.

.. tip::
	* If the matrix is made of data, then this is desirable as it preserves the original columns.
	* A similar factorisation can also be achieved using original rows as well, :math:`\mathbf{A}=\mathbf{C}\mathbf{M}\mathbf{R}` where :math:`\mathbf{R}` consists of indepoendent row-vectors and :math:`\mathbf{M}_{r\times r}` is a mixing matrix.

********************************************************************************
LU Factorisation
********************************************************************************
.. note::
	* Applicable for square matrices where the matrix can be thought of as :math:`n` equations with :math:`n` unknowns.
	* It is an iterative process where every step we peel off the first column and first row of the remaining matrix until we reach a :math:`1\times 1` matrix.

		.. math:: \mathbf{A}=\begin{bmatrix}a_{1,1}&a_{1,2}&\dots&a_{1,n}\\a_{2,1}&a_{2,2}&\dots&a_{2,n}\\\vdots&\vdots&\dots&\vdots\\a_{n,1}&a_{n,2}&\dots&a_{n,n}\end{bmatrix}=\begin{bmatrix}1\\\frac{a_{2,1}}{a_{1,1}}\\\vdots\\\frac{a_{n,1}}{a_{1,1}}\end{bmatrix}\begin{bmatrix}a_{1,1}&a_{1,2}&\dots&a_{1,n}\end{bmatrix}+\begin{bmatrix}0 & 0 & \dots & 0\\0 & \left(a_{2,2}-\frac{a_{2,1}a_{1,2}}{a_{1,1}}\right) & \dots & \left(a_{2,n}-\frac{a_{2,1}a_{1,n}}{a_{1,1}}\right)\\\vdots&\vdots&\dots&\vdots\\0 & \left(a_{n,2}-\frac{a_{n,1}a_{1,2}}{a_{1,1}}\right) & \dots & \left(a_{n,n}-\frac{a_{n,1}a_{1,n}}{a_{1,1}}\right)\end{bmatrix}=\mathbf{l}_1\mathbf{u}^*_1+\begin{bmatrix}0 & \dots\\\vdots & \mathbf{A}_2\end{bmatrix}
	* At the end of the process, we're left with the sum of all rank 1 matrices

		.. math:: \mathbf{A}=\mathbf{l}_1\mathbf{u}^*_1+\cdots+\mathbf{l}_n\mathbf{u}^*_n=\begin{bmatrix}|&\cdots&|\\\mathbf{l}_1&\cdots&\mathbf{l}_n\\|&\cdots&|\end{bmatrix}\begin{bmatrix}-&\mathbf{u}^*_1&-\\\vdots&\vdots&\vdots\\-&\mathbf{u}^*_n&-\end{bmatrix}=\mathbf{L}\mathbf{U}
	* The matrix :math:`\mathbf{L}` is lower triangular with :math:`1s` in its diagonal, where as the matrix :math:`\mathbf{U}` is upper triangular.

********************************************************************************
LDLT Factorisation
********************************************************************************
.. note::
	* For symmetric matrices :math:`\mathbf{A}`, the :math:`\mathbf{U}` factor can be expressed in terms of :math:`\mathbf{L}` after pulling out the diagonal elements to make it all :math:`1s`.

		.. math:: \mathbf{A}=\mathbf{L}\mathbf{D}\mathbf{L}^\top

********************************************************************************
Cholesky Factorisation
********************************************************************************
.. note::
	* We can take square root of the diagonal and push inside the :math:`\mathbf{L}` to obtain factorisation in the form

		.. math:: \mathbf{A}=\mathbf{L}\mathbf{L}^\top

********************************************************************************
Gram-Schmidt Orgthogonalisation
********************************************************************************

********************************************************************************
Eigendecomposition
********************************************************************************
.. note::
	* When we're dealing with square matrices :math:`\mathbf{A}_{n\times n}`, we can think of the matrix transforming the input space by rotating or stretching or flipping every vector in the entire space.
	* Under such a linear transform, there are certain directions which stay fixed (they don't rotate). They just get stretched or flipped.
	* For any vector along these directions, the effect of matrix multiplication is just the same as scalar multiplication which stretches/flips the vectors.

		.. math:: \mathbf{A}\mathbf{x}=\lambda\mathbf{x}

		* :math:`\lambda` is a eigenvalue and :math:`\mathbf{x}` is a eigenvector of :math:`\mathbf{A}`.
		* These are determined entirely by the matrix of the linear transform :math:`\mathbf{A}`.
	* If all such vectors are collected in a matrix, then

		.. math:: \mathbf{A}\mathbf{X}=\mathbf{A}\begin{bmatrix}|&|&\cdots&|\\\mathbf{x}_1&\mathbf{x}_2&\cdots&\mathbf{x}_n\\|&|&\cdots&|\end{bmatrix}=\begin{bmatrix}|&|&\cdots&|\\\mathbf{A}\mathbf{x}_1&\mathbf{A}\mathbf{x}_2&\cdots&\mathbf{A}\mathbf{x}_n\\|&|&\cdots&|\end{bmatrix}=\begin{bmatrix}|&|&\cdots&|\\\lambda_1\mathbf{x}_1&\lambda_2\mathbf{x}_2&\cdots&\lambda_n\mathbf{x}_n\\|&|&\cdots&|\end{bmatrix}=\begin{bmatrix}|&|&\cdots&|\\\mathbf{x}_1&\mathbf{x}_2&\cdots&\mathbf{x}_n\\|&|&\cdots&|\end{bmatrix}\begin{bmatrix}\lambda_1 & 0 & \dots & 0 \\ 0 & \lambda_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \lambda_n\end{bmatrix}=\mathbf{X}\boldsymbol{\Lambda}

	* Therefore, the matrix factorises as 

		.. math:: \mathbf{A}=\mathbf{A}(\mathbf{X}\mathbf{X}^{-1})=(\mathbf{A}\mathbf{X})\mathbf{X}^{-1}=(\mathbf{X}\boldsymbol{\Lambda})\mathbf{X}^{-1}=\mathbf{X}\boldsymbol{\Lambda}\mathbf{X}^{-1}

Real and Complex Eigenvalues
================================================================================
.. note::
	* The eigenvalues can be real or complex.
		
		* **Symmetric matrices have real eigenvalues** 
		* **Orthogonal matrices have complex eigenvalues**.

Matrix power
================================================================================
	.. math:: \mathbf{A}^n\mathbf{u}=(\mathbf{X}\boldsymbol{\Lambda}\mathbf{X}^{-1})^n\mathbf{u}=(\mathbf{X}\boldsymbol{\Lambda}\mathbf{X}^{-1})(\mathbf{X}\boldsymbol{\Lambda}\mathbf{X}^{-1})\cdots(\mathbf{X}\boldsymbol{\Lambda}\mathbf{X}^{-1})\mathbf{u}=(\mathbf{X}\boldsymbol{\Lambda}^n\mathbf{X}^{-1})\mathbf{u}

.. attention::
	* For the eigenvalues that are real, the vectors get stretched repeatedly (and flipped alternatively, if eigenvalues are negative) along that direction as the effect is the same as multiplication by a real number.
	* For the eigenvalues that are complex, the vectors oscilate as the effect is the same as multiplication by a complex number.

.. tip::
	:math:`\exp(\mathbf{A})=\mathbf{X}\exp(\boldsymbol{\Lambda})\mathbf{X}^{-1}`

Trace and Determinant
================================================================================
.. note::
	* **Trace**: :math:`\sum_{i=1}^n\lambda_i`
	* **Determinant**: :math:`\prod_{i=1}^n\lambda_i`

Similar Matrices
================================================================================
.. note::
	* The matrix :math:`\mathbf{A}` and any other matrix in the form :math:`\mathbf{M}=\mathbf{B}\mathbf{A}\mathbf{B}^{-1}` have the same eigenvalues.
	* The eigenvectors corresponding to each such :math:`\lambda` is obtained by :math:`\mathbf{B}\mathbf{x}` whenever :math:`\mathbf{A}\mathbf{x}=\lambda\mathbf{x}`

		.. math:: (\mathbf{B}\mathbf{A}\mathbf{B}^{-1})(\mathbf{B}\mathbf{x})=\mathbf{B}\mathbf{A}(\mathbf{B}^{-1}\mathbf{B})\mathbf{x}=\mathbf{B}\mathbf{A}\mathbf{x}=\lambda\mathbf{B}\mathbf{x}
	* So :math:`\mathbf{A}` and :math:`\mathbf{M}` are called **similar matrices**.

		* They stretch/flip the vectors in the same fashion, but in a different orientation.

Properties
================================================================================
.. warning::
	* It is not necessary that the eigenvectors are orthogonal.

		* Eigenvectors are orthogonal :math:`\iff\mathbf{A}\mathbf{A}^\top=\mathbf{A}^\top\mathbf{A}`
	* It is not necessary that the eigenvalues are all distinct.

		* All eigenvalues are distinct :math:`\iff` the matrix is full rank.
	* Double eigenvalues :math:`\lambda_i=\lambda_j` might or might not have independent eigenvectors.
	* **In general**

		* :math:`\lambda(\mathbf{A}+\mathbf{B})\neq\lambda(\mathbf{A})+\lambda(\mathbf{B})`
		* :math:`\lambda(\mathbf{A}\mathbf{B})\neq\lambda(\mathbf{A})\cdot\lambda(\mathbf{B})`

.. tip::
	For :math:`\mathbf{B}=\mathbf{A}-a\cdot\mathbf{I}`, :math:`\lambda(\mathbf{B})=\lambda(\mathbf{A})-a`

Special case: Symmetric Real Matrices
================================================================================
.. note::
	* For real symmetric matrices :math:`\mathbf{S}`

		* The eigenvalues are all real
			
			* Proof Hint: Multiply with complex conjugate of eigenvectors.

				* Let :math:`\bar{\mathbf{x}}=\begin{bmatrix}\bar{x_1}\\\vdots\\\bar{x_n}\end{bmatrix}=\begin{bmatrix}a_1-ib_1\\\vdots\\a_n-ib_n\end{bmatrix}` be the complex conjugate of the eigenvector :math:`\mathbf{x}=\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}=\begin{bmatrix}a_1+ib_1\\\vdots\\a_n+ib_n\end{bmatrix}\in\mathbb{C}^n`.
				* We have :math:`\bar{\mathbf{x}}^\top\mathbf{S}\mathbf{x}=\lambda\bar{\mathbf{x}}^\top\mathbf{x}`
				* From RHS: :math:`\sum_{i=1}^n\bar{x_i}x_i=\sum_{i=1}^n a_i^2+b_i^2`, all real.
				* The LHS: :math:`S_{1,1}(\bar{x_1}x_1)+S_{1,2}(\bar{x_1}x_2+\bar{x_2}x_1)+\cdots`.
				* Terms of the form :math:`S_{i,i}(\bar{x_i}x_i)` are all real.
				* Terms of the form :math:`S_{i,j}(\bar{x_i}x_j+\bar{x_j}x_i)=S_{i,j}\left((a_i-ib_i)(a_i+ib_i)+(a_i+ib_i)(a_i-ib_i)\right)` which is also real.
				* Therefore, :math:`\lambda` must be real.
		* The eigenvectors are orthogonal

			* Proof Hint: Involve null-space and utilise the fact that for symmetric matrices, row-space and column-space are the same.

				* For some :math:`i\neq j`, let :math:`\lambda_i` and :math:`\lambda_j` be two eigenvalues with corresponding eigenvectors :math:`\mathbf{x}_i` and :math:`\mathbf{x}_j`.
				* We have :math:`(\mathbf{S}-\lambda_i\mathbf{I})\mathbf{x}_i=\mathbf{0}`. Therefore

					.. math:: \mathbf{x}_i\in N(\mathbf{S}-\lambda_i\mathbf{I})
				* We also have :math:`(\mathbf{S}-\lambda_i\mathbf{I})\mathbf{x}_j=(\lambda_j-\lambda_i)\mathbf{x}_j`. Therefore

					.. math:: \mathbf{x}_j\in C(\mathbf{S}-\lambda_i\mathbf{I})=C((\mathbf{S}-\lambda_i\mathbf{I})^\top)
				* Therefore, :math:`\mathbf{x}_i\mathop{\bot}\mathbf{x}_j` for :math:`i\neq j`.

.. tip::
	* We usually write :math:`\mathbf{S}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top`
	* Every matrix in this form is symmetric

		.. math:: \mathbf{S}^\top=(\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top)^\top=(\mathbf{Q}^\top)^\top\boldsymbol{\Lambda}^\top\mathbf{Q}^\top=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top=\mathbf{S}

Positive Definite Matrices
--------------------------------------------------------------------------------
Multiplication by a pd matrix is similar to multiplying by a positive real number.

Tests for positive definiteness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* All eigenvalues are positive.
	* **Quadratic Form**: For any vector :math:`\mathbf{x}\neq\mathbf{0}`, :math:`\mathbf{x}^\top\mathbf{S}\mathbf{x} > 0`.
	* The matrix :math:`\mathbf{S}` can be factorised as :math:`\mathbf{S}=\mathbf{A}^\top\mathbf{A}`.

		* Choices for :math:`\mathbf{A}` can be

			* :math:`\mathbf{S}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^\top=(\sqrt{\boldsymbol{\Lambda}}\mathbf{Q}^\top)^\top(\sqrt{\boldsymbol{\Lambda}}\mathbf{Q}^\top)=\mathbf{A}^\top\mathbf{A}`
			* :math:`\mathbf{S}=\mathbf{L}\mathbf{L}^\top`
	* The leading determinants :math:`D_1,D_2,\cdots,D_n` are all positive.
	* In LU elimination, the pivot elements are all positive.

Positive Semi-definite Matrices
--------------------------------------------------------------------------------
.. note::
	* All eigenvalues are :math:`\geq 0`
	* **Quadratic Form**: For any vector :math:`\mathbf{x}\neq\mathbf{0}`, :math:`\mathbf{x}^\top\mathbf{S}\mathbf{x} \geq 0`.

********************************************************************************
Singular Value Decomposition
********************************************************************************
.. csv-table:: Comparison with Eigen stuff
	:header: "Eigenvalues/vectors", "Singular values/vectors"
	:align: center
	:widths: 40, 40
	:class: longtable

	Works with :math:`\mathbf{A}:\mathbb{R}^n\mapsto\mathbb{R}^n`, Works with :math:`\mathbf{A}:\mathbb{R}^n\mapsto\mathbb{R}^m`	
	Eigenvalues can be real or complex., Singular values are non-negative real numbers.
	Eigenvectors are not always to be orthogonal to one another., Singular vectors are orthonormal.

.. tip::
	* Eigen decompositon finds directions in the :math:`\mathbb{R}^n` (input=output) space that are invariant under the operator. Along those directions the operator acts the same as a scalar multiplier.
	* Singular value decomposition finds directions in the input space :math:`\mathbb{R}^n` and a different set of directions in the output space :math:`\mathbb{R}^m` such that the operator produces a scaled version of these output vectors when applied to any vector in those input directions.

.. note::
	* Let :math:`\mathbf{v}\in\mathbb{R}^n` a singular vector in the input dimension, :math:`\mathbf{u}\in\mathbb{R}^m` a singular vector in the output dimension, and :math:`\sigma` be the singular value for the matrix :math:`\mathbf{A}`. Then

		.. math:: \mathbf{A}\mathbf{v}=\sigma\mathbf{u}
	* If all such vectors are collected in a matrix, then

		.. math:: \mathbf{A}\mathbf{V}=\mathbf{U}\boldsymbol{\Sigma}\implies\mathbf{A}=\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\top
	* We note that :math:`\mathbf{V}` and :math:`\mathbf{U}` are not square, not are matrices with orthonormal columns while :math:`\mathbf{\Sigma}` is a square, diagonal matrix containing all the singular values.

Computing singular values and vectors
================================================================================
We formulate SVD via Eigendecomposition.

.. note::
	* Let :math:`\mathbf{M}=\mathbf{A}^\top\mathbf{A}` and :math:`\mathbf{N}=\mathbf{A}\mathbf{A}^\top`.

		* We note that :math:`\mathbf{M}` and :math:`\mathbf{N}` are symetric, hence have **real eigenvalues** and **orthonormal eigenvectors**.

			.. math:: \mathbf{M}^\top=(\mathbf{A}^\top\mathbf{A})^\top=\mathbf{A}^\top\mathbf{A}=\mathbf{M}\\\mathbf{N}^\top=(\mathbf{A}\mathbf{A}^\top)^\top=\mathbf{A}\mathbf{A}^\top=\mathbf{N}
	* Reformualtion in terms of eigen decomposition

		* :math:`\mathbf{M}=\mathbf{A}^\top\mathbf{A}=(\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\top)^\top\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^\top=\mathbf{V}\boldsymbol{\Sigma}^\top(\mathbf{U}^\top\mathbf{U})\boldsymbol{\Sigma}\mathbf{V}^\top=\mathbf{V}\boldsymbol{\Sigma}^2\mathbf{V}^\top`
		* Similarly, :math:`\mathbf{N}=\mathbf{U}\boldsymbol{\Sigma}^2\mathbf{U}^\top`
	* From the 2 eigen decompositions we obtain 
	
		* **Singular values**: the diagonal matrix :math:`\boldsymbol{\Sigma}=\sqrt{\boldsymbol{\Lambda}}` and 
		* **Singular vectors**: the set of vectors :math:`\mathbf{U}` and :math:`\mathbf{V}`.
	* Since each :math:`\sigma=\sqrt{\lambda}`, we need to ensure that :math:`\lambda\geq 0`.

		* :math:`\mathbf{x}^\top\mathbf{M}\mathbf{x}=\mathbf{x}^\top\mathbf{A}^\top\mathbf{A}\mathbf{x}=||\mathbf{A}\mathbf{x}||\geq 0`
		* :math:`\mathbf{y}^\top\mathbf{N}\mathbf{y}=\mathbf{y}^\top\mathbf{A}\mathbf{A}^\top\mathbf{y}=||\mathbf{A}^\top\mathbf{y}||\geq 0`
		* Therefore, :math:`\mathbf{M}` and :math:`\mathbf{N}` are positive semi definite, so :math:`\sqrt{\lambda}` is real.

.. tip::
	* Singular values are arranged in descending order, :math:`\sigma_1\geq\sigma_2\geq\cdots\sigma_r\geq 0=\cdots 0`, where :math:`r` is the rank of the matrix.
	* Any linear transformation :math:`\mathbf{A}=\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^T` can be thought of as a 

		* pure rotation/flip
		* stretching
		* another pure rotation/flip

	* All the stretching happens due to :math:`\boldsymbol{\Sigma}`.
	* For any vector :math:`\mathbf{x}`, :math:`||\mathbf{A}\mathbf{x}||\leq \sigma_1||\mathbf{x}||` where :math:`\sigma_1` is the first singular value.

		* Proof Hint:

			* We have :math:`||\mathbf{A}\mathbf{x}||=||\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^T\mathbf{x}||`
			* Since :math:`\mathbf{U}` and :math:`\mathbf{V}` are matrices with orthonormal columns, they don't change the length.
			* Therefore, :math:`||\mathbf{A}\mathbf{x}||=||\boldsymbol{\Sigma}\mathbf{x}||=\sigma_1 x_1+\cdots+\sigma_n x_n\leq \sigma_1(x_1+\cdots+x_n)=\sigma_1||\mathbf{x}||`

.. attention::
	* If :math:`A` is a symmetric positive definite matrix, then its SVD is given by its eigen decomposition.
	* If :math:`A` is a matrix with orthonormal columns, then all its singular values are 1.


Eckart-Young: Best rank k approximation
================================================================================
.. attention::
	* Let :math:`\mathbf{A}_k=\sigma_1\mathbf{u}_1\mathbf{v}_1^\top+\cdots+\sigma_k\mathbf{u}_k\mathbf{v}_k^\top` for some :math:`k\leq r`.
	* Let :math:`\mathbf{B}` be any rank :math:`k` matrix.
	* We have :math:`||\mathbf{A}-\mathbf{A}_k||\leq ||\mathbf{A}-\mathbf{B}||`
