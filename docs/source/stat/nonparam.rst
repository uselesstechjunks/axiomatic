########################################################################################
Non-Parametric Methods
########################################################################################

****************************************************************************************
Estimation of CDF
****************************************************************************************
Empirical distribution function as an estimator
========================================================================================
The estimator for any CDF :math:`F` is the discrete estimator :math:`\widehat{F}_n` which assigns a mass :math:`1/n` to every point in sample :math:`\{X_i\}_{i=1}^n`.

.. note::
	Let 
	
		.. math:: I(X_i\leq x)=\begin{cases}1 & \text{if $X_i\leq x$}\\ 0 & \text{otherwise}\end{cases}

	Then

		.. math:: \widehat{F}_n(x)=\frac{1}{n}\sum_{i=1}^n I(X_i\leq x_i)

.. attention::
	* Unbiased: :math:`\mathbb{E}[\widehat{F}_n(x)]=F(x)`
	* :math:`\text{se}_F^2=\mathbb{V}_F(\widehat{F}_n)=\frac{F(x)(1-F(x))}{n}`, and :math:`\lim\limits_{n\to\infty}\text{mse}(\widehat{F}_n)=0`.
	* Empirical distribution function is a consistent estimator for any distribution.

		.. math:: \widehat{F}_n(x)\xrightarrow[]{P}F(x)

Confidence interval for CDF estimator
========================================================================================
.. note::        
	* **Glivenko-Cantelli Theorem**: :math:`||\widehat{F_n}(x)-F(x)||_\infty=\sup_{x}|\widehat{F_n}(x)-F(x)|\xrightarrow[]{as} 0`.
	* **Dvoretzsky-Kiefer-Wolfowitz (DKW) Inequality**: For any :math:`\epsilon>0`,
    
		.. math:: \mathbb{P}(\sup_x|\widehat{F_n}(x)-F(x)|>\epsilon) \le 2\exp(-2n\epsilon^2)

.. tip::
	* It can be derived from DKW that we can form a :math:`1-\alpha` CI of width :math:`2\epsilon_n` around :math:`\widehat{F_n}` where :math:`\epsilon_n=\sqrt{\frac{1}{2n}\ln(\frac{2}{\alpha})}`.

		* TODO: derive.

****************************************************************************************
Plug-in Estimator for Statistical Functionals
****************************************************************************************
The plug-in estimator :math:`\widehat{T}_n(F)` for any :math:`T(F)` can be obtained by replacing :math:`F` with :math:`\widehat{F}_n`.

Estimator for mean
========================================================================================
.. note::
	Here :math:`T(F)=\int x\mathop{dF}`. Since :math:`\widehat{F}_n` is discrete

		.. math:: \widehat{T}_n(F)=T(\widehat{F}_n)=\frac{1}{n}\sum_{i=1}^nX_i=\bar{X}

	* :math:`\text{se}_F^2=\mathbb{V}_F(\widehat{T}_n)=\frac{\sigma^2}{n}`.
	* CLT says that this estimator is asymptotically normal.

.. tip::
	* :math:`\text{se}_F` depends on the true distribution :math:`F`.
	* If the true variance :math:`\sigma^2` is not known, it can be estimated as the next step.
	* Let the estimate for :math:`\text{se}_F` be :math:`\widehat{\text{se}}_n`. Assuming asymptotic normality, we can compute confidence interval as

		.. math:: T(\widehat{F}_n)\pm z_{\alpha/2}\widehat{\text{se}}_n

Estimtor for variance
========================================================================================
.. note::
	Here :math:`T(F)=\int (x-\mathbb{E}[X]^2)\mathop{dF}`. Since :math:`\widehat{F}_n` is discrete

		.. math::  \widehat{T}(F)=T(\widehat{F}_n)=\frac{1}{n}\sum_{i=1}^n(X_i-\bar{X})^2=S^2_n

	* For sample mean estimator, :math:`\widehat{\text{se}}^2_n=S^2_n`

.. tip::
	We can use similar techniques for estimating any moments of :math:`F`.

Estimator for other functionals
=========================================================================================
The estimator can be obtained similarly.

.. tip::
	* :math:`\text{se}_F` often has to be estimated in order to obtain a confidence interval.
	* As the estimator is also a statistic, the variance can be obtained using the following methodology.

****************************************************************************************
Variance Estimation of a Statistic for CI
****************************************************************************************
We're interested in estimating the variance of a statistic :math:`g(X_1,\cdots,X_n)` given the sample.

Bootstrap
========================================================================================
Key Idea
----------------------------------------------------------------------------------------
Let :math:`X^*=(X^*_1,\cdots,X^*_2)` be a simulation obtained from the original sample :math:`(x_1,\cdots,x_n)` by drawing **with replacement**.

.. note::
	* Let :math:`Y=g(X^*_1,\cdots,X^*_n)`
	* WLLN: :math:`\frac{1}{B}\sum_{i=1}^BY_i\xrightarrow[]{P}\mathbb{E}[Y]`
	* :math:`\frac{1}{B}\sum_{i=1}^Bh(Y_i)\xrightarrow[]{P}\mathbb{E}[h(Y)]`
	* :math:`\frac{1}{B}\sum_{i=1}^B(Y_i-\bar{Y})^2=\frac{1}{B}\sum_{i=1}^n Y_i^2-\left(\frac{1}{B}\sum_{i=1}^n Y_i\right)^2\xrightarrow[]{P}\mathbb{E}[Y^2]-(\mathbb{E}[Y])^2=\mathbb{V}(Y)`

.. tip::
	* We can therefore estimate the variance of a statistic by sample variance obtained via simulation :math:`B` times.

Obtaining the variance of an estimator
----------------------------------------------------------------------------------------
Let the estimator for :math:`T(F)` be :math:`\widehat{T}_n=g(X_1,\cdots,X_n)`.

.. note::
	* For :math:`i=1` to :math:`B`:

		* Obtain a simulated sample :math:`X_i^*=(X^*_{i,1},\cdots,X^*_{i,n})`.
		* Compute estimate :math:`\widehat{T}^*_{n,i}=g(X^*_{i,1},\cdots,X^*_{i,n})`
	* Compute bootstrap variance

		.. math:: v_{\text{boot}}=\frac{1}{B}\sum_{i=1}^B(\widehat{T}^*_{n,i}-\frac{1}{B}\sum_{j=1}^B\widehat{T}^*_{n,i})^2
	* Use estimation strategy 
	
		.. math:: \mathbb{V}_F(\widehat{T}_n)\approx\mathbb{V}_{\widehat{F}_n}(\widehat{T}_n)\approx v_{\text{boot}}

.. tip::
	We can use :math:`v_{\text{boot}}` to obtain :math:`\text{se}` and compute CI.

Jack knife
========================================================================================
.. note::
	* Instead of a simulated sample obtained via replacement, we remove one observation and consider it a new sample. 
	* Rest of the steps are carried out exactly the same way as bootstrap and we get :math:`v_{\text{jack}}` to compute CI.
	* This is less computationally expensive than bootstrap.
