################################################################################
Functional Analysis
################################################################################

********************************************************************************
Functions are vectors
********************************************************************************
Intuition
================================================================================
.. tip::
	* We usually think of vectors in finite dimensional case, e.g. :math:`\mathbf{u}\in\mathbb{R}^4`, as a list

		.. math:: \mathbf{u}=\begin{bmatrix}0.3426 \\1.3258 \\6.8943 \\8.3878 \\\end{bmatrix}\\
	* An alternate way to look at this is as a list of tuples, which binds the dimension (integer index in this case) and the value of that dimension

		.. math:: \mathbf{u}=\left((0,0.3426),(1,1.3258),(2,6.8943),(3,8.387)\right)

		* This can be represented by a function
	
			.. math:: u:[0,1,2,3]\mapsto[0.3426,1.3258,6.8943,8.387]
		* In general, these sort of functions can be represented by 
	
			.. math:: u:\mathcal{I}\mapsto\mathbb{R}
	
			where :math:`\mathcal{I}` is a finite index set.
	* If we extend :math:`\mathcal{I}` to be countably infinite or uncountable (e.g. :math:`\mathbb{N}` or :math:`\mathbb{R}`), then, we end up with infinite lists of tuples, e.g.

		.. math:: f=\{(x,y)|x,y\in\mathbb{R}\}
	
		* This is the way functions are defined in set theory, where the dimension of each function (informally) is :math:`|\mathcal{X}|`.

Cardinality of Function Space
--------------------------------------------------------------------------------
.. note::
	* The space of functions :math:`f:\mathcal{X}\mapsto\mathcal{Y}` is often denoted by :math:`\mathcal{Y}^{\mathcal{X}}`.

		* For every element :math:`x\in\mathcal{X}`, we have a choice to make its image map to some :math:`y\in\mathcal{Y}`.
		* Therefore, the size of this choice for each :math:`x\in\mathcal{X}` is :math:`|\mathcal{Y}|`.
		* The size of the choice for **all** the elements in :math:`\mathcal{X}` is therefore :math:`|\mathcal{Y}|^{|\mathcal{X}|}`.

.. tip::
	* To remember, we can think of the selection problem, where we have :math:`n` items which are either selected or discarded.
		
		* We know from combinatorics that the total number of such choices is :math:`2^n`.
		* This can be formed as a function where each of the :math:`n` elements map to either 0 or 1.
	* We also verify that function view of real-valued vectors which maps the index set (of size :math:`d`) to reals also make sense since we represent the dimension as :math:`\mathbb{R}^d`.

Technicalities
================================================================================
As long as we're restricting ourselves to the class of functions from one vector (linear) space :math:`\mathcal{X}` to another :math:`\mathcal{Y}` over the same underlying scalar field :math:`\mathbb{F}`, we can faithfully recover many useful properties from a finite dimensional vector spaces for the (potentially infinite dimensional) space of functions.

Addition and Scalar Multiplication
--------------------------------------------------------------------------------
.. note::
	* For finite dimensional vectors :math:`\mathbf{u},\mathbf{v}\in V_{\mathcal{F}}`, where :math:`\mathcal{F}` is the underlying field:

		* [Vector Addition]: We add the corresponding values for each dimension.
		* [Scalar Multiplication]: For any :math:`\alpha\in\mathcal{F}`, we multiply :math:`\alpha\in\mathcal{F}` to the value of each dimension.
	* For functions :math:`f:\mathcal{X}\mapsto\mathcal{Y}` and :math:`g:\mathcal{X}\mapsto\mathcal{Y}`, the dimensions are :math:`x\in\mathcal{X}`. 

		* [Vector Addition]: We can define vector addition of a function for each "dimension" :math:`x`

			.. math:: (f + g)(x) = f(x) + g(x)
		* [Scalar Multiplication]: We can define scalar multiplication for each "dimension" :math:`x`

			.. math:: (\alpha\cdot f)(x) = \alpha\cdot f(x)

.. tip::
	With :math:`\mathcal{X}` and :math:`\mathcal{Y}` being linear space over the same scalar field, the addition and scalar multiplication makes sense.

Inner Product
--------------------------------------------------------------------------------
.. note::
	* For finite dimensional vectors :math:`\mathbf{u},\mathbf{v}\in V_{\mathcal{F}}`, to compute the inner (dot) product

		* We take a scalar product of the corresponding values for each dimension.
		* We sum the results across all dimensions.

			.. math:: \langle\mathbf{u},\mathbf{v}\rangle=\sum_{i=1}^n u_i\cdot v_i

.. warning::
	* Let's add a constraint that :math:`\mathcal{Y}` is equipped with an inner product.
	* Let's add a constraint that :math:`\mathcal{X}` is equipped with a positive measure :math:`\mu(x)` and :math:`\mathop{d\mu}(x)=\mathop{dx}`.

.. note::
	* For functions :math:`f:\mathcal{X}\mapsto\mathcal{Y}` and :math:`g:\mathcal{X}\mapsto\mathcal{Y}`

		* We can take a scalar product for each dimension :math:`x`.
		* Since :math:`\mathcal{X}` can be uncountable, we replace the sum with integration

			.. math:: \langle f,g\rangle=\int_{\mathcal{X}}f(x)\cdot g(x)\mathop{dx}

.. tip::
	With :math:`\mathcal{Y}` being an inner product space, dot product under the integral makes sense.

Orthogonality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* Two functions :math:`f` and :math:`g` are orthogonal if their inner product is 0.
	* Example: For real trig functions :math:`\sin:[0,\pi]\mapsto[0,1]\in\mathbb{R}` and :math:`\cos:[0,\pi]\mapsto[-1,1]\in\mathbb{R}`

		.. math:: \langle\sin,\cos\rangle=\int_\limits{0}^{\pi}\sin(x)\cos(x)\mathop{dx}=0

Norm - Induced by the Inner Product
--------------------------------------------------------------------------------
Lp Space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* The inner product for finite vectors induces a norm (:math:`l_2`)

		.. math:: ||\mathbf{u}||_2^2=\langle \mathbf{u},\mathbf{u}\rangle=\sum_{i=1}^n|u_i|^2
	* The inner product defined above induces a norm

		.. math:: ||f||_2^2=\langle f,f\rangle=\int_{\mathcal{X}}|f(x)|^2\mathop{dx}
	* More generally, we can have

		.. math:: ||f||_{L_p}=\left(\int_{\mathcal{X}}|f(x)|^p\mathop{dx}\right)^{1/p}

.. tip::
	* For more general measurable spaces where we have a measure :math:`\mu(x)` defined

		.. math:: ||f||_{L_p(\mathcal{X},\mu)}=\left(\int_{\mathcal{X}}|f(x)|^p\mathop{d\mu}(x)\right)^{1/p}
	* For :math:`p=\infty`

		.. math:: ||f||_{L_\infty(\mathcal{X},\mu)}=\text{ess}\sup_\limits{x\in\mathcal{X}}|f(x)|
	* We write the function space as :math:`L^p(\mathcal{X},\mathcal{Y})=\{f|f:\mathcal{X}\mapsto\mathcal{Y};\text{such that }L_p(\mathcal{X,\mu})\text{ exists}\}`

		* Example: :math:`L^2([0,1],\mathbb{R})`

Metric - Induced by the Norm
--------------------------------------------------------------------------------
.. note::
	* The :math:`l_p` norm for finite vectors induces a metric 

		.. math:: d(\mathbf{u}, \mathbf{v})=||\mathbf{u}-\mathbf{v}||_p=\left(\sum_{i=1}^n|u_i-v_i|^p\right)^{1/p}
	* We can define, similarly, for functions

		.. math:: d(f, g)=||f-g||_{L_p(\mathcal{X},\mu)}=\left(\int_\limits{i=1}^n|f(x)-g(x)|^p\mathop{d\mu}(x)\right)^{1/p}

		* If :math:`d(f, g)=0`, then the functions are the same "almost everywhere".
		* In this case, whereever they are different has **measure zero** (e.g, finitely many points or "dimensions").

Topological Properties
--------------------------------------------------------------------------------
.. note::
	With a metric defined, we can define topological properties such as convergence and complete function spaces.

.. tip::
	* Complete normed spaces are known as `Banach Space <https://en.wikipedia.org/wiki/Banach_space>`_.
	* Complete normed spaces where the norm is induced by inner-product are known as `Hilbert Space <https://en.wikipedia.org/wiki/Hilbert_space>`_.

.. warning::
	* Without the metric, the only topology we can have for the set of functions is the `product topology <https://en.wikipedia.org/wiki/Product_topology>`_ (as suggested by :math:`\mathcal{Y}^{\mathcal{X}}`).
	* With product topology, the only convergence that we can define is `point-wise convergence <https://en.wikipedia.org/wiki/Pointwise_convergence#topology_of_pointwise_convergence>`_ which is a weak form of convergence.

Point-wise Convergence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* Let :math:`(f_n)_{n=1}^\infty` be a sequence of functions where :math:`f_n:\mathcal{X}\mapsto\mathcal{Y}`.
	* Let :math:`f` be another function :math:`f:\mathcal{X}\mapsto\mathcal{Y}`
	* We say that the sequence is point-wise converging towards :math:`f`

		.. math:: \lim\limits_{n\to\infty}f_n=f\iff\forall x\in\mathcal{X}, \lim\limits_{n\to\infty}f_n(x)=f(x)

Uniform Convergence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* We can make a stronger convergence criterion for functions which map to a metric space :math:`\mathcal{Y}` (i.e., where :math:`\sup` makes sense).
	* We say that the sequence is uninformly converging towards :math:`f`

		.. math:: \lim\limits_{n\to\infty}f_n=f\iff\lim\limits_{n\to\infty}\sup\{|f_n(x)-f(x)|:x\in\mathcal{X}\}=0

.. tip::
	* All uniformly convergent functions are point-wise convergent.
	* The converse is not true.

Linear Transforms
--------------------------------------------------------------------------------
Linear Transforms on Euclidean Space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* We consider a set of unit-vectors (i.e. normalized but not necessarily orthogonal) in :math:`\mathbb{R}^n` for a finite dimensional vector space as

		.. math:: \{\mathbf{a}_1,\cdots\mathbf{a}_n\}	
	* We can find the projection of any vector :math:`\mathbf{u}\in\mathbb{R}^n` onto each of the basis

		.. math:: \langle\mathbf{a}_i,\mathbf{u}\rangle
	* Under the new basis, this gives the i-th co-ordinate for the result vector :math:`\mathbf{v}`

		.. math:: \begin{bmatrix}0\\\vdots\\v_i\\\vdots\\0\end{bmatrix}=\langle\mathbf{a}_i,\mathbf{u}\rangle
	* We note that we can collect the basis vectors inside a matrix as rows and express the relation as

		.. math:: \mathbf{v}=\begin{bmatrix}-&\mathbf{a_1^*}&-\\ \vdots&\vdots&\vdots\\ -&\mathbf{a_n^*}&-\\\end{bmatrix}\mathbf{u}=\mathbf{A}^T\mathbf{u}
	* We also note that the final vector can be written as a sum

		.. math:: \mathbf{v}=\sum_{i=1}^n\begin{bmatrix}0\\\vdots\\v_i\\\vdots\\0\end{bmatrix}=\sum_{i=1}^n\langle\mathbf{u},\mathbf{a}_i\rangle

Function view
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* Let :math:`\mathcal{I}=\{1,\cdots,d\}` be the index set.
	* The vector :math:`\mathbf{u}` defines a function :math:`u:\mathcal{I}\mapsto\mathbb{R}\in\mathcal{U}(\mathcal{I})`
	* The basis vectors :math:`\mathbf{a}_k` are also functions :math:`a_k:\mathcal{I}\mapsto\mathcal{H}` where :math:`\mathcal{H}^{\mathcal{I}}\subseteq\mathbb{R}^d` is the subspace spanned by the basis.
	* Then the matrix :math:`\mathbf{A}` defines a linear transform :math:`A:\mathcal{H}\mapsto\mathcal{U}(\mathcal{I})` where

		.. math:: v(i)=(Au)(i)

Linear Transforms on Function Space
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* We consider functions :math:`f:E\mapsto\mathbb{R}\in\mathcal{F}(E)` (similar to :math:`\mathcal{U}(\mathcal{I})`) where :math:`E` is any abstract space.
	* We consider basis functions :math:`h:E\mapsto\mathcal{H}` where :math:`\mathcal{H}` is a Hilbert space equipped with a norm

		.. math:: \langle \cdot,\cdot\rangle_{\mathcal{H}}
	* For any :math:`x\in E`, the projection onto a basis is given by

		.. math:: f(x)=\langle f,h(x)\rangle_{\mathcal{H}}
	* This defines a linear transform :math:`L:\mathcal{H}\mapsto\mathcal{F}(E)` where 

		.. math:: f(\cdot)=(Lf)(\cdot)

Kernel of a Linear Transform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* The kernel of a linear transform is found by inner products of the basis functions.
	* For finite dimensional case :math:`K:\mathcal{I}\times\mathcal{I}\mapsto\mathbb{R}`

		.. math:: K(i,j)=\langle\mathbf{a}^*_i,\mathbf{a}^*_j\rangle
	* For the functional case :math:`K:E\times E\mapsto\mathbb{R}`

		.. math:: K(x,y)=\langle h(y),h(x)\rangle_{\mathcal{H}}
	* For any fixed :math:`y_n\in E`, :math:`K(x,y_n)` is a function of just :math:`x\in E` in :math:`\mathcal{F}(E)`
	* Therefore, often the basis functions are referred by just the kernel itself as 

		.. math:: K(\cdot,x)=h(x)

		and

		.. math:: K(x,y)=\langle K(\cdot,x),K(\cdot,y)\rangle
	* Symmetry: :math:`K(x,y)=K(y,x)` due to the symmetry of the inner product.
	* Reproducing Property:

		* Function evaluation is inner product: :math:`f(x)=\langle f,K(\cdot,x)\rangle_{\mathcal{H}}`
		* Therefore, knowing the kernel, we can recover any function.
	* Any function :math:`g\in\mathcal{F}(E)` can be expressed as a linear combination of the basis

		.. math:: g(x)=\sum_m\alpha_m K(x,y_m)

.. tip::
	* We note that when the matrix is the centered, normalised data matrix, then the kernel gives the sample covariance matrix.
	* This hints as the usability of functional kernels for covariance functions for infinite dimensional Gaussian distributions (GPs).

Mercer Theorem - Eigenfunctions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	TODO

Other Integral Transforms
--------------------------------------------------------------------------------
General Form
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	TODO

Fourier Basis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* For "well-behaved" (i.e. square-integrable so that one can define :math:`L_2` norm as per above) periodic functions, we can have `basis functions of odd and even frequencies <https://math.stackexchange.com/a/32663>`_.
	* `Schauder basis <https://en.wikipedia.org/wiki/Schauder_basis>`_ (allows for infinite sum over basis):

		* A basis for functions in :math:`L^2([0,1],\mathbb{R})` can be defined in terms of an infinite set of orthonormal functions`

			.. math:: \{1, (\sqrt{2}\sin(2\pi kx))_{k=1}^\infty, (\sqrt{2}\cos(2\pi kx))_{k=1}^\infty\}
		* The :math:`\sin` functions account for odd-frequencies and the :math:`\cos` functions account for even-frequencies.
	* Here we have 3 sets of basis functions, so we use 3 different kinds of normalised-projection co-efficients, :math:`a_0,a_k,b_k`

		.. math:: f(x)=a_0\cdot1+\sum_{k=1}^\infty a_i\cdot\cos(2\pi kx)+\sum_{k=1}^\infty b_i\cdot\sin(2\pi kx)
	* :math:`a_0` computes the projection of :math:`f(x)` onto the constant function :math:`1`.

		.. math:: a_0=\frac{\int_\limits{[0,1]}1\cdot f(x)\mathop{dx}}{\int_\limits{[0,1]}1\cdot 1\mathop{dx}}=\int_\limits{[0,1]}f(x)\mathop{dx}
	* For each :math:`k>0`, :math:`a_k` computes the projection of :math:`f(x)` onto the even frequencies, :math:`\sqrt{2}\cos(2\pi nx)`.

		.. math:: a_k=\frac{\int_\limits{[0,1]}f(x)\cdot\sqrt{2}\cos(2\pi kx)\mathop{dx}}{\int_\limits{[0,1]}\sqrt{2}\cos(2\pi kx)\cdot\sqrt{2}\cos(2\pi kx)\mathop{dx}}
	* Similarly, for :math:`b_k`.

********************************************************************************
Useful Function Spaces
********************************************************************************
Sobolev Space
================================================================================
Holder Space
================================================================================
Reproducing kernel Hilbert space
================================================================================
Moore-Aronszajn Theorem
--------------------------------------------------------------------------------
We assume that the kernel is positive definite.
.. warning::
	For every positive definite kernel :math:`K` on a set :math:`E`, there exists a unique RKHS :math:`\mathcal{H}_k` of functions on :math:`E` for which :math:`K` is the reproducing kernel.

********************************************************************************
Generalised Functions - Distributions
********************************************************************************
Dirac-Delta Function
================================================================================

.. seealso::
	* `Functions are vectors <https://www.youtube.com/watch?v=LSbpQawNzU8>`_
	* `THE GEOMETRY OF MATHEMATICAL METHODS <https://books.physics.oregonstate.edu/GMM/complete.html>`_
	* `Math 353 Lecture Notes Fourier series <https://services.math.duke.edu/~jtwong/math353-2020/lectures/Lec12-Fourier.pdf>`_
	* `[MIT] 9.520 Math Camp 2010 Functional Analysis Review <https://www.mit.edu/~9.520/spring10/Classes/mathcamp2010-fa-notes.pdf>`_
	* `SO post about Dirac delta being a generalized function instead of normal function <https://math.stackexchange.com/a/285643>`_
