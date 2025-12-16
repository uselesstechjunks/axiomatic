##########################################################################################
Functions of Random Variable
##########################################################################################

******************************************************************************************
Density of a function of a rv
******************************************************************************************
Let :math:`Y=g(X)` be a function of an rv :math:`X`.

.. note::
	* If :math:`X` is discrete, this is discussed in the random variable section (TODO: add hyperlink)
	* If :math:`X` is continuous with a PDF :math:`f_X(x)`, then the process for finding :math:`f_Y(y)` is as follows:

		* Compute the CDF as

			.. math:: F_Y(y)=\mathbb{P}(Y\leq y)=\mathbb{P}(g(X)\leq y)=\int\limits_{\{x|g(x)\leq y\}}f_X(x) \mathop{dx}
		* Compute the PDF as :math:`f_Y(y)=F'_Y(y)`.

.. tip::
	* Some effort is required to compute the set :math:`\{x|g(x)\leq y\}`.
	* Find :math:`f_Y(y)` where :math:`Y=X^2`.

Special cases
========================================================================
Linear functions
------------------------------------------------------------------------
Let :math:`Y=g(X)=aX+b`.

.. tip::
	* If :math:`a=0`, then :math:`Y=b` with probability 1 and it's no longer a continuous rv.
	* If :math:`a\neq 0`, then we have

		.. math:: F_Y(y)=\mathbb{P}(Y\leq y)=\mathbb{P}(g(X)\leq y)=\mathbb{P}(aX+b\leq y)=\begin{cases}\mathbb{P}\left(X\leq\frac{y-b}{a}\right) & \text{if $a>0$} \\ \mathbb{P}\left(X\geq\frac{y-b}{a}\right) & \text{if $a<0$}\end{cases}=\begin{cases}F_X(\frac{y-b}{a}) & \text{if $a>0$} \\ 1-F_X(\frac{y-b}{a}) & \text{if $a<0$}\end{cases}
	* We can recover the PDF in both cases as

		.. math:: f_Y(y)=\begin{cases}\frac{1}{a}f_X(\frac{y-b}{a}) & \text{if $a>0$} \\ -\frac{1}{a}f_X(\frac{y-b}{a}) & \text{if $a<0$}\end{cases}=\frac{1}{\left| a \right|}f_X(\frac{y-b}{a})

Monotonic functions
------------------------------------------------------------------------
.. note::
	* If :math:`g(y)=x` is a monotonic function, then it has an inverse, :math:`x=g^{-1}(y)`.
	* Therefore, we have

		.. math:: F_Y(y)=\mathbb{P}(Y\leq y)=\mathbb{P}(g(X)\leq y)=\begin{cases}\mathbb{P}(X\leq g^{-1}(y)) & \text{if $g(X)$ is monotonic increasing}\\\mathbb{P}(X\geq g^{-1}(y)) & \text{if $g(X)$ is monotonic decreasing}\end{cases}=\begin{cases}F_X(g^{-1}(y)) & \text{if $g(X)$ is monotonic increasing}\\1-F_X(g^{-1}(y)) & \text{if $g(X)$ is monotonic decreasing}\end{cases}
	* We can recover the PDF in both cases as

		.. math:: f_Y(y)=|f_X(g^{-1}(y))|\cdot\frac{\mathop{d}}{\mathop{dy}}\left[g^{-1}(y)\right]
	* We note that the linear case is a special case of monotonic functions.

******************************************************************************************
Density of a function of multiple jointly distributed rvs
******************************************************************************************
Let :math:`Z=g(X,Y)` be a function of 2 jointly distributed rvs, :math:`X` and :math:`Y`. In this case, we follow the same process as before.

.. tip::
	* Compute the CDF as

		.. math:: F_Z(z)=\mathbb{P}(Z\leq z)=\mathbb{P}(g(X,Y)\leq z)=\iint\limits_{\{(x,y)|g(x,y)\leq z\}}f_{X,Y}(x,y)\mathop{dx}\mathop{dy}
	* Compute the PDF as :math:`f_Z(z)=F'_Z(z)`.
	* Extends naturally for more than 2 rvs.

.. seealso::
	* Find the PDF of :math:`Z=X/Y`, where :math:`X` and :math:`Y` are independent and uniformly distributed in :math:`[0,1]`.
	* Two people join a call but they are late by an amount, independent of the other, that follows an exponential distribution with parameter :math:`\lambda`. Find the PDF of the difference in their joining time.

Special cases
========================================================================
Sum of independent rvs: Convolution
------------------------------------------------------------------------
We want the PDF (or PMF) of the sum of two independent rvs, :math:`X` and :math:`Y`, :math:`Z=X+Y`.

Discrete case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. tip::
	* We note that

		.. math:: p_{Z|X}(z|x)=\mathbb{P}(Z=z|X=x)=\mathbb{P}(X+Y=z|X=x)=\mathbb{P}(x+Y=z)=\mathbb{P}(Y=z-x)=p_{Y}(z-x)
	* Therefore, the joint mass between :math:`X` and :math:`Z` factorises as

		.. math:: p_{X,Z}(x,z)=p_X(x)p_{Z|X}(z|x)=p_X(x)p_{Y}(z-x)
	* Marginalising, we obtain

		.. math:: p_Z(z)=\sum_x p_{X,Z}(x,z)=\sum_x p_X(x)p_{Y}(z-x)=(p_X \ast p_Y)[z]

Continuous case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. tip::
	* We note that

		.. math:: F_{Z|X}(z|x)=\mathbb{P}(Z\leq z|X=x)=\mathbb{P}(X+Y\leq z|X=x)=\mathbb{P}(x+Y\leq z)=\mathbb{P}(Y\leq z-x)=F_{Y}(z-x)
	* Differentiating both sides, :math:`f_{Z|X}(z|x)=f_{Y}(z-x)`.
	* Therefore, the joint density between :math:`X` and :math:`Z` factorises as

		.. math:: f_{X,Z}(x,z)=f_X(x)f_{Z|X}(z|x)=f_X(x)f_{Y}(z-x)
	* Marginalising, we obtain

		.. math:: f_Z(z)=\int\limits_{-\infty}^\infty f_{X,Z}(x,z)\mathop{dx}=\int\limits_{-\infty}^\infty f_X(x)f_{Y}(z-x)\mathop{dx}=(f_X \ast f_Y)[z]

.. seealso::
	* Find the PDF of the sum of two independent normals.

******************************************************************************************
Covariance and correlation
******************************************************************************************

Scalar valued rvs
==========================================================================================
**Covariance** is defined between two scalar valued rvs as :math:`\sigma_{X,Y}=\mathrm{Cov}(X,Y)=\mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])]`.

.. note::
	* :math:`\mathrm{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]`.

		* Proof follows from expanding the expression in definition.
	* :math:`\mathrm{Cov}(X,X)=\mathbb{V}(X)`.
	* :math:`\mathrm{Cov}(X,aY+b)=a\cdot\mathrm{Cov}(X,Y)`.
	* :math:`\mathrm{Cov}(X,Y+Z)=\mathrm{Cov}(X,Y)+\mathrm{Cov}(X,Z)`.
	* :math:`\mathbb{V}(X+Y)=\mathbb{V}(X)+\mathbb{V}(Y)+\mathrm{Cov}(X,Y)`.
	* In general

		.. math:: \mathbb{V}\left(\sum_{i=1}^n X_i\right)=\sum_{i=1}^n \mathbb{V}(X_i)+\sum_{i=1}^n\sum_{j=1, i\neq j}^n\mathrm{Cov}(X_i,Y_j)

.. note::
	* **Correlation coefficient** is defined as the normalised version of covariance

		.. math:: \rho(X,Y)=\frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathbb{V}(X)\mathbb{V}(Y)}}.
	* We have :math:`|\rho(X,Y)|\leq 1`.

		* Let :math:`\tilde{X}=X-\mathbb{E}[X]` and :math:`\tilde{Y}=Y-\mathbb{E}[Y]` be the centered rvs.
		* The correlation coefficient then becomes

			.. math:: \rho(X,Y)=\frac{\mathbb{E}[\tilde{X}\tilde{Y}]}{\sqrt{\mathbb{E}[\tilde{X}^2]\cdot \mathbb{E}[\tilde{Y}^2]}}
		* The proof follows from Cauchy-Schwarz inequality.
	* The equality holds only when :math:`\tilde{X}=c\cdot \tilde{Y}` for some :math:`c`.

.. seealso::
	* We can solve the hat problem using covariance.

Vector valued rvs
==========================================================================================
Let us consider vector values rvs :math:`\mathbf{X}\in\mathbb{R}^n` and :math:`\mathbf{Y}\in\mathbb{R}^m` which takes values :math:`\mathbf{X}=\mathbf{x}\implies(X_1=x_1,\cdots,X_n=x_n)^\top` and :math:`\mathbf{Y}=\mathbf{y}\implies(Y_1=y_1,\cdots,Y_m=y_m)^\top`.

.. attention::
	* Expectation: :math:`\mathbb{E}[\mathbf{X}]=\{\mathbb{E}[X_1],\cdots\mathbb{E}[X_2]\}^\top\in\mathbb{R}^n` (similarly for :math:`\mathbf{Y}`).

.. note::
	* **Auto-covariance matrix**: :math:`\mathbb{V}(\mathbf{X})=\mathrm{Cov}(\mathbf{X},\mathbf{X})=\mathbf{K}_{\mathbf{X,X}}=\mathbb{E}\left[\left(\mathbf{X}-\mathbb{E}[\mathbf{X}]\right)\left(\mathbf{X}-\mathbb{E}[\mathbf{X}]\right)^\top\right]`.

		* This is also known as just variance matrix or variance-covariance matrix.
		* :math:`\mathbf{K}_{\mathbf{X,X}}\in\mathbb{R}^{n\times n}`.
		* The entries of this matrix are :math:`\mathrm{Cov}(X_i,X_j)=\sigma_{X_i,X_j}`.		
		* We note that when :math:`n=1` this reduces to the single rv case.
		* :math:`\mathbf{K}_{\mathbf{X,Y}}` is positive-semidefinite and symmetric.
		* **Linearity**: For a constant matrix :math:`\mathbf{A}` and a constant vector :math:`\mathbf{b}` of appropriate dimension

			.. math: \mathbb{V}(\mathbf{A}\mathbf{X}+\mathbf{b})=\mathbf{A}\mathbb{V}(\mathbf{X})\mathbf{A}^\top
	* **Auto-correlation matrix**: :math:`\mathbf{R}_{\mathbf{X,X}}=\mathbb{E}[\mathbf{X}\mathbf{X}^\top]`.

		* It is connected with auto-covariance as :math:`\mathbf{K}_{\mathbf{X,X}}=\mathbf{R}_{\mathbf{X,X}}-\mathbb{E}[\mathbf{X}]\mathbb{E}[\mathbf{X}]^\top`.
		* The entries of this matrix are :math:`\rho(X_i,X_j)=\frac{\sigma_{X_i,X_j}}{\sigma_{X_i}\sigma_{X_j}}`.
		* Let :math:`\bar{\mathbf{X}}=\mathbf{X}-\mathbb{E}[\mathbf{X}]` be the centered rv.

			* We note that in this case: :math:`\mathbf{K}_{\mathbf{X,X}}=\mathbf{R}_{\mathbf{X,X}}`.
		* **Precision matrix**: If it exists, :math:`\mathbf{K}_{\mathbf{X,X}}^{-1}` is known as precision matrix.
	* **Cross-covariance matrix**: :math:`\mathrm{Cov}(\mathbf{X},\mathbf{Y})=\mathbf{K}_{\mathbf{X,Y}}=\mathbb{E}\left[\left(\mathbf{X}-\mathbb{E}[\mathbf{X}]\right)\left(\mathbf{Y}-\mathbb{E}[\mathbf{Y}]\right)^\top\right]`.

		* :math:`\mathbf{K}_{\mathbf{X,Y}}\in\mathbb{R}^{n\times m}`.
		* The entries of this matrix are :math:`\mathrm{Cov}(X_i,Y_j)=\sigma_{X_i,Y_j}`.
		* If :math:`\mathbf{X}` and :math:`\mathbf{Y}` are of same dimension

			.. math: \mathbb{V}(\mathbf{X}+\mathbf{Y})=\mathbb{V}(\mathbf{X})+\mathrm{Cov}(\mathbf{X},\mathbf{Y})+\mathrm{Cov}(\mathbf{Y},\mathbf{X})+\mathbb{V}(\mathbf{Y})
	* **Correlation matrix**: :math:`\mathrm{\rho}(\mathbf{X},\mathbf{Y})=\mathbb{E}[\mathbf{X}\mathbf{Y}^\top]`.

		* The entries of this matrix are :math:`\rho(X_i,Y_j)=\frac{\sigma_{X_i,Y_j}}{\sigma_{X_i}\sigma_{Y_j}}`.

******************************************************************************************
Fundamentals of Point Estimation
******************************************************************************************
.. note::
	* **Estimate**: If we do not know the exact value of a rv :math:`Y`, or an unknown, constant, parameter :math:`\theta`, we can use a **guess** (estimate). 
	
		* The **guess** is a rv which can be observed or calculated based on other rvs.
	* **Estimator**: The rv which takes estimates as values is known as the **estimator**.

		* Estimator for :math:`Y` is usually written as :math:`\hat{Y}`.
		* Estimates are the values that this rv can take, :math:`\hat{Y}=\hat{y}`.
		* **Standard error**: :math:`\text{se}(\hat{Y})=\sqrt{\mathbb{V}_Y(\hat{Y})}`.
	* **Estimation error**: :math:`\tilde{Y}=\hat{Y}-Y`.

		* **Bias of an estimator**: :math:`\text{bias}(\hat{Y})=\mathbb{E}_Y[\tilde{Y}]`.
		* **Mean squared error**: :math:`\text{mse}(\hat{Y})=\mathbb{E}_Y[\tilde{Y}^2]`.

			* We note that :math:`\mathbb{V}_Y(\tilde{Y})=\mathbb{E}_Y[\tilde{Y}^2]-\left(\mathbb{E}_Y[\tilde{Y}]\right)^2=\text{mse}(\hat{Y})-\text{bias}(\hat{Y})^2`.
			* This can be rewritten as :math:`\text{mse}(\hat{Y})=\text{bias}(\hat{Y})^2+\mathbb{V}_Y(\tilde{Y})`.
			* If the quantity we're estimating is an unknown constant :math:`\theta` instead of being a rv (as in classical statistical estimation of an unknown parameter),

				.. math:: \text{mse}(\hat{\theta})=\text{bias}(\hat{\theta})^2+\mathbb{V}_\theta(\hat{\theta}-\theta)=\text{bias}(\hat{\theta})^2+\mathbb{V}_\theta(\hat{\theta})=\text{bias}(\hat{\theta})^2+\text{se}(\hat{\theta})^2

Bayesian point estimation using conditional expectation
==========================================================================================
.. note::
	* We assume that knowing :math:`X`, we can infer about an rv :math:`Y` (or, equivalently, an unknown constant :math:`\theta`).

		* We assume that conditional density :math:`f_{Y|X}(y|x)` is known.
	
			* We might have access to the conditional density directly.
			* We might have access to a prior :math:`f_Y(y)` and the likelihood :math:`f_{X|Y}(x|y)` and we can compute the posterior with Bayes theorem. 
	* From law of iterated expectation, we have :math:`\mathbb{E}[Y]=\mathbb{E}[\mathbb{E}[Y|X]]`.
		
		* This is a Bayesian estimator for :math:`Y`.
	* Therefore

		* Estimator: :math:`\hat{Y}=\mathbb{E}[Y|X]` can be thought of as an estimator of :math:`X` as their expected values are the same.

			* For a given value of :math:`X=x`, the estimation is :math:`\hat{y}=\mathbb{E}[Y|X=x]=r(x)`.
			* The function :math:`r(x)` is known called **regression function**.
		* Bias: Since :math:`\tilde{Y}` is expected to be 0

			.. math:: \text{bias}(\hat{Y})=\mathbb{E}[\tilde{Y}]=\mathbb{E}[\mathbb{E}[Y|X]]-\mathbb{E}[Y]=0\implies\text{mse}(\hat{Y})=\text{se}(\hat{Y})^2
		* **MMSE**: It can be shown that the conditional expectation estimator minimises the MSE. This is also known as a Minimum Mean Square Error Estimator (MMSE).
		* **Orthogonality Principle**: This error is uncorrelated with the estimator.

			* We note that

				.. math:: \mathrm{Cov}(\hat{Y},\tilde{Y})=\mathbb{E}[\hat{Y}\tilde{Y}]-\mathbb{E}[\hat{Y}]\mathbb{E}[\tilde{Y}]=\mathbb{E}[\hat{Y}\tilde{Y}]
			* Invoking law of iterated expectation

				.. math:: \mathbb{E}[\hat{Y}\tilde{Y}]=\mathbb{E}[\mathbb{E}[\hat{Y}\tilde{Y}|X]]
			* Given :math:`X`, :math:`\hat{Y}` is constant.

				.. math:: \mathbb{E}[\mathbb{E}[\hat{Y}\tilde{Y}|X]]=\mathbb{E}[\hat{Y}\cdot\mathbb{E}[\tilde{Y}|X]]=\mathbb{E}[\hat{Y}\cdot\mathbb{E}[(\hat{Y}-Y)|X]]=\mathbb{E}[\hat{Y}\cdot\mathbb{E}[\hat{Y}|X]]-\mathbb{E}[\hat{Y}\cdot\mathbb{E}[Y|X]]=\mathbb{E}[\hat{Y}^2]-\mathbb{E}[\hat{Y}^2]=0
		* Therefore, we have :math:`\mathbb{V}(Y)=\mathbb{V}(\hat{Y})+\mathbb{V}(\tilde{Y})=\text{se}(\hat{Y})^2+\text{mse}(\hat{Y})`.		

Conditional variance
========================================================================
.. note::
	We can define conditional variance as :math:`\mathbb{V}(X|Y)=\mathbb{E}[(X-\mathbb{E}[X|Y])^2|Y]` such that
	
		.. math:: \mathbb{E}[\mathbb{V}(X|Y)]=\mathbb{E}[\mathbb{E}[(X-\mathbb{E}[X|Y])^2|Y]]=\mathbb{E}[(X-\mathbb{E}[X|Y])^2]=\mathrm{E}[\tilde{X}^2]=\mathbb{V}(\tilde{X})

Law of iterated variance
========================================================================

.. note::
	We can rewrite the variance relation using this new notation

		.. math:: \mathbb{V}(X)=\mathbb{V}(\mathbb{E}[X|Y])+\mathbb{E}[\mathbb{V}(X|Y)]

.. tip::
	The iterated law of expectation and variance allows us to tackle complicated cases by taking help in conditioning.

.. seealso::
	* A coin with unknown probability of head is tossed :math:`n` times. The probability is known to be uniform in :math:`[0,1]`. Let :math:`X` is the total number of heads. Find :math:`\mathbb{E}[X]` and :math:`\mathbb{V}(X)`.

******************************************************************************************
Transforms of rv
******************************************************************************************
Moment Generating Function
========================================================================
.. note::
	* Moment generating function (MGF) of a rv is defined as a function of another parameter :math:`s`

		.. math:: M_X(s)=\mathbb{E}[e^{sX}]
	* This closely relates to the **Laplace Transform** (see stat stackexchange post `here <https://stats.stackexchange.com/questions/238776/how-would-you-explain-moment-generating-functionmgf-in-laymans-terms>`_)
	* We note that

		.. math:: M_X(s)=\mathbb{E}[e^{sX}]=\int\left(1+sx+\frac{s^2x^2}{2!}+\cdots\right)\mathop{dx}=1+s\cdot\mathbb{E}[X]+\frac{s^2}{2!}\cdot\mathbb{E}[X^2]+\cdots

		* From this, we establish that :math:`\frac{\mathop{d}^n}{\mathop{ds}^n}\left(M_X(s)\right)|_{s=0}=\mathbb{E}[X^n]`.
	* Extends to the multivariate case as

		.. math:: M_{X_1,X_2,\cdots,X_n}(s_1,s_2,\cdots,s_n)=\mathbb{E}[e^{\sum_{i=1}^n s_i X_i}]
	* For two independent rvs :math:`X` and :math:`Y`, the MGF of their sum :math:`Z=X+Y` is given by 

		.. math:: M_{Z}(s)=\mathbb{E}[e^{sX+sY}]=\mathbb{E}[e^{sX}e^{sY}]=\mathbb{E}[e^{sX}]\mathbb{E}[e^{sY}]=M_{X}(s)\cdot M_{Y}(s)
	* The above extends for multiple independent rvs.

.. attention::
	MGFs completely determines the CDFs and densities/mass functions.

.. tip::
	* Knowing MGF often helps us find the moments easier than direct approach.
	* Find the expectation and variance of exponential distribution in normal way and using MGF.

.. seealso::
	Find the expectation, variance and the transform of the sum of independent rvs where the number of terms is also a rv.

Integral Transforms
==========================================================================================
Let :math:`p` and :math:`q` be two densities over rv :math:`x\in\mathcal{X}` with finite Borel measure.

KL Divergence
------------------------------------------------------------------------------------------
.. math:: D_{KL}(p\parallel q)=\mathbb{E}_{x\sim p}\left[\log\frac{p(x)}{q(x)}\right]

.. note::
	* :math:`D_{KL}(p\parallel q)\geq 0` (proof follows from Jensen's inequality since :math:`-\log` is a convex function).
	* :math:`p=q\implies D_{KL}(p\parallel q)= 0` (other direction does not hold)
	* This is not a metric as :math:`D_{KL}(p\parallel q)\neq D_{KL}(q\parallel p)`.

.. seealso::
	* Note that entropy :math:`H(p)` and cross-entropy :math:`H(p, q)` can be defined as

		* :math:`H(p)=-\mathbb{E}_{x\sim p}[\log p(x)]`
		* :math:`H(p\parallel q)=-\mathbb{E}_{x\sim p}[\log q(x)]`
	* Therefore :math:`D_{KL}(p\parallel q)=H(p\parallel q)-H(p)`
	* [Gibb's inequality] :math:`D_{KL}(p\parallel q)\geq 0\implies H(p\parallel q)\ge H(p)`

.. attention::
	* Say :math:`x\sim p` but unknown, and we approximate :math:`p` with some :math:`q^*\in\mathcal{Q}` such that

		.. math:: q^*=\underset{q\in\mathcal{Q}}{\arg\min}\left(D_{KL}(p\parallel q)\right)
	* We disregard the inherent randomness associated with :math:`p` itself (i.e. :math:`H(p)`).
	* Minimising :math:`H(p\parallel q)` is the same as minimising :math:`D_{KL}(p\parallel q)`.
	* Finite sample case:

		* We use the empirical distribution :math:`\hat{p}` from a iid sample :math:`\{x_i\}_{i=1}^N`.
		* Using WLLN, as :math:`N\to\infty`, :math:`H(\hat{p},q)\overset{P}\to H(p\parallel q)`.
		* :math:`H(p\parallel q)` then becomes the same as negative log-likelihood (NLL)
	
			.. math:: H(p\parallel q)\approx H(\hat{p},q)=-\mathbb{E}_{x\sim \hat{p}}[\log q(x)]=-\frac{1}{N}\sum_{i=1}^N\log q(x_i)

For jointly distributed rvs :math:`x,y\sim p(x,y)`, we define

.. note::
	* Conditional entropy

		.. math:: H(X∣Y)=−\mathbb{E}_{x,y\sim p(x,y)}​[\log p(x|y)]=-\mathbb{E}_{y\sim p(y)}\left[\mathbb{E}_{x\sim x|y}\left[\log p(x|y)\right]\right]
	* Mutual information 

		.. math:: I(X;Y)=H(X)−H(X∣Y)

Integral Probability Metric: Wasserstein Distance
------------------------------------------------------------------------------------------

Integral Probability Metric: Maximum Mean Discrepancy (MMD)
------------------------------------------------------------------------------------------

.. seealso::
	`Divergence measures <https://www.desmos.com/calculator/2sboqbhler>`_
