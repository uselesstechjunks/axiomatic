##########################################################################################
Statistical Inference
##########################################################################################

.. note::
	**Statistical Functionals**: The functions of this form, :math:`T(F)`, such as

	* density :math:`T(F)=f_F=\frac{\mathop{d}}{\mathop{dx}}=\mathop{dF}`
	* expectation :math:`T(F)=\mathbb{E}_F[X]=\int x \mathop{dF}`
	* variance :math:`T(F)=\mathbb{V}_F(X)=\int(x-\mathbb{E}[X])^2\mathop{dF}`
	* moments: :math:`T(F)=M_F(X)=\int e^{sx}\mathop{dF}`
	* median: :math:`T(F)=F^{-1}(1/2)`	

.. attention::
	* We have a sample of size :math:`n`, :math:`X_1,\cdots X_n` from an unknown CDF :math:`F`.
	* The task for statistical inference is to infer :math:`F` or some :math:`T(F)`, that best explains the data, for some criteria of **best** chosen beforehand.	
	* The **inferred values** based on data are called **estimates** of the quantities of interest.
	* Estimates are rv as their values may change subject to a different sample.
	* The **rv** associated with these estimates is called an **estimator**.

.. attention::
	* **Statistic**: Any function of the data :math:`g(X_1,\cdots,X_n)` is called a statistic.
	* Any estimator is a statistic.

******************************************************************************************
Statistical Model
******************************************************************************************
.. note::
	A statistical model :math:`\mathcal{F}` is set of distributions or other statistical functionals of interest.

Types of Statistical Model
==========================================================================================
The following categories of models are based on the dimensionality of :math:`\mathcal{F}`.

Parametric Model
------------------------------------------------------------------------------------------
.. note::
	* :math:`\mathcal{F}` can be spanned by a finitely many parameters.

.. seealso::
	Example: 

	* Let the parameter vector be :math:`\boldsymbol{\theta}=(\theta_1,\cdots,\theta_k)^\top`.
	* The model here is the set of distributions :math:`\mathcal{F}=\{F_\boldsymbol{\theta}\}=\{F_X(x;\theta_1,\cdots,\theta_k)\}`.

Non-parametric Model
------------------------------------------------------------------------------------------
.. note::
	:math:`\mathcal{F}` cannot be spanned by a finitely many parameters.

.. seealso::
	Example: Set of all possible CDFs.

******************************************************************************************
Different Approaches to Inference
******************************************************************************************
Bayesian Inference
==========================================================================================
.. note::
	* The quantity that we want to estimate is assumed to be a rv on its own, :math:`\Theta`. 
	* Before observing any data, we have a prior notion of what its distribution. This is expressed as the prior probability :math:`f_\Theta(\theta)`.
	* The likelihood is the PDF of the data conditioned on :math:`\Theta`, :math:`f_{X|\Theta}(x|\theta)`.
	* The posterior is obtained by applying Bayes rule which gives a **single probability model** for the quantity after observation :math:`f_{\Theta|X}(\theta|x)`.
	* We perform inference about :math:`\Theta` based on this distribution directly.

Frequentist (Classical) Inference
==========================================================================================
.. note::
	* The quantity that we want to estimate is assumed to be an unknown constant, :math:`\theta`.
	* No prior knowledge is assumed about this.
	* We assume that our underlying probability model is dependent on :math:`\theta` in some way.
	* Therefore, the **probability model here is the collection of PDFs** :math:`f_\theta(x;\theta)` for each possible values of :math:`\theta`.
	* In order to perform inference, our statements must apply to all possible values of :math:`\theta`.

******************************************************************************************
Types of Inference
******************************************************************************************
Point Estimation
==========================================================================================
.. note::
	* A single **best** estimate (point) within the model for 
		
		* Classical: the unknown constant :math:`\theta`
		* Bayesian: the rv :math:`\Theta=\theta`
	* This estimate of :math:`\theta` is expressed as a statistic :math:`\widehat{\theta}_n=g(x_1,\cdots,x_n)`
	* The estimator :math:`\widehat{\Theta}_n` is always a rv as it evaluates to a different value with a different sample.
	* Examples: 

		#. a single distribution/density function (parameterised/non-parameterised)
		#. a single regression function
		#. a single value for expectation/variance/other moments
		#. a single prediction for a dependent variable with a given independent variable. etc. 

Some useful terminology
-------------------------------------------------------------------------------------------
.. note::
	* **Sampling Distribution**: The distribution of :math:`\widehat{\Theta}_n` over different samples.
	* **Estimation Error**: 

		* Classical: :math:`\tilde{\Theta}_n=\widehat{\Theta}_n-\theta`
		* Bayesian: :math:`\tilde{\Theta}_n=\widehat{\Theta}_n-\Theta`
	* **Bias**: 

		* Classical: :math:`\text{b}(\widehat{\Theta}_n)=\mathbb{E}_{\theta}[\tilde{\Theta}_n]=\mathbb{E}_{\theta}[\widehat{\Theta}_n]-\theta`
		* Bayesian: :math:`\text{b}(\widehat{\Theta}_n)=\mathbb{E}[\tilde{\Theta}_n]=\mathbb{E}[\widehat{\Theta}_n]-\mathbb{E}[\Theta]`
	* **Standard Error**:

		* Classical: :math:`\text{se}(\widehat{\Theta}_n)=\sqrt{\mathbb{V}_{\theta}(\widehat{\Theta}_n)}`
		* Bayesian: :math:`\text{se}(\widehat{\Theta}_n)=\sqrt{\mathbb{V}(\widehat{\Theta}_n)}`
	* If the variance in above is also an estimate (as it often is), then we estimate SE as :math:`\widehat{\text{se}}=\widehat{\text{se}}(\widehat{\Theta}_n)=\sqrt{\widehat{\mathbb{V}}_{\theta}(\widehat{\Theta}_n)}`.
	* **Mean-Squared Error**: 

		* Classical: :math:`\text{mse}(\widehat{\Theta}_n)=\mathbb{E}_{\theta}[\tilde{\Theta}_n^2]=\mathbb{E}_{\theta}[(\widehat{\Theta}_n-\theta)^2]=\text{b}^2(\widehat{\Theta}_n)+\text{se}^2(\widehat{\Theta}_n)`
		* Bayesian: :math:`\text{mse}(\widehat{\Theta}_n)=\mathbb{E}[\tilde{\Theta}_n^2]=\mathbb{E}[(\widehat{\Theta}_n-\Theta)^2]=\mathbb{E}[\widehat{\Theta}_n^2]+\mathbb{E}[\Theta^2]-2\mathbb{E}[\widehat{\Theta}_n\Theta]`

.. note::
	* **Unbiased Estimator**: If :math:`\text{b}(\widehat{\Theta}_n)=0`.
	* **Asymptotically Unbiased Estimator**: If :math:`\widehat{\Theta}_n\xrightarrow[]{L_1}\theta` (or :math:`\Theta`).
	* **Consistent Estimator**: If :math:`\widehat{\Theta}_n\xrightarrow[]{P}\theta` (or :math:`\Theta`).
	* **Asymptotically Normal Estimator**: 

		* Classical: :math:`\frac{\widehat{\Theta}_n-\theta}{\widehat{\text{se}}}\xrightarrow[]{D}\mathcal{N}(0,1)`.
		* Bayesian: :math:`\frac{\widehat{\Theta}_n-\Theta}{\widehat{\text{se}}}\xrightarrow[]{D}\mathcal{N}(0,1)`.

.. attention::
	Theorem: If :math:`\lim\limits_{n\to\infty}\text{b}_\theta(\widehat{\Theta}_n)=0` and :math:`\lim\limits_{n\to\infty}\text{se}(\widehat{\Theta}_n)=0` then :math:`\widehat{\Theta}_n` is consistent.

Confidence Set Estimation
==========================================================================================
.. attention::
	* In Bayesian setting, the point estimate is already associated with a probability distribution which convey the degree of belief about the true quantity being the same as the estimated quantity.
	* On the other hand, confidence set estimation is a technique used in a classical setting. However, this makes probabilitic statement about the estimated set, not the quantity itself.

.. note::
	* An estimated set which traps the fixed, unknown value of our quality of interest with a pre-determined probability.
	* A 95% confidence set means that if we repeatedly estimate it from multiple samples (works even if samples are from completely unrelated experiments), then around 95% of the times the estimated set contains the true quantity.

.. attention::
	#. A :math:`1-\alpha` confidence interval (CI) for a real qualtity of interest :math:`\theta` is defined as :math:`\widehat{C}_n=(a,b)` where :math:`\mathbb{P}(\theta\in\widehat{C}_n)\ge 1-\alpha`. 
	#. The task is to estimate :math:`\widehat{a}=a(X_1,\cdots,X_n)` and :math:`\widehat{b}=b(X_1,\cdots,X_n)` such that the above holds. 
	#. For vector quantities, this is expressed with sets instead of intervals.
	#. In regression setting, a confidence interval around the regression function can be thought of the set of functions which contains the true function with certain probabilty. However, this is usually never measured.

Some useful terminology
-------------------------------------------------------------------------------------------
.. note::
	* **Pointwise Asymptotic CI**: :math:`\forall\theta,\liminf\limits_{n\to\infty}\mathbb{P}_{\theta}(\theta\in\widehat{C}_n)\ge 1-\alpha`

		* Given any :math:`\theta`, the smallest probability that :math:`\widehat{C}_n` captures :math:`\theta` is at least :math:`1-\alpha` asymptotically as :math:`n\to\infty`.
		* The rate of this convergence depends on the value of :math:`\theta`.
	* **Uniform Asymptotic CI**: :math:`\liminf\limits_{n\to\infty}\inf\limits_{\theta\in\Theta}\mathbb{P}_{\theta}(\theta\in\widehat{C}_n)\ge 1-\alpha`

		* Given any :math:`n`, we consider the smallest probability that :math:`\widehat{C}_n` captures :math:`\theta` for any :math:`\theta\in\Theta`.
		* This probability is at least :math:`1-\alpha` asymptotically as :math:`n\to\infty`.
		* Uniform Asymptotic CI is stricter, as in, satisfying this condition automatically implies the former.
	* **Normal-based CI**: If :math:`\widehat{\Theta}_n` is an aysmptotically normal estimator of :math:`\theta`, then a :math:`1-\alpha` confidence interval is given by

		.. math:: (\widehat{\Theta}_n-z_{\alpha/2}\widehat{\text{se}},\widehat{\Theta}_n+z_{\alpha/2}\widehat{\text{se}})
	
		* The above is a pointwise asymptotic CI.

Hypothesis Testing
==========================================================================================
.. note::
	* We have 2 or more unknown hypothesis about the probability model, :math:`H_0` (null) and :math:`H_1` (alternate), which are exclusively T/F.
	
		* We might have 1 hypothesis which we can convert into 2 as :math:`H_1=\not H_0`.
	* We assume that this unknown hypothesis determines the distribution of the data.

		* Bayesian: 
			* Here we assume that the hypothesis themselves are Bernoulli rv, :math:`H_0=T\implies\Theta=1.`
			* We have some prior :math:`p_{\Theta}(\theta)`
		* Classical: 
			* We assume that we have a different probability model under each hypothesis, :math:`f_X(x; H_0)` and :math:`f_X(x; H_1)`.
			* No prior knowledge is assumed
	* Inferring about :math:`H_0` and :math:`H_1` then becomes similar to point estimation.

.. attention::
	We create a :math:`1-\alpha` confidence set for the estimated quantity.

		* If the quantity as-per-model doesn't fall within this set, then we **reject** the null hypothesis with significance level :math:`\alpha`. 
		* If it does, then we **fail to reject** the null hypothesis.

.. note::
	* TODO - write common definitions, significance level, rejection region, critical point, type-I type-II errors

******************************************************************************************
Machine Learning as a Statistical Inference
******************************************************************************************
.. note::
	* We have iid samples from an unknown joint CDF, e.g. :math:`(X_i,Y_i)_{i=1}^n\sim F_{X,Y}`.
	* **Model inference**: Model inference means estmating the conditional expectation corresponding to :math:`F_{Y|X}` with a **regression function** :math:`r(X)` such that

		.. math::
		    T(F_{Y|X})=\mathbb{E}[Y|X]=r(X)+\epsilon

	  where :math:`\mathbb{E}[\epsilon]=0`. 

		* This inference is known as **learning** in Machine Learning and **curve estimation** in statistics.
	* **Variable inference**: In the above case, a variable inference means estimating an unseen :math:`Y|X=x` by :math:`\widehat{Y}=\widehat{y}=r(x)` for a given :math:`X=x`. 

		* This is known as **inference** in Machine Learning and **prediction** in statistics.

.. note::
	Dependent and Independent Variable: 


.. attention::
	* The process that decides the model, such as choice of function-class or number of parameters, is independent of the inference and is performed separately beforehand. In ML, these are called **hyper-parameters**. 
	* Since there are multiple items to choose before performing inference, it is useful to clarify the sequence:

		#. A metric of goodness of an estimator is chosen first.
		#. A model is chosen (such as, hyperparameters).
		#. Inference is performed using computation involving the samples.
		#. Quality of model is judged by evaluating the model on the inference data.
		#. (Optional) A different model is chosen and the process repeats.

	* :math:`X` is called the independent variable (**features**) and :math:`Y` called as dependent variable (**target**). 
	* Independent variables are often multidimensional vectors :math:`X=\mathbf{x}\in\mathbb{R}^d` for some :math:`d>1`.	
