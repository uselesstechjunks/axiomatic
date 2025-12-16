################################################################################
Parametric Point Estimation
################################################################################

********************************************************************************
Classical Infernece
********************************************************************************

Method of Moments Estimator (MOM)
================================================================================
.. note::
	* Let the parameter vector be :math:`\boldsymbol{\theta}=(\theta_1,\cdots,\theta_k)`.
	* Let the estimator be :math:`\widehat{\Theta}_n=(\widehat{\theta_1},\cdots,\widehat{\theta_k})`.
	* Let :math:`\alpha_j=\alpha_j({\boldsymbol{\theta}})=\mathbb{E}_{\boldsymbol{\theta}}[X^j]=\int x^j\mathop{dF_{\boldsymbol{\theta}}}(x)` for :math:`1\leq j\leq k`.
	* We assume that the moments exist and can be expressed in closed form as equations involving the parameters :math:`\theta_j`.
	* Estimate moments with sample moments as

		.. math:: \widehat{\alpha_j}({\boldsymbol{\theta}})=\alpha(\widehat{\Theta}_n)=\frac{1}{n}\sum_{i=1}^n X_i^j
	* We'd have a system of equations k equations with k unknowns involving :math:`(\widehat{\theta}_j)_{j=1}^k`.

Properties
--------------------------------------------------------------------------------
.. seealso::
	* **Consistent**: :math:`\widehat{\Theta}_n\xrightarrow[]{P}\boldsymbol{\theta}`
	* **Asymptotically normal**:

		* TODO write expression

Common Estimators
--------------------------------------------------------------------------------

Bernoulli
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* We have samples :math:`X=(X_1,\cdots,X_n)` from a Bernoulli with unknown :math:`p`.
	* :math:`\widehat{\alpha_0}=p=\frac{1}{n}\sum_{i=1}^n X_i`.

Normal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* We have samples :math:`X=(X_1,\cdots,X_n)` from a Normal with unknown :math:`\mu,\sigma`.
	* :math:`\widehat{\alpha_0}=\mu=\frac{1}{n}\sum_{i=1}^n X_i`.
	* :math:`\widehat{\alpha_1}=\mu^2+\sigma^2=\frac{1}{n}\sum_{i=1}^n X^2_i`.

Maximum Likelihood Estimator (MLE)
================================================================================

Likelihood function
--------------------------------------------------------------------------------
.. note::
	* We assume that we have samples of size :math:`n`, :math:`X=(X_1,\cdots,X_n)` such that :math:`X_i\sim f_{X_i}(x_i; \theta)`.
	* Likelihood function is defined as :math:`\mathcal{L}_n(\theta)=f_X(x; \theta)=f_{X_1,\cdots,X_n}(x_1,\cdots,x_n;\theta)`.
	
.. warning::
	* Given a particular observation :math:`X=x=(x_1,\cdots,x_n)`, the function :math:`\mathcal{L}_n(\theta)=f_X(x; \theta)` is no longer a density, but just a function of :math:`\theta`.
	* For discrete case, :math:`\mathcal{L}_n(\theta)=p_X(x; \theta)=\mathbb{P}(X_1=x_1,\cdots,X_n=x_n;\theta)`.

		* This is the probability that the observation would match current data under a particular :math:`\theta`.
		* If this probability is higher when :math:`\theta=\theta_i` compared to :math:`\theta=\theta_j`, it is more likely that the underlying parameter has value :math:`\theta_i`.

.. note::
	We estimate :math:`\widehat{\Theta}_n=\widehat{\Theta}_{\text{ML}}=\mathop{\underset{\theta}{\mathrm{argmax}}}\mathcal{L}(\theta)`.
	
Log likelihood
--------------------------------------------------------------------------------
	* Independence assumption:

		.. math:: \mathcal{L}_n(\theta)=f_{X_1,\cdots,X_n}(x_1,\cdots,x_n;\theta)=\prod_{i=1}^n f_{X_i}(x_i;\theta)	

	* Identical distribution assumption: 

		.. math:: \mathcal{L}_n(\theta)=f_{X_1,\cdots,X_n}(x_1,\cdots,x_n;\theta)=\prod_{i=1}^n f_X(x_i;\theta)
	* Log likelihood is defined as

		.. math:: \mathcal{l}_n(\theta)=\log{\mathcal{L}(\theta)}=\sum_{i=1}^n \log(f_X(x_i;\theta))
	* As log is a monotonic increasing function

		.. math:: \mathop{\underset{\theta}{\mathrm{argmax}}}\mathcal{l}_n(\theta)=\mathop{\underset{\theta}{\mathrm{argmax}}}\mathcal{L}_n(\theta)

Properties
--------------------------------------------------------------------------------
.. note::
	* **Consistent**: :math:`\widehat{\Theta}_{\text{ML}}\xrightarrow[]{P}\theta`.

		* Proof Hint: Involve KL distance between the true value of :math:`\theta`, :math:`\theta_{\text{true}}` and any arbitrary :math:`\theta`.

			* The likelihood function with the true value :math:`l_n(\theta_{\text{true}})` evaluates to a constant.
			* Maximising :math:`l_n(\theta)` is the same as maximising 

				.. math:: M_n(\theta)=\frac{1}{n}\left(l_n(\theta)-l_n(\theta_{\text{true}})\right)=\frac{1}{n}\sum_{i=1}^n\log\left(\frac{f_X(x_i;\theta)}{f_X(x_i;\theta_{\text{true}})}\right)	
			* Let :math:`M(\theta)` be defined as the expectation of this rv

				.. math:: M(\theta)=\mathbb{E}_{\theta_\text{true}}\left[\log\left(\frac{f_X(x;\theta)}{f_X(x;\theta_{\text{true}})}\right)\right]=\int\log\left(\frac{f_X(x;\theta)}{f_X(x;\theta_{\text{true}})}\right)f_X(x;\theta_{\text{true}})\mathop{dx}=-D_{KL}(\theta_{\text{true}},\theta)
			* Maximum value of :math:`M(\theta)` is 0.
			* For all :math:`\theta`, :math:`M_n(\theta)\xrightarrow[]{P}M(\theta)`
			* Technically, we need uniform convergence to prove this formally.
	* **Equivariant**: If :math:`\widehat{\Theta}_{\text{ML}}` is the MLE for :math:`\theta`, then :math:`g(\widehat{\Theta}_{\text{ML}})` is the MLE for :math:`g(\theta)`.

		* TODO proof
	* **Asymptotically normal**: :math:`\frac{\widehat{\Theta}_{\text{ML}}-\theta}{\widehat{\text{se}}}\xrightarrow[]{D}\mathcal{N}(0,1)`

		* Score function: :math:`s(X;\theta)=\frac{\partial}{\partial\theta}\log f(X;\theta)`
		* Fisher information: :math:`I_n(\theta)=\mathbb{V}_\theta\left(\sum_{i=1}^n s(X_i;\theta)\right)=\sum_{i=1}^n\mathbb{V}_\theta\left(s(X_i;\theta)\right)`
	* **Asymptotically optimal**: Estimator has least variance for large sample size.

		* TODO proof

Computing CI for MLE
--------------------------------------------------------------------------------

Common Estimators
--------------------------------------------------------------------------------

Bernoulli
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Uniform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Binomial
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Geometric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multinomial
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exponential
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Iterative Method of Computation
--------------------------------------------------------------------------------
.. note::
	* For complicated or composite rvs, computation of likelihood in a closed form might be challenging. 
	* We can approximate MLE estimates by iterative methods.

Newton Raphson
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* We gather an initial estimate as a starting point, :math:`\theta'`.

		* MOM can give us a good starting point.
	* We assume that the true optimal value :math:`\theta^*` lie in the vicinity of this initial guess.
	* We apply first order taylor approximation

The EM Algorithm
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* TODO add more details
	* Assume hidden variables - likelihood computation is easier for joint

********************************************************************************
Bayesian Inference
********************************************************************************

Maximum A Posterior Estimator (MAP)
================================================================================

Common Estimators
--------------------------------------------------------------------------------

Bernoulli
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Minimum Mean Squared Error Estimator (MMSE)
================================================================================
