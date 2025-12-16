########################################################################################
Optimisation
########################################################################################
****************************************************************************************
Convexity
****************************************************************************************
Convex Set
========================================================================================
.. note::
	* We consider a set :math:`A\subseteq\mathcal{X}` where :math:`\mathcal{X}` is a vector space.
	* If we connect any two points, :math:`\mathbf{x},\mathbf{y}\in A`, by a line segment, then all the points in that line should also be in the set :math:`A`.
	* More formally, for any :math:`0\leq\alpha\leq 1`,

		.. math:: \alpha\mathbf{x}+(1-\alpha)\mathbf{y}\in A

Convex Function
========================================================================================
.. note::
	* We consider of a function :math:`f:\mathcal{X}\mapsto\mathcal{Y}`.
	* If :math:`A\subseteq\mathcal{X}` is a convex subset, then its image, :math:`f(A)` also forms a convex subset in :math:`\mathcal{Y}`.
	* Formally, for any :math:`0\leq\alpha\leq 1`,

		.. math:: f(\alpha\mathbf{x}+(1-\alpha)\mathbf{y})=\alpha f(\mathbf{x})+(1-\alpha)f(\mathbf{y})

****************************************************************************************
Convex Optimisation
****************************************************************************************
.. note::
	* The functions we're dealing with are of the form :math:`f(\mathbf{x}):\mathbb{R}^d\mapsto\mathbb{R}`
	* Taylor expansion of the function around a fixed point :math:`\mathbf{x}_0\in\mathbb{R}^d` if the function is infinitely differentiable

		.. math:: f(\mathbf{x})=f(\mathbf{x}_0)+\langle\nabla_f(\mathbf{x}_0), (\mathbf{x}-\mathbf{x}_0)\rangle+\frac{1}{2!}(\mathbf{x}-\mathbf{x}_0)^T\nabla^2_f(\mathbf{x}_0)(\mathbf{x}-\mathbf{x}_0)+\cdots
	* We use the notation :math:`\mathbf{g}_0:=\nabla_f(\mathbf{x}_0)\in\mathbb{R}^d` for the gradient vector evaluated at :math:`\mathbf{x}_0` and :math:`\mathbf{H}_0:=\nabla^2_f(\mathbf{x}_0)\in:\mathbb{R}^{d\times d}` for the Hessian matrix evaluated at :math:`\mathbf{x}_0`.
	* The Taylor expansion is then written as

		.. math:: f(\mathbf{x})=f(\mathbf{x}_0)+\mathbf{g}_0^T(\mathbf{x}-\mathbf{x}_0)+\frac{1}{2!}(\mathbf{x}-\mathbf{x}_0)^T\mathbf{H}_0(\mathbf{x}-\mathbf{x}_0)+\cdots

****************************************************************************************
Unconstrained Optimisation
****************************************************************************************
.. note::
	* We're interested in finding the minimum :math:`\min_{\mathbf{x}\in\mathbb{R}^d}f(\mathbf{x})`.

First-order Methods
========================================================================================
.. note::
	* First-order methods use the first-order Taylor's approximation
	* It is assumed that the function :math:`f(\mathbf{x})` behaves locally linear around a point :math:`\mathbf{x}\in\mathbb{R}^d` and therefore can be approximated by

		.. math:: f(\mathbf{x})\approx f(\mathbf{x}_0)+\mathbf{g}_0^T(\mathbf{x}-\mathbf{x}_0)

Gradient Descent
----------------------------------------------------------------------------------------
.. note::
	* [TODO: proof] The direction of the gradient gives the direction of steepest ascent (i.e. the opposite of gradient provides the direction of steepest descent).
	* We start with an abritrary starting point :math:`\mathbf{x}_t=\mathbf{x}_0\in\mathbb{R}^d`.
	* We take a small step along the direction of the gradient as

		.. math:: \mathbf{x}_{t+1}=\mathbf{x}_t-\eta\mathbf{g}_t
	* Here, the scalar :math:`\eta>0` is a parameter that determines the stepsize.

Code example for Linear Regression
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. code-block:: python

	import numpy as np
	import matplotlib.pyplot as plot
	import pandas as pd
	import seaborn as seaborn
	
	# create the function as linear with random normal noise
	def define_function(d):
		return np.random.randn(d)

	def create_dataset(w, noise_sigma, N=1000):
		d = w.shape[0]
		X = [np.random.rand(d).tolist() for i in np.arange(N)] # N rows and d columns
		return pd.DataFrame([(*x, w.dot(x) + np.random.randn() * noise_sigma) for x in X])

	def compute_loss(X, y, wt):
		return np.linalg.norm(y-X*wt)

	def compute_gradient(X, y, wt):
		return -2*X.T*(y-X*wt)

	def gradient_descent(X, y, lr=0.0001, eps=1e-5, max_iter=100):
		wt = np.matrix(np.random.randn(X.shape[1],1))
		loss = compute_loss(X, y, wt)
		i = 0
		print(f'iter={i}')
		print(f'wt={wt}')
		print(f'loss={loss}')
		loss_values = []
    
		while loss > eps and i < max_iter:
			print(f'iter={i}')
			g = compute_gradient(X, y, wt)
			wt = wt - lr*g
			loss = compute_loss(X, y, wt)
			i = i+1
			print(f'wt={wt}')
			print(f'loss={loss}')
			loss_values.append([loss])
        
		return wt, loss_values

	w = define_function(2)
	df = create_dataset(w, noise_sigma=0.01, N=1000)
	X = np.asarray(df.iloc[:,:2])
	y = np.asarray(df.iloc[:,2])

	# direct estimator from least square
	w_hat = (np.linalg.inv(X.T * X)) * X.T * y

	X = np.asmatrix(X)
	y = np.asmatrix(y).T
	w_gd, loss_values = gradient_descent(X, y, lr=0.001, eps=1e-5, max_iter=50)

	plot.plot(np.arange(len(loss_values)), loss_values)
	plot.show()

Accelerated Gradient Descent
----------------------------------------------------------------------------------------
.. note::
	`Nesterov Accelerated Gradient Descent <https://jlmelville.github.io/mize/nesterov.html>`_

Second-order Methods
========================================================================================
Newton's Method
----------------------------------------------------------------------------------------
.. note::
	* Originally developed for finding roots of equations :math:`f(x)=0`.
	* We start with an abritrary starting point :math:`x_t=x_0\in\mathbb{R}`.
	* We compute the gradient and obtain the point where the tangent line of :math:`f` at :math:`x_t` equals 0. 
	* We use this point as the next iteration.

		.. math:: 0=f(x_t)+g(x_t)(x_{t+1}-x_t)\implies x_{t+1}=x_t-\frac{f(x_t)}{g(x_t)}
	* This can be used for minimizing a function :math:`f` as well by finding roots of :math:`\nabla_f(x)=0`.
	* For a function :math:`f:\mathbb{R}^d\mapsto\mathbb{R}`, the iteration rule becomes

		.. math:: \mathbf{0}=\mathbf{g}_t+\mathbf{H}_t(\mathbf{x}_{t+1}-\mathbf{x}_t)\implies \mathbf{x}_{t+1}=\mathbf{x}_t-\mathbf{H}_t^{-1}\mathbf{g}_t
	* It approximates the functional locally (around :math:`\mathbf{x}_t`) by a quadratic function.

.. tip::
	* Here the learning rate is not required. The rate is implied automatically by the geometric behaviour of :math:`\mathbf{H}_t` at every :math:`\mathbf{x}_t`.
	* If :math:`\mathbf{H}_t` is symmetric positive definite, the inverse always exists and we can investigate the eigenvalues to find out the step-size across each dimension

		.. math:: \mathbf{H}_t=\mathbf{Q}^T\boldsymbol{\Lambda}\mathbf{Q}\implies \mathbf{x}_{t+1}=\mathbf{x}_t-\mathbf{Q}^T\boldsymbol{\Lambda}^{-1}\mathbf{Q}\mathbf{g}_t
	* If the original function is quadratic, this method finds the minima in 1 step (TODO: prove)

Code example for Linear Regression
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. note::
	* For Linear Regression, since the function is quadratic in its parameter, Newton's method finds the minima in exactly 1 step.
	* TODO: prove why?

.. code-block:: python

	def compute_loss(X, y, wt):
		return np.linalg.norm(y-X*wt)

	def compute_gradient(X, y, wt):
		return -2*X.T*(y-X*wt)

	def compute_hessian(X):
		return 2*X.T*X

	def newton_method(X, y, eps=1e-5, max_iter=5):
		wt = np.matrix(np.random.randn(X.shape[1],1))
		loss = compute_loss(X, y, wt)
		i = 0
		print(f'iter={i}')
		print(f'wt={wt}')
		print(f'loss={loss}')
		loss_values = []
    
		while loss > eps and i < max_iter:
			print(f'iter={i}')
			g = compute_gradient(X, y, wt)
			H = compute_hessian(X)
			wt = wt - np.linalg.inv(H)*g
			loss = compute_loss(X, y, wt)
			i = i+1
			print(f'wt={wt}')
			print(f'loss={loss}')
			loss_values.append([loss])
        
		return wt, loss_values

	w_newt, loss_values_newt = newton_method(X, y, eps=1e-5, max_iter=2)
	plot.plot(np.arange(len(loss_values_newt)), loss_values_newt)
	plot.show()

****************************************************************************************
Constrained Optimisation
****************************************************************************************
.. note::
	* We're interested in finding the minimum :math:`\min_{\mathbf{x}\in S\subseteq \mathbb{R}^d}f(\mathbf{x})`.

****************************************************************************************
Learning Resources
****************************************************************************************
.. note::
	* `[convexoptimization.com] <https://convexoptimization.com/>`_
	* `Convex Optimization Playlist by Visully Explained <https://www.youtube.com/playlist?list=PLqwozWPBo-FuPu4d9pFOobsCF1vDGdY_I>`_
