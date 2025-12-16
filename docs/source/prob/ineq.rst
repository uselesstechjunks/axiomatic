########################################################################################
Tail Bounds, Convergence and Limit Theorems
########################################################################################

****************************************************************************************
Tail Bounds : Inequalities
****************************************************************************************
Why do we need inequalities?

.. note::
	* If we know the density directly, then, theoretically, we can compute exactly how much probability lie on the "tails".
	* However, often we have to work with scenarios where either the density is not known or the exact calculation is cumbersome.
	* These inequalities bound the probability on the tails based on how much we know about the underlying distribution.

Mean known: Markov
========================================================================================
.. note::
	* Let :math:`X` be a **non-negative** rv with well defined :math:`\mathbb{E}[X]=\mu`.
	* Markov's inequality states that the tail probability goes down inversely as we move further right.

		.. math:: \mathbb{P}(X\geq t)\leq \frac{\mu}{t}
	* Proof:

		.. math:: \mathbb{P}(X\geq t)=\int\limits_t^\infty f_X(x)\mathop{dx}=\frac{1}{t}\int\limits_t^\infty t\cdot f_X(x)\mathop{dx}\leq \frac{1}{t}\int\limits_t^\infty x\cdot f_X(x)\mathop{dx}\leq \frac{1}{t}\int\limits_{-\infty}^\infty x\cdot f_X(x)\mathop{dx}

Mean and variance known: Chebyshev
========================================================================================
.. note::
	* Let :math:`X` be **any** rv with well defined :math:`\mathbb{E}[X]=\mu` and :math:`\mathbb{V}(X)=\sigma^2`.
	* Chebyshev's inequality states that the tail probability of :math:`t` being away from :math:`\mu` goes down quadratically.

		.. math:: \mathbb{P}(|X-\mu|\geq t)\leq \frac{\sigma^2}{t^2}
	* Proof:

		.. math:: Y=(X-\mu)\implies\mathbb{E}[Y^2]=\sigma^2\implies\mathbb{P}(|Y|\geq t)=\mathbb{P}(Y^2\geq t^2)\leq\frac{\sigma^2}{t^2}
	* This is a tighter bound than Markov's.

MGF known: Chernoff's Bound
========================================================================================
.. note::
	* Let :math:`X` be any rv with well defined MGF, :math:`M_X(s)`.
	* Chernoff's bound states that the probability of the tails goes down exponentially as we move further right. So, for any :math:`s`,

		.. math:: \mathbb{P}(X\geq t)\leq \frac{M_X(s)}{e^{st}}
	* We can recover Markov's and Chebyshev's from this one.

Distribution known (Gaussian): Mill 
========================================================================================
.. note::
	* Let :math:`Z` be a standard normal rv.
	* Mills equality calculates directly from density how much probability lies on the tails.

		.. math:: \mathbb{P}(|Z|\geq t)\leq \frac{2e^{-t^2/2}}{t}

****************************************************************************************
Convergence of sequences involving rvs
****************************************************************************************
The concept of convergence of sequences involving rvs is more subtle than convergence of normal sequences. We consider a sequence of rvs, :math:`X_1,X_2,\cdots` and :math:`X` as the limiting rv. There are multiple notions of convergence for such sequences, some being stronger than others (as in, convergence in one sense might imply convergence in another sense, but not vice versa).

Convergence in distribution
========================================================================================
.. note::
	* :math:`(X_n)_{n=1}^\infty` is said to be converging to :math:`X` in distribution, :math:`X_n\xrightarrow[]{D}X`, if

		.. math:: \lim\limits_{n\to\infty}\mathbb{P}(X_n\leq t)=\mathbb{P}(X\leq t)
	* If :math:`X_i\sim F_i` and :math:`X\sim F`, then the above can be written in terms of CDF as

		.. math:: \lim\limits_{n\to\infty}F_n(t)=F(t)

Convergence in probability
========================================================================================
.. note::
	* :math:`(X_n)_{n=1}^\infty` is said to be converging to :math:`X` in probability, :math:`X_n\xrightarrow[]{P}X`, if

		.. math:: \lim\limits_{n\to\infty}\mathbb{P}(|X_n-X|\geq\epsilon)=0
	* It can be restated using notions similar to convergence from calculus as follows: for a given **accuracy level** :math:`\epsilon>0` and a given **confidence level** :math:`\delta>0`,

		.. math:: \exists N_{(\epsilon,\delta)} . n>N_{(\epsilon,\delta)}\implies\mathbb{P}(|X_n-X|\geq\epsilon)\leq\delta
	* Convergence in probability implies convergence in distribution.

Convergence in :math:`L_1`
========================================================================================
.. note::
	* :math:`(X_n)_{n=1}^\infty` is said to be converging to :math:`X` in :math:`L_1`, :math:`X_n\xrightarrow[]{L_1}X`, if

		.. math:: \lim\limits_{n\to\infty}\mathbb{E}[|X_n-X|]=0
	* Convergence in :math:`L_1` implies convergence in probability.

Convergence in quadratic mean
========================================================================================
.. note::
	* :math:`(X_n)_{n=1}^\infty` is said to be converging to :math:`X` in quadratic mean, :math:`X_n\xrightarrow[]{qm}X`, if

		.. math:: \lim\limits_{n\to\infty}\mathbb{E}[(X_n-X)^2]=0
	* Convergence in quadratic mean implies convergence in :math:`L_1`.

Almost surely convergence
========================================================================================
.. note::
	* :math:`(X_n)_{n=1}^\infty` is said to be converging to :math:`X` almost surely (with probability 1), :math:`X_n\xrightarrow[]{as}X`, if

		.. math:: \mathbb{P}(\lim\limits_{n\to\infty} X_n=X)=1
	* This can be restated as follows: for any :math:`\epsilon>0`

		.. math:: \mathbb{P}(\lim\limits_{n\to\infty}|X_n-X|\geq\epsilon)=0
	* Interpretation:

		* We note that the limit is inside. Hence it's talking about **probability about the convergence of the values** of the rvs in standard calculus sense.
		* We can think that the sample space is represented as the set of sequences :math:`\{(x_n)_{n=1}^\infty\}`.
		* In this case, almost surely convergence would mean that there are only finite number of elements in this set where the limit doesn't converge to the value of the rv :math:`X`.
	* Almost surely convergence implies convergence in quadratic mean.

****************************************************************************************
Convergence of sequences involving parametric models
****************************************************************************************
Convergence of functions
========================================================================================
Let :math:`\left(f_n(x)\right)_{i=1}^n` be a sequence of functions where :math:`f_n:E\to\mathbb{R}`. Let :math:`f:E\to\mathbb{R}` is the limit function.

Point-wise convergence
----------------------------------------------------------------------------------------
.. math:: \forall x\in E, \lim\limits_{n\to\infty}|f_n(x)-f(x)|=0

.. note::
	* Interpretation: For every :math:`\epsilon>0`, there is a :math:`N_{\epsilon,x}` for each specific :math:`x\in E`, such that :math:`n> N_{\epsilon,x}\implies |f_n(x)-f(x)|<\epsilon`.
	* We note that the speed of convergence is dependent on the value of :math:`x`.	

Uniform convergence
----------------------------------------------------------------------------------------
.. math:: \lim\limits_{n\to\infty}\sup_{x\in E}|f_n(x)-f(x)|=0

.. note::
	* Interpretation: For every :math:`\epsilon>0`, there is a universal :math:`N_\epsilon`, such that :math:`n> N_\epsilon\implies |f_n(x)-f(x)|<\epsilon` holds for any :math:`x\in E`.
	* We note that the speed of convergence is independent on the value of :math:`x`. This is more stricter.

Convergence of statistical functionals
========================================================================================
Let :math:`\left(f_n(\theta)\right)_{i=1}^n` be a sequence functions evaluated on observed data :math:`\left(X_i\right)_{i=1}^n`, where :math:`X_i\sim f_X(x_i;\theta)` in a parametric model.

.. seealso::
	For example, :math:`f_n(\theta)=\frac{1}{n}\sum_{i=1}^n X_i` and :math:`f(\theta)=\mathbb{E}_\theta[X]`.

Point-wise convergence in probability
----------------------------------------------------------------------------------------
.. math:: \forall \theta\in\Theta, |f_n(\theta)-f(\theta)|\xrightarrow[]{P}0

Uniform convergence in probability
----------------------------------------------------------------------------------------
.. math:: \sup_{\theta\in\Theta} |f_n(\theta)-f(\theta)|\xrightarrow[]{P}0

****************************************************************************************
Limit Theorems
****************************************************************************************
Here we deal with rvs of 3 special kind for a given sequence of rvs :math:`(X_n)_{n=1}^\infty`. Let the rvs be independent and have common, well defined mean :math:`\mu` and variance :math:`\sigma^2`.

.. note::
	* Let the sum rv be :math:`S_n=\sum_{i=1}^n X_i` for a given :math:`n`. We can think of a sequence of this as :math:`(S_n)_{n=1}^\infty`.

		* We note that :math:`\mathbb{E}[S_n]=n\mu` :math:`\mathbb{V}(S_n)=n\sigma^2`.
	* Let the sample mean rv be :math:`M_n=\frac{S_n}{n}` for a given :math:`n`. We can think of a sequence of this as :math:`(M_n)_{n=1}^\infty`.

		* We note that :math:`\mathbb{E}[M_n]=\mu` and :math:`\mathbb{V}(M_n)=\sigma^2/n`.
	* Let the standardised rv be :math:`Z_n=\frac{S_n-n\mu}{\sigma\sqrt{n}}` for a given :math:`n`. We can think of a sequence of this as :math:`(Z_n)_{n=1}^\infty`.

		* We note that :math:`\mathbb{E}[Z_n]=0` and :math:`\mathbb{V}(M_n)=1`.

Weak Law of Large Number
========================================================================================
.. note::
	* This talks about the convergence properties of :math:`M_n`.
	* Recall that :math:`\mathbb{E}[M_n]=\mu` and :math:`\mathbb{V}(M_n)=\frac{\sigma^2}{n}`.
	* Applying Chebyshev's inequality, we obtain :math:`\mathbb{P}(|M_n-\mu|\geq \epsilon)\leq \frac{\sigma^2}{n\epsilon^2}`.
	* Therefore :math:`\lim\limits_{n\to\infty}\mathbb{P}(|M_n-\mu|\geq \epsilon)=0`.
	* WLLN: For a sequence of rvs :math:`(X_n)_{n=1}^\infty`, independent with common, well defined mean and variance, :math:`M_n\xrightarrow[]{P}\mu`.

.. attention::
	It doesn't require the rvs to be identically distributed.

.. warning::
	It doesn't talk about how quickly the sample mean converges.	

Special case: bounded rvs
----------------------------------------------------------------------------------------
Tail bounds from Chebyshev's inequality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If we know that the rvs are bounded, i.e. :math:`\forall i, a\leq X_i\leq b`, then we know that :math:`\mathbb{V}(X_i)\leq \frac{(b-a)^2}{4}` (see note in random variable chapter TODO add link).

.. note::
	* From Chebyshev's inequality, we can obtain a bound which goes down inversely with :math:`n`.

		.. math:: \mathbb{P}(|M_n-\mu|\geq \epsilon)\leq \frac{\sigma^2}{n\epsilon^2}\leq \frac{(b-a)^2}{4n\epsilon^2}

Tigher bounds from Hoeffding's inequality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. attention::
	* For bounded rvs, Hoeffding's inequality gives an even tigher bound which goes down exponentially with :math:`n`.

		.. math:: \mathbb{P}(|M_n-\mu|\geq \epsilon)\leq 2\exp\left(\frac{-2n\epsilon^2}{(b-a)^2}\right)

.. note::
	`Concentration Inequality <https://en.wikipedia.org/wiki/Concentration_inequality>`_

Strong Law of Large Number
========================================================================================
.. note::
	* SLLN: For a sequence of rvs :math:`(X_n)_{n=1}^\infty`, iid with well defined moments till at least 4th moment, :math:`M_n\xrightarrow[]{as}\mu`.

Central Limit Theorem
========================================================================================
.. note::
	* CLT: For a sequence of rvs :math:`(X_n)_{n=1}^\infty`, iid with well defined mean and variance, :math:`Z_n\xrightarrow[]{D}\mathcal{N}(0,1)`.
	* Since :math:`S_n` can be expressed as a linear transformation of :math:`Z_n`, it also converges to some normal distribution with ever increasing mean :math:`n\mu` and variance :math:`\sigma\sqrt{n}`.

.. warning::
	* It doesn't talk about how quickly the sum converges to normal.
	* The speed of this convergence depends on the actual underlying distribution.

		* Uniform: very quickly resembles a normal.
		* Exponential: takes a long time.

The Delta Method
========================================================================================
.. note::
	* Let :math:`X_n\xrightarrow[]{D}\mathcal{N}(\mu,\frac{\sigma}{\sqrt{n}})`
	* Let :math:`g` be a differentiable function.
	* Then :math:`g(X_n)\xrightarrow[]{D}\mathcal{N}(g(\mu),\frac{\sigma}{\sqrt{n}}\left(g'(\mu)^2\right))`.

.. tip::
	A multivariate version can be obtained by observing that :math:`\sigma\left(g'(\mu)^2\right)` becomes :math:`\nabla_g(\mu)^\top\Sigma\nabla_g(\mu)`.
