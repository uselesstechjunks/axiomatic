##########################################################
Multivariable Calculus
##########################################################
We consider functions from :math:`\mathbb{R}^n` to :math:`\mathbb{R}^m` which are expressed as

	.. math:: \mathbf{f}(\mathbf{x})=\mathbf{f}(x_1,\cdots,x_n)=(f_1(\mathbf{x}),\cdots,f_m(\mathbf{x}))

**********************************************************
Different Forms of Multivariable Functions
**********************************************************
Parametric Surface
==========================================================
.. note::
	* If :math:`n=1` and :math:`m > 1` then the functions :math:`f:\mathbb{R}\mapsto\mathbb{R}^m` are known as parametric sufraces.
	* Example: :math:`f(x)=(x, x^2)`

Scalar field
==========================================================
.. note::
	* If :math:`n> 1` and :math:`m=1` then the functions :math:`f:\mathbb{R}^n\mapsto\mathbb{R}` are known as scalar fields.
	* Example: :math:`f(x,y)=xy`

.. image:: ../../img/1.png
  :width: 300

Vector field
==========================================================
.. note::
	* If :math:`n> 1` and :math:`m> 1` then the functions :math:`\mathbf{f}:\mathbb{R}^n\mapsto\mathbb{R}^m` are known as vector fields.
	* Example: :math:`f(x,y)=(x^2,\sin(y),x+y)`

**********************************************************
Continuity
**********************************************************
.. note::
	* We have a function :math:`\mathbf{f}`, from an open set :math:`E\in\mathbb{R}^n` into :math:`\mathbb{R}^m`.
	* A function is continuous at a point if each of its components, :math:`f_k(\mathbf{x})` is continuous at that point.

**********************************************************
Differentiation
**********************************************************
Directional Derivative as a rate of change in scalar fields
==============================================================
We have a function :math:`f`, from an open set :math:`E\in\mathbb{R}^n` into :math:`\mathbb{R}`. We want to find a proper definition of derivative of :math:`f` at some point :math:`\mathbf{x}\in E`.

.. note::
	* There is a single direction along which we can approach a point :math:`x\in\mathbb{R}`.
	* However, there are infinite directions along which we can approach a point :math:`\mathbf{x}\in\mathbb{R}^n`.
	* Along each such direction, the rate-of-change in the function can be different.
	* In order to apply the notion of single variable derivative, we can therefore reduce the function to a single dimensional one by looking at the slice along a particular line.
	* We fix our direction along some vector :math:`\mathbf{u}\in\mathbb{R}^n` and look at the rate-of-change of the function along :math:`\mathbf{u}` as we move closer to :math:`\mathbf{x}`.
	* For some :math:`h> 0`, we assume an open-ball around :math:`\mathbf{x}` of radius :math:`h\cdot||\mathbf{u}||`, and define the ratio

		.. math:: \frac{f(\mathbf{x}+h\cdot\mathbf{u})-f(\mathbf{x})}{h}
	* We define a version of derivative as :math:`f'(\mathbf{x}; \mathbf{u})=\lim\limits_{h\to 0}\frac{f(\mathbf{x}+h\cdot\mathbf{u})-f(\mathbf{x})}{h}`

.. attention::
	We note that the open ball in this case is essentially an equivalent of an one dimensional interval.

.. note::
	* If :math:`\mathbf{u}` happens to a unit-vector, then our open ball is :math:`B_h(\mathbf{x})`.
	* In this case, :math:`f'(\mathbf{x}; \mathbf{u})` is called the directional derivative along :math:`\mathbf{u}`.

Partial Derivative
------------------------------------------------------------
.. note::
	* If the unit vector in a directional derivative is along any of the coordinate-axes, such as :math:`\mathbf{e}_k`, the directional derivative is called a partial derivative.
	* Notation: :math:`D_k f(\mathbf{x})=f'(\mathbf{x}; \mathbf{e}_k)=\frac{\mathop{\partial}}{\mathop{\partial x_k}}f(\mathbf{x})`

Directional Derivative isn't sufficient
------------------------------------------------------------
.. warning::
	* A nice property of derivatives for single variable case is that if it exists at a given point, it implies that the function is continuous at that particular point.
	* HOWEVER, existence of direcitional derivatives doesn't imply continuity.

Example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. seealso::
	* We consider a scalar field 

		.. math:: f(x,y)=\begin{cases}\frac{xy^2}{x^2+y^4} & x\neq 0\\0 & x=0\end{cases}
	* We consider any arbitrary vector :math:`\mathbf{u}=(u_x,u_y)` where :math:`u_x\neq 0` and consider :math:`f'(x,y;\mathbf{u})` at :math:`\mathbf{0}`.

		.. math:: \frac{f(\mathbf{0}+h\mathbf{u})-f(\mathbf{0})}{h}=\frac{f(h\mathbf{u})}{h}=\frac{f(hu_x,hu_y)}{h}=\frac{hu_x(hu_y)^2}{h((hu_x)^2+(hu_y)^4)}=\frac{u_xu_y^2}{u_x^2+h^2u_y^4}
	* Therefore, :math:`f'(x,y;\mathbf{u})=\lim\limits_{h\to 0}\frac{u_xu_y^2}{u_x^2+h^2u_y^4}=\frac{u_y^2}{u_x}` which exists for all such :math:`\mathbf{u}`.
	* We now consider another vector :math:`\mathbf{v}=(0,v_y)` and consider :math:`f'(x,y;\mathbf{v})` at :math:`\mathbf{0}`.

		.. math:: \frac{f(\mathbf{0}+h\mathbf{v})-f(\mathbf{0})}{h}=\frac{f(h\mathbf{v})}{h}=\frac{f(0,hv_y)}{h}=0
	* Therefore, a directional derivative exists along every conceivable direction.

.. warning::
	* However, we note that along the parabolic path :math:`x=y^2`, :math:`f(x,y)=\frac{1}{2}`.
	* This means that if we move along this parabolic path, the value of the function jumps from :math:`\frac{1}{2}` to 0 at the origin all of a sudden.
	* No directional derivative along any straight line can catch this jump, as along that line, we can always form tiny open balls which excludes the points in the parabola.
	* Therefore, directional, and by extension, partial derivatives don't define a proper differentiation.

.. image:: ../../img/2.png
  :width: 400

Total Derivative as a linear approximation in general
==========================================================
We define the total derivative as a linear approximation of the function at close proximity of :math:`\mathbf{x}`.

.. note::
	* Instead of checking from a single direction, we need to consider all directions at once.
	* Therefore, we consider a variable length vector :math:`\mathbf{h}` which is allowed to rotate.
	* We consider the **open-hypersphere** :math:`B_\mathbf{h}(\mathbf{x})`, and assume that inside this, the function is approximately linear.
	* Therefore, we introduce a linear transform :math:`\mathbf{A}:\mathbb{R}^n\mapsto\mathbb{R}^m` to replace our original function :math:`\mathbf{f}:\mathbb{R}^n\mapsto\mathbb{R}^m`.
	* The **change in value** as we move from :math:`\mathbf{x}` to :math:`\mathbf{x}+\mathbf{h}` is

		* :math:`\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})` under the actual function.
		* :math:`\mathbf{A}(\mathbf{x}+\mathbf{h})-\mathbf{A}(\mathbf{x})=\mathbf{A}\mathbf{h}` under the approximation.
	* The error in this approximation is 

		.. math:: \boldsymbol{\epsilon}_\mathbf{x}(\mathbf{h})=\mathbf{f}(\mathbf{x}+\mathbf{h})-\mathbf{f}(\mathbf{x})-\mathbf{A}\mathbf{h}
	* We assume that :math:`\lim\limits_{\mathbf{h}\to\mathbf{0}}\frac{||\boldsymbol{\epsilon}_\mathbf{x}(\mathbf{h})||}{||\mathbf{h}||}=0` and define :math:`\mathbf{f}'(\mathbf{x})=\mathbf{A}`.

Gradient
------------------------------------------------------------
.. note::
	* If :math:`m=1`, then :math:`\mathbf{A}` is usually written as a column vector instead of a :math:`1\times n` matrix which is known as the gradient.

		.. math:: \nabla f(\mathbf{x}) =\begin{bmatrix}\frac{\mathop{\partial f(\mathbf{x})}}{\mathop{\partial x_1}}\\ \vdots \\ \frac{\mathop{\partial f(\mathbf{x})}}{\mathop{\partial x_n}}\end{bmatrix}
	* At any point :math:`\mathbf{x}`, the directional derivative along any :math:`\mathbf{v}` is given by

		.. math:: f'(\mathbf{x};\mathbf{v})=\nabla f(\mathbf{x})\cdot\mathbf{v}=\sum_{i=1}^n\frac{\mathop{\partial f(\mathbf{x})}}{\mathop{\partial x_i}}\cdot v_i
	* The total derivative operator :math:`D` in this case is the gradient operator

		.. math:: \nabla =\begin{bmatrix}\frac{\mathop{\partial}}{\mathop{\partial x_1}}\\ \vdots \\ \frac{\mathop{\partial}}{\mathop{\partial x_n}}\end{bmatrix}

Jacobian
------------------------------------------------------------
.. note::
	* If :math:`m> 1`, :math:`\mathbf{A}` is known as Jacobian matrix.

		.. math:: J_\mathbf{f}(\mathbf{x})=\begin{bmatrix}\nabla f_1(\mathbf{x})^\top\\ \vdots \\ \nabla f_m(\mathbf{x})^\top\end{bmatrix}=\begin{bmatrix}\frac{\mathop{\partial f_1(\mathbf{x})}}{\mathop{\partial x_1}} & \cdots & \frac{\mathop{\partial f_1(\mathbf{x})}}{\mathop{\partial x_n}} \\ \vdots & \vdots & \vdots \\ \frac{\mathop{\partial f_m(\mathbf{x})}}{\mathop{\partial x_1}} & \cdots & \frac{\mathop{\partial f_m(\mathbf{x})}}{\mathop{\partial x_n}}\end{bmatrix}

Differentiability : Continuously Differentiable Functions
===========================================================
.. warning::
	* Since we've established that the partial derivatives can exist at a point even when the function is not continuous at that point, let alone be differentiable, the existance of the gradient or the Jacobian doesn't imply that the function is differentiable at any point.

.. note::
	* The function is differentiable at :math:`\mathbf{x}` if all the partial derivatives exist and are **continuous** at :math:`\mathbf{x}`.
	* If the function is differentiable at :math:`\mathbf{x}`, it is continuous at :math:`\mathbf{x}`. All is good in the world again.

Properties
===========================================================
.. tip::
	* The sum, product and the chain rule works just as the single variable case.
	* The composition might be a bit complicated though. For example, we might have a composition like :math:`f\circ \mathbf{g}` where

		* :math:`\mathbf{g}` is a vector field, :math:`\mathbf{g}:\mathbb{R}^n\mapsto\mathbb{R}^m`
		* while :math:`f` is a scalar field, :math:`f:\mathbb{R}^m\mapsto\mathbb{R}`
	* So we'd be using a Jacobian matrix for :math:`\mathbf{g}` and a gradient for :math:`f`.

Higher Order Derivative
===========================================================
Higher Order Partial Derivative
------------------------------------------------------------
.. note::
	* We can partial derivatives of second order for functions, as 

		.. math:: D_k^2f(\mathbf{x})=\frac{\partial^2}{\mathop{\partial x_k^2}}f(\mathbf{x})=\frac{\partial}{\mathop{\partial x_k}}\left(\frac{\partial}{\mathop{\partial x_k}}f(\mathbf{x})\right)
	* We can also have mixed partial derivatives, as

		.. math:: D_{i,j}f(\mathbf{x})=D_i (D_j f(\mathbf{x}))=\frac{\partial^2}{\mathop{\partial x_i}\mathop{\partial x_j}}f(\mathbf{x})=\frac{\partial}{\mathop{\partial x_i}}\left(\frac{\partial}{\mathop{\partial x_j}}f(\mathbf{x})\right)

.. warning::
	* In general :math:`D_{i,j}f(\mathbf{x})\neq D_{j,i}f(\mathbf{x})`

.. attention::
	* We assume that :math:`D_i` and :math:`D_j` exist.
	* If :math:`D_{i,j}` and :math:`D_{j,i}` are both continuous at a point :math:`\mathbf{p}`, then :math:`D_{i,j}f(\mathbf{p})= D_{j,i}f(\mathbf{p})`
	* If either of :math:`D_{i,j}` and :math:`D_{j,i}` are contibuous, then the other is also continuous.
	* This is a sufficient condition, not a necessary one.

Higher Order Total Derivative
------------------------------------------------------------
Hessian
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* The gradient of a scalar field :math:`f:\mathbb{R}^n\mapsto\mathbb{R}` at any point in :math:`\mathbf{x}` is a vector field on :math:`\mathbf{x}`

		.. math:: \nabla f:\mathbf{R}^n\mapsto\mathbf{R}^n
	* Therefore, the total derivative of second order is given by the Jacobian :math:`\mathbf{J}(\nabla f(\mathbf{x}))`
	* The Hessian matrix is defined as 

		.. math:: \mathbf{H}(\mathbf{x})=\mathbf{J}(\nabla f(\mathbf{x}))^\top
	* We have the :math:`D_1^2,\cdots,D_n^2` on the diagonal and partial derivatives elsewhere.
	* The matrix is symmetric depending on the equality of partial derivatives.

Laplacian
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* The Laplacian operator is defined as

		.. math:: \Delta f=\nabla^2f=\nabla\cdot\nabla f
	* We note that :math:`\Delta f(\mathbf{x})=\text{trace}({\mathbf{H}(\mathbf{x})})`

Application
===========================================================
Normal vector to level sets
------------------------------------------------------------
Level sets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* Set of :math:`\mathbf{x}` where the value of the function is constant.

		.. math:: L(c) = \{\mathbf{x}\mathop{|} f(\mathbf{x})=c \}
	* Level curve for :math:`f:\mathbb{R}^2\mapsto\mathbb{R}` (represented by lines in a contour plot)
	* Level surface for :math:`f:\mathbb{R}^3\mapsto\mathbb{R}`

.. attention::
	* The gradient vector of the scalar field at any point :math:`\mathbf{a}` is perpendicular to the tangent vector at the same point on the level curve :math:`L(f(\mathbf{a}))`.

Local extremum
------------------------------------------------------------
.. note::
	We note that extremum makes sense only for scalar fields.

.. attention::
	Second order Taylor approximation for a scalar field :math:`f` at a point :math:`\mathbf{x}`

	.. math:: f(\mathbf{x}+\mathbf{h})=f(\mathbf{x})+\nabla f(\mathbf{x})\cdot\mathbf{h}+\frac{1}{2!}\left(\mathbf{h}\cdot H\mathbf{x}\cdot\mathbf{h}^\top\right)+\boldsymbol{\epsilon}_\mathbf{x}(\mathbf{h})

First Derivative Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	At a critical point :math:`\mathbf{c}\in E\subset\mathbf{R}^n`, we have :math:`\nabla f(\mathbf{c})=\mathbf{0}`.

Second Derivative Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* For a minimum, the Hessian matrix :math:`\mathbf{H}(\mathbf{c})` is positive definite.
	* For a maximum, the Hessian matrix :math:`\mathbf{H}(\mathbf{c})` is negative definite.
	* If the Hessian matrix :math:`\mathbf{H}(\mathbf{c})` is neither, then it is a saddle point.

************************************************************
Matrix Calculus: Tricks and Useful Results
************************************************************
.. note::
	* We can have a 

		* dependent quantity in scalar (:math:`y`), vector (:math:`\mathbf{y}`) or matrix (:math:`\mathbf{Y}`) form and an 
		* independent variable in scalar (:math:`x`), vector (:math:`\mathbf{x}`) or matrix form (:math:`\mathbf{X}`).
	* We can think about the derivatives in this case as the limiting ratio of the changes in components for the dependent variable in response to a tiny nudge in the components of the independent one.

.. csv-table:: Table for derivatives
	:align: center

	:math:`\frac{\partial y}{\mathop{\partial x}}`, :math:`\frac{\partial \mathbf{y}}{\mathop{\partial x}}`, :math:`\frac{\partial \mathbf{Y}}{\mathop{\partial x}}`
	:math:`\frac{\partial y}{\mathop{\partial \mathbf{x}}}`, :math:`\frac{\partial \mathbf{y}}{\mathop{\partial \mathbf{x}}}`, :math:`\frac{\partial \mathbf{Y}}{\mathop{\partial \mathbf{x}}}`
	:math:`\frac{\partial y}{\mathop{\partial \mathbf{X}}}`, :math:`\frac{\partial \mathbf{y}}{\mathop{\partial \mathbf{X}}}`, :math:`\frac{\partial \mathbf{Y}}{\mathop{\partial \mathbf{X}}}`

.. tip::
	* In any case, we can stick to the `numerator layout notation <https://en.wikipedia.org/wiki/Matrix_calculus#Numerator-layout_notation>`_ - where the number of rows in the derivative would be the same as the number of rows in the numerator (or, the output dimension as we think of them as functions of the independent variables).
	* We can take the differential operators in the transposed order of the denominator in each case.

		* Let a function :math:`\mathbf{f}:\mathbb{R}^2\mapsto\mathbb{R}^3` be defined as

			.. math:: \mathbf{f}(x,y)=\begin{bmatrix}x^2e^y\\ \log(x)\\ y-\cos(x)\end{bmatrix}
		* We wish to compute :math:`\frac{\partial \mathbf{f}}{\mathop{\partial \mathbf{r}}}` where :math:`\mathbf{r}=\begin{bmatrix}x\\ y\end{bmatrix}=(x,y)^T`
		* To follow numerator layout notation, we transpose :math:`\mathbf{r}` and take the differential operator in the row format

			.. math:: \frac{\partial}{\mathop{\partial\mathbf{r}}}=\begin{bmatrix}\frac{\partial}{\mathop{\partial x}} & \frac{\partial}{\mathop{\partial y}}\end{bmatrix}
	* We can then perform Kronecker product of the operator and operand.

		* For the example, it then becomes

			.. math:: \frac{\partial\mathbf{f}}{\mathop{\partial\mathbf{r}}}=\begin{bmatrix}\frac{\partial}{\mathop{\partial x}} & \frac{\partial}{\mathop{\partial y}}\end{bmatrix}\otimes \begin{bmatrix}x^2e^y\\ \log(x)\\ y-\cos(x)\end{bmatrix}=\begin{bmatrix}\frac{\partial}{\mathop{\partial x}}(x^2e^y) & \frac{\partial}{\mathop{\partial y}}(x^2e^y)\\ \frac{\partial}{\mathop{\partial x}}(\log(x)) & \frac{\partial}{\mathop{\partial y}}(\log(x))\\ \frac{\partial}{\mathop{\partial x}}(y-\cos(x)) & \frac{\partial}{\mathop{\partial y}}(y-\cos(x))\end{bmatrix}=\begin{bmatrix}2xe^y&x^2e^y\\ 1/x&0\\\sin(x)&1\end{bmatrix}

Useful Derivatives
===========================================================
.. csv-table:: Useful derivatives
	:header: "Variable", "Scalar", "Vector", "Matrix", "Denominator Layout", "Numerator Layout"
	:align: center

	:math:`x`, :math:`x`, , , :math:`1`, :math:`1`
	:math:`x`, :math:`ax`, , , :math:`a`, :math:`a`
	:math:`x`, :math:`x^2`, , , :math:`2x`, :math:`2x`
	:math:`x`, :math:`ax^2`, , , :math:`2ax`, :math:`2ax`
	:math:`x`, :math:`(ax)^2`, , , :math:`2a^2x`, :math:`2a^2x`
	:math:`\mathbf{x}`, , :math:`\mathbf{x}`, , :math:`\mathbb{I}`, :math:`\mathbb{I}`
	:math:`\mathbf{x}`, :math:`\mathbf{x}^T\mathbf{a}=\mathbf{a}^T\mathbf{x}`, , , :math:`\mathbf{a}`,:math:`\mathbf{a}^T`
	:math:`\mathbf{x}`, :math:`\mathbf{x}^T\mathbf{x}=||\mathbf{x}||_2^2`, , , :math:`2\mathbf{x}`,:math:`2\mathbf{x}^T`
	:math:`\mathbf{x}`, :math:`\mathbf{x}^T\mathbf{A}\mathbf{x}`, , , :math:`(\mathbf{A}+\mathbf{A}^T)\mathbf{x}`,:math:`\mathbf{x}^T(\mathbf{A}+\mathbf{A}^T)`
	:math:`\mathbf{x}`, :math:`\mathbf{x}^T\mathbf{B}^T\mathbf{A}\mathbf{x}=(\mathbf{B}\mathbf{x})^T(\mathbf{A}\mathbf{x})`, , , :math:`(\mathbf{B}^T\mathbf{A}+\mathbf{A}^T\mathbf{B})\mathbf{x}`, :math:`\mathbf{x}^T(\mathbf{B}^T\mathbf{A}+\mathbf{A}^T\mathbf{B})`
	:math:`\mathbf{x}`, :math:`\mathbf{x}^T\mathbf{A}^T\mathbf{A}\mathbf{x}=||\mathbf{A}\mathbf{x}||_2^2`, , , :math:`2\mathbf{A}^T\mathbf{A}\mathbf{x}`, :math:`2\mathbf{x}^T\mathbf{A}^T\mathbf{A}`
	:math:`\mathbf{x}`, , :math:`\mathbf{A}\mathbf{x}`, , :math:`\mathbf{A}^T`,:math:`\mathbf{A}`
	:math:`\mathbf{x}`, , , :math:`\mathbf{x}\mathbf{x}^T`, :math:`\mathbf{x}\otimes\mathbb{I}+\mathbb{I}\otimes\mathbf{x}`, 
	:math:`\mathbf{X}`, , ,:math:`\mathbf{X}`, :math:`\mathbb{I}\otimes\mathbb{I}`, :math:`\mathbb{I}\otimes\mathbb{I}`
	:math:`\mathbf{X}`, , :math:`\mathbf{X}\mathbf{a}`, , :math:`\mathbf{a}^T\otimes\mathbb{I}`, 
	:math:`\mathbf{X}`, :math:`\mathbf{a}^T\mathbf{X}\mathbf{b}=\mathbf{b}^T\mathbf{X}^T\mathbf{a}`, , , :math:`\mathbf{a}\mathbf{b}^T`, :math:`\mathbf{b}\mathbf{a}^T`
	:math:`\mathbf{X}`, :math:`\mathbf{a}^T\mathbf{X}^T\mathbf{b}=\mathbf{b}^T\mathbf{X}\mathbf{a}`, , , :math:`\mathbf{b}\mathbf{a}^T`, :math:`\mathbf{a}\mathbf{b}^T`
	:math:`\mathbf{X}`, :math:`\mathbf{b}^T\mathbf{X}^T\mathbf{X}\mathbf{a}=(\mathbf{X}\mathbf{b})^T(\mathbf{X}\mathbf{a})`, , , :math:`\mathbf{X}(\mathbf{a}\mathbf{b}^T+\mathbf{b}\mathbf{a}^T)`, :math:`(\mathbf{a}\mathbf{b}^T+\mathbf{b}\mathbf{a}^T)\mathbf{X}^T`

.. seealso::
	* Plethora of useful results: `Matrix Cookbook <https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf>`_
	* `The Matrix Calculus You Need For Deep Learning <https://arxiv.org/abs/1802.01528>`_
	* `matrixcalculus.org <https://www.matrixcalculus.org/>`_

**********************************************************
Integration
**********************************************************
Fubini's Theorem
===========================================================
For double integral of a function :math:`f(x,y)` in a rectangular region :math:`R=[a,b]\times [c,d]` and :math:`\iint\limits_{R} \left|f(x,y)\right|\mathop{dx} \mathop{dy}<\infty`, we can compute it using iterated integrals as follows:

	.. math:: \iint\limits_{R} f(x,y)\mathop{dx} \mathop{dy}=\int\limits_a^b \left(\int\limits_c^d f(x,y)\mathop{dy}\right)\mathop{dx}=\int\limits_c^d \left(\int\limits_a^b f(x,y)\mathop{dx}\right)\mathop{dy}

Gaussian Integral using Polar Substitute
===========================================================
.. note::
	* Let :math:`I=\int\limits_{-\infty}^\infty e^{-x^2}\mathop{dx}`. 
	* Try to compute :math:`I^2`, convert this into a double integral using Fubini's theorem.

		.. math:: I^2=\left(\int\limits_{-\infty}^\infty e^{-x^2}\mathop{dx}\right)\left(\int\limits_{-\infty}^\infty e^{-y^2}\mathop{dy}\right)=\iint_{\mathbb{R}^2}e^{-(x^2+y^2)}\mathop{dx}\mathop{dy}
	* Use polar co-ordinate transform, :math:`x=r\cos(\theta)` and :math:`y=r\sin(\theta)`.
	* To substitute the differentials,

		* We assume a small tiny rectangular region, starting at :math:`(x,y)` in the original space spanned by tiny sides :math:`\mathop{dx}` and :math:`\mathop{dy}`.
		* In polar system, the rectangle is a distnace of :math:`r` away from origin, and it can be approximated by the region of sides :math:`r\mathop{d\theta}` and :math:`\mathop{dr}`.
		* Therefore, the area of the tiny region, :math:`\mathop{dA}=\mathop{dx}\mathop{dy}=r\mathop{dr}\mathop{d\theta}`.
		* For the limits, :math:`r` varies from 0 to :math:`\infty` and :math:`\theta` varies from 0 to :math:`2\pi`.
	* Therefore, we have 

		.. math:: I^2=\int_0^{2\pi}\left(\int_0^\infty e^{-r^2}r\mathop{dr}\right)\mathop{d\theta}=\int_0^{2\pi}\left(\frac{1}{2}\int_\infty^0 e^t\mathop{dt}\right)\mathop{d\theta}=\int_0^{2\pi}\left(\frac{1}{2}\left[e^t\right]_\infty^0\right)\mathop{d\theta}=\frac{1}{2}\int_0^{2\pi}\mathop{d\theta}=\pi
	* So :math:`I=\sqrt{\pi}`.

Useful Resources
===========================================================
.. seealso::
	* Different ways for evaluating the Gaussian integral: `YouTube video playlist by Dr Peyam <https://www.youtube.com/watch?v=HcneBkidSDQ&list=PLJb1qAQIrmmCgLyHWMXGZnioRHLqOk2bW>`_.
