#######################################################################################
Random Variable
#######################################################################################
Random variables (rvs) are real-valued functions of the outcome of an experiment.

.. note::
	* A function of a rv is another rv.
	* We can associate certain *central measures*/*averages* (such as **mean**, **variance**) with each rv, subject to certain condition on their existence.
	* We can *condition* an rv on an event or another rv.
	* We can define the notion of *independence* of an rv w.r.t an event or another rv.

*********************************************
Discrete Random Variable
*********************************************
Discrete = values are from a finite/countably infinite subset of :math:`\mathbb{R}`.

Probability mass function
=========================================
.. note::
	For a discrete rv, :math:`X`:

	* We can define a probability mass function (PMF), :math:`p_X(x)`, associated with :math:`X`, as follows: For each value :math:`x` of :math:`X`

		#. Collect all possible outcomes that give rise to the event :math:`\{X=x\}`.
		#. Add their probabilities to obtain the mass :math:`p_X(x)=\mathbb{P}(\{X=x\})`.

	* A function :math:`g(X)` of :math:`X` is another rv, :math:`Y`, whose PMF can be obtained as follows: For each value :math:`y` of :math:`Y`

		#. Collect all possible values for which :math:`\{x | g(x)=y\}`
		#. Utilize axiom 3 to obtain :math:`p_Y(y)=\sum_{\{x | g(x)=y\}} p_X(x)`

Expectation and Variance
======================================================
.. note::
	* We can define **Expectation** of :math:`X` as :math:`\mathbb{E}[X]=\sum_x x p_X(x)` (assuming that the sum exists).
	* Elementary properties of expectation:

		* If :math:`X>0`, then :math:`\mathbf{E}[X]>0`.
		* If :math:`a\leq X\leq b`, then :math:`a\leq \mathbf{E}[X]\leq b`.
		* If :math:`X=c`, then :math:`\mathbf{E}[X]=c`.
	* We can define **Variance** of :math:`X` as :math:`\mathbb{V}(X)=\mathbb{E}[(X-\mathbb{E}[X])^2]`.

Law of The Unconscious Statistician (LOTUS)
-----------------------------------------------------
.. tip::
	* For expectation of :math:`Y=g(X)`, we can get away without having to compute PMF explicitly for :math:`Y`, as it can be shown that

		.. math:: \mathbb{E}[g(X)]=\sum_x g(x)p_X(x)

	* With the help of LOTUS, :math:`\mathbb{V}(X)=\sum_x (x-\mathbb{E}[X])^2 p_X(x)`.

Moments of a rv
---------------------------
.. note::
	* The *n-th moment* of :math:`X` is defined as :math:`\mathbb{E}[X^n]`.
	* Variance in terms of moments: :math:`\mathbb{V}(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2`.

Expectations of linear functions of rv
--------------------------------------------------------
.. note::
	For linear functions of :math:`X`, :math:`g(X)=aX+b`

	* :math:`\mathbb{E}[aX+b]=a\mathbb{E}[X]+b`.
	* :math:`\mathbb{V}(aX+b)=a^2\mathbb{V}(X)`.

Variance of bounded rv
--------------------------------------------------------
.. tip::
	* For bounded rvs :math:`a\leq X\leq b`, the variance is bounded as

		.. math:: \mathbb{V}(X)\leq\frac{(b-a)^2}{4}
	* Proof Hint:

		* The expression :math:`\mathbb{E}[(X-\gamma)^2]` is minimised when :math:`\gamma=\mathbb{E}[X]`
		* Therefore, :math:`\mathbb{V}(X)\leq\mathbb{E}\left[\left(X-\frac{a+b}{2}\right)^2\right]=\mathbb{E}[(X-a)(X-b)]+\frac{(b-a)^2}{4}`
		* :math:`a\leq X\leq b\implies (X-a)(X-b)\leq 0\implies \mathbb{E}[(X-a)(X-b)]\leq 0`

Expectations of general functions of rv
--------------------------------------------------------
..  warning::
	For non-linear functions, it is generally **not** true that :math:`\mathbb{E}[g(X)]=g(\mathbb{E}[X])`.

Jensen's inequality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. attention::
	* If :math:`g` is convex, :math:`\mathbb{E}[g(X)]\geq g(\mathbb{X}[X])`.
	* If :math:`g` is concave, :math:`\mathbb{E}[g(X)]\leq g(\mathbb{X}[X])`.

Multiple discrete random variables
======================================================
.. note::
	* We can define the joint-probability mass function for 2 rvs as 

		.. math:: p_{X,Y}(x,y)=\mathbb{P}(\{X=x\}\cap\{Y=y\})=\mathbb{P}(X=x,Y=y).

	* The **marginal probability** is defined as :math:`p_X(x)=\sum_y p_{X,Y}(x,y)` (similarly for :math:`p_Y(y)`.).
	* LOTUS holds, i.e. for :math:`g(X,Y)`, :math:`\mathbb{E}[g(X,Y)]=\sum_{x,y} g(x,y) p_{X,Y}(x,y)`.
	* Linearity of expectation holds, i.e. :math:`\mathbb{E}[aX+bY+c]=a\mathbb{E}[X]+b\mathbb{E}[Y]+c`.
	* Extends naturally for more than 2 rvs.

Conditioning
======================================================
.. note::
	* A discrete rv can be conditioned on an event :math:`A` (when :math:`\mathbb{P}(A)>0`) and its conditional PMF is defined as 

		.. math:: p_{X|A}(x)=\mathbb{P}(X=x|A).

	* Extends to the case when the event is defined in terms of another discrete rv, i.e. :math:`A=\{Y=y\}` with :math:`p_Y(y)>0` and is written as

		.. math:: p_{X|Y}(x|y)=\mathbb{P}(X=x|Y=y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}

	* Connects to the joint PMF as :math:`p_{X,Y}(x,y)=p_Y(y)p_{X|Y}(x|y)`	

Bayes theorem
--------------------------------------------
.. tip::
	* For :math:`p_Y(y)>0`, :math:`p_{Y|X}(y|x)=\frac{p_Y(y)p_{X|Y}(x|y)}{\sum_y p_Y(y)p_{X|Y}(x|y)}`
	* :math:`p_Y(y)` is known as **prior**, :math:`p_{Y|X}(y|x)` is called **posterior**, and :math:`p_{X|Y}(x|y)` is known as **likelihood**. 
	* The denominator :math:`Z=\sum_y p_Y(y)p_{X|Y}(x|y)` is the probability normalisation factor (i.e. it ensures that the sum is 1).
	* We can often work with unnormalised probabilities when exact values are not required, as :math:`p_{Y|X}(y|x)\propto p_Y(y)p_{X|Y}(x|y)`.

Total law of probability
--------------------------------------------
.. tip::
	* Let :math:`A_1,A_2,\cdots,A_n` be disjoints events such that :math:`\bigcup_{i=1}^n A_i=\Omega` (i.e. they define a partition).
	* If :math:`\mathbb{P}(A_i)>0` for all :math:`i`, then 
	
		.. math:: p_X(x)=\sum_{i=1}^n\mathbb{P}(A_i)p_{X|A_i}(x)

	* This also works if the events :math:`A_i` are defined in terms of another discrete rv (i.e. :math:`A_i=\{Y=y\}`)

		.. math:: p_{X}(x)=\sum_y p_Y(y)p_{X|Y}(x|y)

		* Note: This extends it to the countable infinite case from the finite case.

	* This allows us to compute the probability of events in a complicated probability model by utilising events from a simpler model, i.e. let's us use the divide-and-conquer technique. We just need to ensure that the events from the simpler model in fact exhausts the entirety of sample space of the original probability model.
	* For any other event :math:`B` where :math:`\mathbb{P}(A_i\cap B)>0` for all :math:`i`

		.. math:: p_{X|B}(x)=\sum_{i=1}^n\mathbb{P}(A_i|B)p_{X|A_i\cap B}(x)

Conditional expectation
--------------------------------------------
.. note::
	* Defined in terms of the conditional PMF, such as 

		* :math:`\mathbb{E}[X|A]=\sum_x x p_{X|A}(x)` and 
		* :math:`\mathbb{E}[X|Y=y]=\sum_x x p_{X|Y}(x|y)`
	* LOTUS holds, i.e. :math:`\mathbb{E}[g(X)|A]=\sum_x g(x)p_{X|A}(x)`.

.. tip::
	* Since we can have multivariable functions and joint distributions, we explicitly write the variables along with the expectation that are part of the PMF.
	* This means

		* :math:`\mathbb{E}_{X,Y}[f(X,Y)]=\sum_x\sum_yf(x,y)p_{X,Y}(x,y)`
		* :math:`\mathbb{E}_{X|Y}[f(X,Y)|Y=y]=\sum_xf(x,y)p_{X|Y}(x|y)`

.. attention::
	* :math:`\mathbb{E}[X]` is a constant.
	* We note that :math:`\mathbb{E}_{X|Y}[X|Y=y]` is just a function (not a rv) of a simple variable :math:`y\in\mathbb{R}`.

		* :math:`g(y)=\mathbb{E}_{X|Y}[X|Y=y]`
	* On the other hand, :math:`\mathbb{E}_{X|Y}[X|Y]` is a rv and it has the same PMF as :math:`Y`.

.. tip::
	From total law of probability:

	* For partitions :math:`A_1,A_2,\cdots,A_n`

		.. math:: \mathbb{E}[X]=\sum_x x p_X(x)=\sum_{i=1}^n \mathbb{P}(A_i)\sum_x x p_{X|A_i}(x)=\sum_{i=1}^n \mathbb{P}(A_i)\mathbb{E}[X|A_i]
	
	* For any other event :math:`B` where :math:`\mathbb{P}(A_i\cap B)>0` for all :math:`i`

		.. math:: \mathbb{E}[X|B]=\sum_{i=1}^n \mathbb{P}(A_i|B)\mathbb{E}[X|A_i\cap B]
	* If the events, :math:`A_i`, are represented by another discrete rv such that :math:`A_i=\{Y=y\}`

		.. math:: \mathbb{E}[X]=\sum_y p_Y(y)\mathbb{E}[X|Y=y]=\sum_y g(y)p_Y(y)=\mathbb{E}[g(Y)]=\mathbb{E}\left[\mathbb{E}[X|Y]\right] \text{, where $g(Y)=\mathbb{E}[X|Y]$.}

Law of iterated expectation
----------------------------------------
.. attention::	
	* For a single-valued function :math:`f(X)` of a rv, we have 

		.. math:: \mathbb{E}_X[f(X)]=\mathbb{E}_Y\left[\mathbb{E}_{X|Y}[f(X)|Y]\right]
	* For a multi-valued function :math:`f(X,Y)` of two jointly distributed rvs, we have

		.. math:: \mathbb{E}_{X,Y}[f(X,Y)]=\mathbb{E}_X\left[\mathbb{E}_{Y|X}[f(X,Y)|X]\right]=\mathbb{E}_Y\left[\mathbb{E}_{X|Y}[f(X,Y)|Y]\right]
	* Proof (first):

		.. math:: \mathbb{E}_X[f(X)]=\sum_xf(x)p_X(x)=\sum_xf(x)\left(\sum_yp_{X,Y}(x,y)\right)=\sum_xf(x)\left(\sum_yp_{Y}(y)p_{X|Y}(x|y)\right)=\sum_yp_{Y}(y)\left(\sum_xf(x)p_{X|Y}(x|y)\right)=\sum_yp_{Y}(y)\mathbb{E}_{X|Y}[f(X)|Y=y]=\mathbb{E}_Y\left[\mathbb{E}_{X|Y}[f(X)|Y]\right]
	* Proof (second:

		.. math:: \mathbb{E}_{X,Y}[f(X,Y)]=\sum_x\sum_yf(x,y)p_{X,Y}(x,y)=\sum_x\sum_yf(x,y)p_X(x)p_{Y|X}(y|x)=\sum_xp_X(x)\left(\sum_yf(x,y)p_{Y|X}(y|x)\right)=\sum_xp_X(x)\mathbb{E}_{Y|X}[f(X,Y)|X=x]=\mathbb{E}_X\left[\mathbb{E}_{Y|X}[f(X,Y)|X]\right]

Notion of Independence
======================================================
.. note::
	* :math:`X` is independent of an event :math:`A` iff :math:`p_{X|A}(x)=p_X(x)` for all :math:`x`.
	* Two rvs are independent when :math:`p_X(x)=p_{X|Y}(x|y)` and :math:`p_Y(y)=p_{Y|X}(y|x)` hold for all values of :math:`x` and :math:`y`.
	* Two independent rvs are written with the notation :math:`X\perp\!\!\!\perp Y`.
	* If :math:`X\perp\!\!\!\perp Y`, :math:`p_{X,Y}(x,y)=p_X(x)p_Y(y)` for all :math:`x` and :math:`y`.

Expectation and variance for independent rvs
------------------------------------------------------
.. note::
	* :math:`\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]`
	* :math:`\mathbb{V}(X+Y)=\mathbb{V}(X)+\mathbb{V}(Y)`
	* Extends naturally to more than 2 rvs.

Mean and variance of sample mean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. attention::
	* Let :math:`X_1,\cdots,X_n` be a sample of size :math:`n`.
	* We assume that these rvs 

		* are **independent**.
		* have **common mean** :math:`\mu` and **common variance** :math:`\sigma^2`.		
	* The sample mean is the rv :math:`M_n=\frac{1}{n}\sum_{i=1}^n X_i`.
	* Mean of :math:`M_n`:

		.. math:: \mathbb{E}[M_n]=\mathbb{E}\left[\frac{1}{n}\sum_{i=1}^n X_i\right]=\frac{1}{n}\sum_{i=1}^n\mathbb{E}[X_i]=\frac{1}{n}\sum_{i=1}^n\mu=\mu

		* Note: We've only used linearity of expectation.
	* Variance of :math:`M_n`:

		.. math:: \mathbb{V}[M_n]=\mathbb{V}\left[\frac{1}{n}\sum_{i=1}^n X_i\right]=\frac{1}{n^2}\sum_{i=1}^n\mathbb{V}[X_i]=\frac{1}{n^2}\sum_{i=1}^n\sigma^2=\frac{\sigma^2}{n}

		* Note: We've used the independence assumption here.

.. note::
	* Note: We **don't required them to be identically distributed**.
	* This is useful in establishing WLLN along with Chebyshev's inequality.

Some discrete random variables
======================================================
Bernoulli
-------------------------------------
Any experiment that deals with a binary outcome (e.g. **success** or **failure**) can be represented by a Bernoulli rv. 

.. note::
	* We can define a rv :math:`X=1` which represents success and :math:`X=0` which represents failure.
	* We only need to know about one of the probability values, :math:`\mathbb{P}(X=1)=p`, as :math:`\mathbb{P}(X=0)=1-p`.
	* Therefore, a Bernoulli rv is parameterised with just 1 parameter, :math:`p`.
	* [Derive] For :math:`X\sim\mathrm{Ber}(p)`, :math:`\mathbb{E}[X]=p` and :math:`\mathbb{V}(X)=p(1-p)`.

.. tip::
	* For any set of events :math:`A_1,A_2,\cdot A_n`, we can use **indicator functions** to denote the same.
	* Indicator functions are Bernoulli rvs which are defined

		.. math::
			X_i =
			  \begin{cases}
			    1 & \text{if $A_i$ occurs} \\
			    0 & \text{otherwise}
			  \end{cases}
	* Under this setup, :math:`\mathbb{P}(A_i)=\mathbb{E}[X_i]`.	

Multinoulli
-------------------------------------
Any experiment that deals with a categorical outcome can be represented by a Multinoulli rv.

.. note::
	* If the rv :math:`X` takes the values from the set :math:`\{x_1,\cdots,x_k\}`, then :math:`X\sim\mathrm{Multinoulli}(p_1,\cdots,p_k)`.
	* We can do away with :math:`k-1` parameters instead of :math:`k`, as :math:`\sum_{i=1}^k p_i=1`.
	* Bernoulli is a special case of Multinoulli where :math:`k=2`.

Uniform
-------------------------------------
TODO

Binomial
-------------------------------------
In a repeated (:math:`n`-times) Bernoulli trial with parameter :math:`p`, let :math:`X` denote the total number of **successes**. Then :math:`X\sim\mathrm{Bin}(n,p)` and the PMF is given by

.. math::
	p_X(x)={n \choose x} p^x(1-p)^{n-x}

.. attention::
	Prove that :math:`\sum_{x=0}^n p_X(x)=1`.

.. note::
	We can write a Binomially distributed rv as a sum of independent, Bernoulli rvs. 

	* Let's denote each of the trials with a different Bernoulli rv, :math:`X_i\sim\mathrm{Ber}(p)` for :math:`i`-th trial. 
	* Then :math:`Y=X_1+\cdots+X_n` is the total number of successes, :math:`X_i\perp\!\!\!\perp X_j` for :math:`i\neq j`.
	* [Derive] For :math:`X\sim\mathrm{Bin}(n,p)`, :math:`\mathbb{E}[X]=np` and :math:`\mathbb{V}(X)=np(1-p)`.
	* Hint:

		* For mean, utilise the linearity of expectation (does not require independence).
		* For variance, utilise independence in the sum of rvs.

..  tip::
	Solving a problem with an exisitng framework often requires us to think of a process with which the experiment takes place. With the right process description, seemingly difficult problems often become easy.

The Birthday Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
..  attention::
	In a party of :math:`500` guests, what is the probability that you share your birthday with :math:`5` other people?

	* All birthdays are equally likely (assumption of the underlying probability model).
	* Person A's birthday is independent of person B's birthday.
	* [The process] To find out the number of people who share their birthday with me, I can

		* pick a person at random and ask their birthday
		* I consider it a success if their birthday is the same as mine, failure otherwise
		* repeat for all :math:`n`

	* Total number of successes represents the total number of people who share their birthday with me.

The Hat Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. attention::
	There are :math:`n` people with numbered hats. They throw all their hats into a basket and then pick up one hat one by one. What is the expected number of people who get their own hat back? What is the variance of this?

	* Let :math:`X_i=1` if :math:`i`-th person get their hat back in the process, and :math:`X_i=0` otherwise.
	* Total number of people who get their own hat back is given by :math:`Y=X_1+X_2+\cdots+X_n`.
	* This looks like the case for Binomial distribution but it's not.
	* **[IMPORTANT]** In this case, the rvs are not independent. 
	
		* To see why, let's take :math:`n=2`.
		* The unconditional probabilities :math:`\mathbb{P}(X_1=1)=\mathbb{P}(X_2=1)=\frac{1}{2}`. 
		* But, if :math:`X_1=1`, then :math:`\mathbb{P}(X_2=1|X_1=1)=1`. If :math:`X_1=0`, then :math:`\mathbb{P}(X_2=1|X_1=0)=0`.
	* However, each person is equally likely to get their own hat back if they're the first to pick.
	* **[IMPORTANT]** Therefore, for the unconditional probability, for any :math:`i`, :math:`\mathbb{P}(X_i=1)=\mathbb{P}(X_1=1)=\frac{1}{n}`.
	* The expectation can therefore be calculated by

		.. math:: \mathbb{E}[Y]=\mathbb{E}[X_1+\cdots+X_n]=\sum_{i=1}^n\mathbb{E}[X_i]=\sum_{i=1}^n\mathbb{E}[X_1]=n\cdot\frac{1}{n}=1
	* For the variance, we calculate :math:`\mathbb{E}[Y^2]` as follows:

		.. math:: \mathbf{E}[Y^2]=\mathbf{E}[(X_1+\cdots+X_n)^2]=\underbrace{\sum_{i=1}^n\mathbf{E}[X_i^2]}_\text{$n$ terms} + \underbrace{\sum_{i=1}^n\sum_{j=1|i\neq j}^n\mathbf{E}[X_i X_j]}_\text{$n^2-n$ terms}=\sum_{i=1}^n X_i^2\mathbb{P}(X_i)+\sum_{i=1}^n\sum_{j=1|i\neq j}^n X_i X_j\mathbb{P}(X_i,X_j)
	* For the first term:
	
		* We can ignore the case where :math:`X_i=0` as :math:`X_i^2=0` as well.
		* Also, :math:`X_i^2=1` when :math:`X_i=1`.
		* The first term becomes :math:`\sum_{i=1}^n 1\cdot\mathbb{P}(X_1=1)=n\cdot\frac{1}{n}=1`.
	* For the second term:

		* We ignore the cases when either of :math:`X_i` or :math:`X_j` are 0.
		* **[IMPORTANT]** For :math:`X_i=1,X_j=1`, by symmetry argument similar to above, we can conclude that for any :math:`i\neq j`

		.. math:: \mathbb{P}(X_i=1,X_j=1)=\mathbb{P}(X_1=1,X_2=1)=\mathbb{P}(X_1=1)\mathbb{P}(X_2=1|X_1=1)=\frac{1}{n}\cdot\frac{1}{n-1}

Geometric
-------------------------------------
The number of repeated Bernoulli trials we need until we get a success can be modelled using a Geometric distribution. Let the Bernoulli trails have parameter :math:`p`. Then :math:`X\sim\mathrm{Geom}(p)` and the PMF for :math:`X=1,\cdots` is given by

.. math:: p_X(x)=(1-p)^x p

.. attention::
	Prove that :math:`\sum_{x=1}^\infty p_X(x)=1`.

.. note::
	* Geometric rvs have a memorylessness property. Even if we know that the first trial was a failure, it doesn't tell us anything about the remaining number of trials required to get a success. 
	* The remaining number of trials follows the same geometric distribution.
	* This fact is useful for obtaining the mean and variance of geometric rvs.

		* Suppose the first trial was a failure. This is represented by the conditional rv :math:`X|X>1`.
		* Let the remaining number of trials until first success is represented by :math:`Y`. Clearly, :math:`X|X>1=Y+1` and :math:`\mathbb{E}[X|X>1]=\mathbb{E}[Y]+1`.
		* By the memorylessless property, :math:`Y\sim\mathrm{Geom}(p)` as well. Therefore, :math:`\mathbb{E}[Y]=\mathbb{E}[X]`.
		* We use the fact to compute the conditional expectation, :math:`\mathbb{E}[X|X>1]=1+\mathbb{E}[X]`.
	* [Derive] For :math:`X\sim\mathrm{Geom}(p)`, :math:`\mathbb{E}[X]=\frac{1}{p}` and :math:`\mathbb{V}(X)=\frac{1-p}{p^2}`.
	* Hint:

		* Use divide-and-conquer by splitting the case where :math:`X=1` and :math:`X>1`.
		* Utilise the total expectation law as :math:`\mathbb{E}[X]=\mathbb{P}(X=1)\mathbb{E}[X|X=1]+\mathbb{P}(X>1)\mathbb{E}[X|X>1]`

Multinomial
-------------------------------------
Like Binomial, Multinomial describes the joint distribution of counts of different possible values for of :math:`n` repeated Multinoulli trials. 

.. note::
	* Let :math:`Y\sim\mathrm{Multinoulli}(p_1,\cdots,p_k)` where :math:`Y=\{y_1,\cdots,y_k\}`. 
	* Let :math:`X_i` be rv represending the number of times :math:`y_i` occurs.
	* These rvs are not independent.
	* The joint PMF for all such rvs is given by the Multinomial distribution, i.e. :math:`X_1,\cdots,X_k\sim\mathrm{Multinomial}(p1,\cdots,p_k)`

		.. math:: p_{X1,\cdots,X_k}(x_1,\cdots,x_k)={n \choose {x_1,\cdots,x_k}} p_1^{x_1}\cdots p_k^{x_k}
	* Note that the individual rvs have a Binomial distribution, :math:`X_i\sim\mathrm{Bin}(n, p_i)`.

Poisson
-------------------------------------
If a Binomial rv has :math:`n\to\infty` and :math:`p\to 0`, we can approximate it using another rv with an easier-to-manipulate distribution. For :math:`\lambda=n\cdot p`, :math:`X\sim\mathrm{Poisson}(\lambda)` (:math:`\lambda>0`), the PMF is given by 

.. math:: p_X(x)=e^{-\lambda}\frac{\lambda^x}{x!}

.. attention::
	Prove that :math:`\sum_{x=0}^\infty p_X(x)=1`.

.. tip::
	* It is useful to model a specific, time-dependent outcome given just the average.
	* [Derive] For :math:`X\sim\mathrm{Poisson}(\lambda)`, :math:`\mathbb{E}[X]=\lambda` and :math:`\mathbb{V}(X)=\lambda`.
	* Hint: 

		* For mean, reindex the terms in the sum.
		* For the variance, reindex terms in :math:`\mathbb{E}[X^2]` to evaluate :math:`\lambda\mathbb{E}[X+1]`.

.. attention::
	[The Birthday Problem] As the value of :math:`p` is quite low and :math:`n` is quite high, we can model this as a Poisson rv as well.

*********************************************
Continuous Random Variable
*********************************************

Continuous = values are from an uncountable subset of :math:`\mathbb{R}`.

Probability density function
=========================================
.. note::
	* When the set is uncountable, the probability :math:`\mathbb{P}(X=x)` of each individual such values :math:`x` is 0. 
	* Therefore, the probabilistic interpreration has to work with a subset of the real line :math:`B\subset\mathbb{R}`.
	* We define a probability density function (PDF), :math:`f_X(x)\geq 0`, such that

		.. math:: \mathbb{P}(X\in B)=\int\limits_{B} f_X(x)\mathop{dx}.
	* This term is well defined when

		* :math:`B` can be represented as the union of a countable collection of intervals.
		* :math:`f_X` is a continuous/piecewise continuous function with at most countable number of points of discontinuity.
	* We say a rv is continuous for which such PDF can be defined.

.. tip::
	* For the simplest case when :math:`B` is an interval, :math:`[a,b]`, then :math:`\mathbb{P}(a\leq X\leq b)=\int\limits_a^b f_X(x)\mathop{dx}`.	
	* Since individual points have 0 probability

		.. math:: \mathbb{P}(a\leq X\leq b)=\mathbb{P}(a\leq X< b)=\mathbb{P}(a< X\leq b)=\mathbb{P}(a< X< b).
	* Normalisation property holds, i.e.

		.. math:: \mathbb{P}(-\infty< X<\infty)=\int\limits_{-\infty}^\infty f_X(x)\mathop{dx}=1.

Probabilistic interpretation
---------------------------------------------------
.. note::
	To understand why it is called a density

		* We consider an interval :math:`[x,x+\delta]`, for some small :math:`\delta>0`. 
		* Assuming that :math:`f_X(x)` is "well behaved" (its values doesn't jump around fanatically), we assume that it stays (almost) constant for this entire interval.
		* Therefore, :math:`\mathbb{P}(X\in[x,x+\delta])=\int\limits_x^{x+\delta} f_X(t)\mathop{dt}\approx f_X(x)\cdot\delta`.
		* Hence, :math:`f_X(x)` can be thought of "probability per unit length".

.. attention::
	* A PDF can take arbitrarily large values as long as the normalisation property holds, e.g.

		.. math::
			f_X(x) =
			  \begin{cases}
			    \frac{1}{2\sqrt(x)} & \text{if $0 < x \leq 1$} \\
			    0 & \text{otherwise}
			  \end{cases}

Expectation and Variance
=========================================================
We can define Expectation of as :math:`\int\limits_{-\infty}^\infty x f_X(x) \mathop{dx}` (assuming that the integral exists and is bounded).

.. attention::
	* Expectation is well-defined when :math:`\int\limits_{-\infty}^\infty \left|x \right| f_X(x) \mathop{dx} < \infty`.
	* Example where the expectation isn't defined

		.. math:: f_X(x)=\frac{c}{1+x^2}

	  where :math:`c` is a normalisation constant to make it a valid PDF.

.. tip::
	* LOTUS holds, even when :math:`g(X)` is a discrete-valued function.
	* Variance can be defined as usual.

Centerisation, standardisation, skewness and kurtosis
------------------------------------------------------------------
.. attention::
	* We denote :math:`\tilde{X}=X-\mathbb{E}[X]` as the **centered** version of :math:`X`.
	
		* We also have :math:`\mathbb{E}[\tilde{X}]=\mathbb{E}[X-\mathbb{E}[X]]=0`.

	* Variance is the 2nd moment of centered rv :math:`\mathbb{V}(X)=\mathbb{E}[\tilde{X}^2]`.
	* We denote :math:`Z=\frac{X-\mathbb{E}[X]}{\sqrt{\mathbb{V}(X)}}=\frac{\tilde{X}}{\sqrt{\mathbb{E}[\tilde{X}^2]}}` as the **standardised** version of :math:`X`.

		* We note that :math:`\mathbb{E}[Z]=0` and :math:`\mathbb{E}[Z^2]=\mathbb{E}\left[\left(\frac{\tilde{X}}{\sqrt{\mathbb{E}[\tilde{X}^2]}}\right)^2\right]=\frac{\mathbb{E}[\tilde{X}^2]}{\mathbb{E}[\tilde{X}^2]}=1`.
	* Skewness is the 3rd moment of **standardised** rv, :math:`\mathrm{skew}(X)=\mathbb{E}[Z^3]`.

		* Skewness is a way to describe the shape of a probability distribution. It tells us if the distribution is lopsided. 
	
			* If the skewness is positive, the distribution has a longer tail on the right. 
			* If it’s negative, the distribution has a longer tail on the left.
	* Kurtosis is the 4th moment of **standardised** rv, :math:`\mathrm{kurt}(X)=\mathbb{E}[Z^4]`.

		* Kurtosis comes from the Greek word for bulging.
		* Kurtosis describes how a probability distribution is shaped. It tells us about the distribution’s tails and its peak. 

			* If kurtosis is positive, the distribution has heavy tails and a sharp peak. 
			* If it’s negative, the distribution has light tails and a flat peak.

.. tip::
	* Note that :math:`\mathbb{E}[X^2]=0` signifies that :math:`X=0` with probability 1. This is a useful trick in many calculations.

Cauchy-Schwarz inequality
---------------------------------------
.. note::
	* We define the inner product between two rvs :math:`X` and :math:`Y` as :math:`\langle X,Y\rangle=\mathbb{E}[XY]`.

		* TODO: Understand why this is a valid definition for an inner product.
	* We can define the norm induced by this inner product as :math:`\left\| \cdot \right\|_{\text{norm}}`, such that

		.. math:: \langle X,X\rangle=\left\| X \right\|_{\text{norm}}^2=\mathbb{E}[X^2]
	* Then Cauchy-Schwarz inequality becomes

		.. math:: |\langle X,Y\rangle|^2\leq \left\| X \right\|_{\text{norm}}^2\cdot\left\| Y \right\|_{\text{norm}}^2\implies \left(\mathbb{E}[XY]\right)^2\leq\mathbb{E}[X^2]\cdot\mathbb{E}[Y^2]

	* Direct proof without involving Cauchy-Schwarz:

		* For :math:`\mathbb{E}[Y^2]=0`, we have :math:`\mathbb{P}(Y=0)=1`. In that case the above is satisfied.
		* For :math:`\mathbb{E}[Y^2]\neq 0`, the proof follows from the observation that
		
			.. math:: \mathbb{E}\left[\left(X-\frac{\mathbb{E}[XY]}{\mathbb{E}[Y^2]}Y\right)^2\right]\geq 0

Cumulative distribution function
=========================================================
Regardless of whether a rv is discrete or continuous, there event :math:`\{X\leq x\}` has well defined probability.

.. note::
	We can define a **cumulative distribution function** (CDF) for any rv as 

		.. math::
			F_X(x)=\mathbb{P}(X\leq x)=\begin{cases}
			    \sum_{k\leq x} p_X(k), & \text{if $X$ is discrete} \\
			    \int\limits_{-\infty}^x f_X(x) \mathop{dx}, & \text{if $X$ is continuous}
			  \end{cases}

Properties of CDF
--------------------------------------------------
.. attention::
	* Monotonic: The CDF :math:`F_X(x)` is non-decreasing. If :math:`x_1<x_2`, then :math:`F_X(x_1)\leq F_X(x_2)`.
	* Normalised: We have :math:`\lim\limits_{x\to -\infty} F_X(x)=0` and :math:`\lim\limits_{x\to \infty} F_X(x)=1`.
	* Right-continuous: We have :math:`F_X(x)=F_X(x^+)` for all :math:`x`, where

		.. math:: F_X(x^+)=\lim\limits_{y\to x, y > x} F_X(y)

	* Let :math:`X\sim F_X` and :math:`Y\sim G_Y`. We have

		.. math:: \forall x\in\mathbb{R}. F_X(x)=G_Y(x)\implies \forall \omega\in\Omega. \mathbb{P}(X\in \omega)=\mathbb{P}(Y\in \omega)

.. seealso::
	* :math:`F_X` is
		* piecewise continuous, if :math:`X` is discrete.
		* continuous, if :math:`X` is continuous.
		* This explains why, in general, :math:`F_X` can only have countable points of discontinuity.
	* If :math:`X` is discrete and takes integer values, then :math:`F_X(k)=\sum_{-\infty}^k p_X(k)` and :math:`p_X(k)=F_X(k)-F_X(k-1)`.
	* If :math:`X` is continuous, then :math:`F_X(x)=\int\limits_{-\infty}^x f_X(x) \mathop{dx}` and :math:`f_X(x)=\frac{dF_X}{\mathop{dx}}(x)`.

.. tip::
	We can work with a **mixed** rv that takes discrete values for some and continuous values for others if we work with the CDF.

Multiple continuous random variables
=========================================================
Similar to the single continuous variable case, we say that two rvs, :math:`X` and :math:`Y` are **jointly continuous** if we can define an associated joint PDF :math:`f_{X,Y}(x,y)\geq 0` for any subset :math:`B\subset\mathbb{R}^2`, such that :math:`\mathbb{P}((x,y)\in B)=\iint\limits_{(x,y)\in B} f_{X,Y}(x,y) d(x,y)`.

.. tip::
	* For the simple case when :math:`B=[a,b]\times [c,d]`, and when Fubini's theorem applies, then

		.. math:: \mathbb{P}(a\leq X\leq b, c\leq Y\leq d)=\int\limits_a^b\int\limits_c^d f_{X,Y}(x,y) \mathop{dx} \mathop{dy}=\int\limits_c^d\int\limits_a^b f_{X,Y}(x,y) \mathop{dy} \mathop{dx}
	* Normalisation property holds.

		.. math:: \int\limits_{-\infty}^\infty\int\limits_{-\infty}^\infty f_{X,Y}(x,y)\mathop{dx} \mathop{dy}=1

Probabilistic interpretation
---------------------------------------------------
.. note::
	* For some small :math:`\delta>0` and :math:`\epsilon>0`, we consider the rectangular area :math:`[x,x+\delta]\times[y,y+\epsilon]`.
	* Assuming that :math:`f_{X,Y}` is "well behaved", we can assume that it stays (almost) constant within this small rectangular region.
	* Therefore
	
		.. math:: \mathbb{P}(x\leq X\leq x+\delta, y\leq Y\leq y+\epsilon)=\int\limits_x^{x+\delta}\int\limits_y^{y+\epsilon}f_{X,Y}(t,v)\mathop{dt} \mathop{dv}\approx f_{X,Y}(x,y)\cdot\delta\cdot \epsilon.
	* Hence :math:`f_{X,Y}(x,y)` can be thought of as the joint probability per unit area.

.. warning::
	If :math:`X=g(Y)`, then the entire function :math:`f_{X,Y}` has an area of 0 in the :math:`\mathbb{R}^2` plane. Therefore, we cannot define a PDF which can represent probability per unit area. So :math:`X` and :math:`Y` cannot be **jointly** continuous even if they are **marginally** continuous (i.e. their marginal PDFs are well defined).

.. note::
	* The marginal probability is defined as :math:`f_X(x)=\int\limits_{-\infty}^\infty f_{X,Y}(x,y)\mathop{dy}` (similarly for :math:`f_Y(y)`).
	* We can define **joint CDF** as 

		.. math:: F_{X,Y}(x,y)=\mathbb{P}(X\leq x, Y\leq y)=\int\limits_{-\infty}^x \int\limits_{-\infty}^y f_{X,Y}(x,y) \mathop{dx} \mathop{dy}

		* PDF can be recovered from CDF as 

			.. math:: f_{X,Y}(x,y)=\frac{\partial^2 F_{X,Y}}{\partial x\partial x}(x,y).
	* Extends naturally for more than 2 rvs.
	* All the properties for expectation holds as usual.

Conditioning
=========================================================
A continuous rv can be conditioned on an event, or another rv, discrete or continuous.

Conditioning on an event
---------------------------------------------------
A continuous rv can be conditioned on an event :math:`A` with :math:`\mathbb{P}(A)>0` and we can define a conditional PDF :math:`f_{X|A}(x)` such that for any (measurable) subset :math:`B\in\mathbb{R}`

	.. math:: \mathbb{P}(X\in B|A)=\int\limits_B f_{X|A}(x) \mathop{dx}

.. note::
	* Normalisation property holds like normal PDFs, i.e. :math:`\int\limits_{-\infty}^\infty f_{X|A}(x) \mathop{dx}=1`.
	* When the event is defined with the same rv such as :math:`X\in A`, then 

		.. math:: 
			f_{X|X\in A}(x)=\begin{cases}
			\frac{f_{X}(x)}{\mathbb{P}(X\in A)}, & \text{if $X\in A$} \\
			0, & \text{otherwise}
			\end{cases}

Probabilistic interpretation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* We can think of a small interval around :math:`X=x` of width :math:`\delta`, so that :math:`X\approx x`.
	* Assuming that :math:`f_{X|A}(x)` stays the same within this interval

		.. math:: \mathbb{P}(x\leq X\leq x+\delta|A)=\frac{\mathbb{P}(x\leq X\leq x+\delta,A)}{\mathbb{P}(A)}=\frac{\int\limits_{\{x\leq t\leq x+\delta\}\cap A} f_X(t)\mathop{dt}}{\mathbb{P}(A)}=\begin{cases}\frac{f_X(x)}{\mathbb{P}(A)}\int\limits_x^{x+\delta} \mathop{dt}\approx f_{X|A}(x)\cdot\delta & \text{if $[x,x+\delta]\in A$}\\ 0 & \text{otherwise}\end{cases}

	* So, the conditional PDF represents conditional probability per unit length.
	* Conditional CDF can be defined as :math:`F_{X|A}(x)=\int\limits_{-\infty}^x f_{X|A}(x) \mathop{dx}`.
	* Jointly continuous rvs can be conditioned on an event :math:`C=\{x,y\}\in A` with :math:`\mathbb{P}(C)>0` as exactly like above.

Total probability theorem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. tip::
	* For a partition of the sample space :math:`A_1,\cdots,A_n`, with :math:`\mathbb{P}(A_i)>0` for all :math:`i`

		.. math:: F_X(x)=\sum_{i=1}^n \mathbb{P}(A_i) F_{X|A}(x)
	* Differentiating both sides, we can recover a formula involving PDFs as :math:`f_X(x)=\sum_{i=1}^n \mathbb{P}(A_i) f_{X|A}(x)`.

Conditioning on a rv
---------------------------------------------------
Conditioning on a continuous rv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A continuous rv :math:`X` can be conditioned on another continuous rv :math:`Y`, assuming that they are jointly continuous with CDF :math:`f_{X,Y}(x,y)` as long as :math:`f_Y(y)>0`.

.. note::
	* The conditional PDF is defined as :math:`f_{X|Y}(x|y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}`.

Probabilistic interpretation
""""""""""""""""""""""""""""""""""""""""""
.. note::
	* We can think of a small interval around :math:`X=x` of width :math:`\delta`, so that :math:`X\approx x`.
	* However, we cannot take the conditioning event as :math:`Y=y` as it has 0 probability.
	* Therefore, we must consider a small interval around :math:`Y=y` of width :math:`\epsilon` such that :math:`Y\approx y`.
	* Assuming that the joint and the marginal PDFs stay the same within this rectangular region, we have

		.. math:: \mathbb{P}(x\leq X\leq x+\delta|y\leq Y\leq y+\epsilon)=\frac{\mathbb{P}(x\leq X\leq x+\delta,y\leq Y\leq y+\epsilon)}{\mathbb{P}(y\leq Y\leq y+\epsilon)}\approx\frac{f_{X,Y}(x,y)\cdot\delta\cdot\epsilon}{f_Y(y)\cdot\epsilon}=\frac{f_{X,Y}(x,y)}{f_Y(y)}\cdot\delta=f_{X|Y}(x|y)\cdot\delta
	* The above doesn't depent on :math:`\epsilon` at all, and is well defined even if we assign to it the limit value 0.
	* The interpretation then works as conditional probability per unit length of the rv :math:`X`.

Definition of probability conditioned on an event with 0 probability
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
.. tip::
	Using above, we can define the conditional probability for any (measurable) subset :math:`B\in\mathbb{R}` as

		.. math:: \mathbb{P}(X\in B|Y=y)=\int\limits_B f_{X|Y}(x|y) \mathop{dx}

Conditioning on a discrete rv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If we have a mixed distribution with one discrete rv, :math:`K` and one continuous rv :math:`Y`, then we can define conditional PMF :math:`p_{K|Y}(k|y)` and conditional PDF :math:`f_{Y|K}(y|k)`.

Probabilistic interpretation
""""""""""""""""""""""""""""""""""""""""""
.. note::
	* We can think of a small interval around :math:`Y=y` of width :math:`\delta`, so that :math:`Y\approx y`.
	* Assuming that :math:`f_Y(y)` and :math:`f_{K|Y}(y)` stays the same within this interval

		.. math:: p_{K|Y}(k|y)=\frac{\mathbb{P}(K=k,y\leq Y\leq y+\delta)}{\mathbb{P}(y\leq Y\leq y+\delta)}=\frac{\mathbb{P}(K=k)\mathbb{P}(y\leq Y\leq y+\delta|K=k)}{\mathbb{P}(y\leq Y\leq y+\delta)}\approx\frac{p_K(k)f_{Y|K}(y|k)\cdot\delta}{f_Y(y)\cdot\delta}=\frac{p_K(k)f_{Y|K}(y|k)}{f_Y(y)}

Total probability theorem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* We recover the marginals as

		* :math:`f_Y(y)=\sum_{k}p_K(k)f_{Y|K}(y|k)` and 
		* :math:`p_K(k)=\int\limits_{-\infty}^\infty f_Y(y)p_{K|Y}(k|t) \mathop{dy}`.

Bayes theorem
---------------------------------------------------
There are 4 versions of Bayes theorem.

.. tip::
	* Discrete-discrete: Already discussed in the context of discrete rv.
	* Discrete-continuous: :math:`p_{K|Y}(k|y)=\frac{p_K(k)f_{Y|K}(y|k)}{f_Y(y)}`.

		* Example: detection of digital signal transmission with noise

	* Continuous-discrete: :math:`f_{X|K}(x|k)=\frac{f_X(x)p_{X|K}(x|k)}{p_K(k)}`.

		* Example: inference about bernoulli parameter

	* Continuous-continuous: :math:`f_{X|Y}(x|y)=\frac{f_X(x)f_{X|Y}(x|y)}{f_Y(y)}`.

Conditional expectation
--------------------------------------------
.. note::
	Conditional expectation and LOTUS with conditional PDFs work the same as the discrete case.

Notion of Independence
=========================================================
.. note::
	* Two jointly continuous rvs are considered independent (:math:`X\perp\!\!\!\perp Y`) if :math:`f_{X|Y}(x|y)=f_X(x)` for all :math:`x` for all :math:`y` where :math:`f_Y(y)>0`.
	* If :math:`X\perp\!\!\!\perp Y`, :math:`f_{X,Y}(x,y)=f_X(x)f_Y(y)` and :math:`F_{X,Y}(x,y)=F_X(x)F_Y(y)` for all :math:`x` and :math:`y`.

Some continuous random variables
=========================================================

Uniform
-------------------------------------

Exponential
-------------------------------------
TOD: explain the memorylessness property of the exponential and connection with geometric

Laplace
-------------------------------------
TOD: explain the memorylessness property of the exponential and connection with geometric

Gaussian
-------------------------------------
.. note::
	* We write :math:`X\sim\mathcal{N}(\mu,\sigma)` to represent an rv :math:`X\in\mathbb{R}` with Gaussian density, which is given by

		.. math:: f_X(x;\mu,\sigma)=\frac{1}{\sigma\sqrt{2\pi}}\exp(-\frac{1}{2\sigma^2}(x-\mu)^2)
	* :math:`\mu,\sigma\in\mathbb{R}` are the mean and standard-deviation parameters.	

Multivariate Gaussian
-------------------------------------
.. note::
	* We write :math:`X\sim\mathcal{N}(\boldsymbol{\mu},\boldsymbol{\Sigma})` to represent an rv :math:`X\in\mathbb{R}^d` with Gaussian density, which is given by

		.. math:: f_X(\mathbf{x};\boldsymbol{\mu},\boldsymbol{\Sigma})=(2\pi)^{-\frac{d}{2}}|\boldsymbol{\Sigma}|^{-\frac{1}{2}}\exp(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}))
	* :math:`\boldsymbol{\mu}\in\mathbb{R}^d` is the mean and :math:`\boldsymbol{\Sigma}\in\mathbb{R}^{d\times d}` is the covariance matrix.	

Important Properties of Gaussian Densities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note::
	* explain the shape of 2d normal density 
	* independent case - circles in contours
	* dependent case - parabolas in contours
	* gaussians are closed under linear transform
	* gaussians are closed under conditioning
