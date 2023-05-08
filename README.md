# PHSX815_Project4

The idea of Project 4 is to tie in the course concepts (parameter estimation or hypothesis testing) with an actual Physics experiment.

My experiment measures the charge of an electron based upon the amount of Shot Noise in an electronic system.

**Parameter Estimation**

The Poisson distribution is utilized to generate random data in **Poisson.py**, 

$P(X | \lambda) = \frac{\lambda^{X} e^{- \lambda}}{X!}$.

One should note that 'lambda' has to be a positive, real number and that the Poisson Distribution will only return whole numbers for X. 

Various graphs for the Poisson Distribution are shown in **PoissonGraphs.png**.

![PoissonGraphs.png](https://github.com/DJDdawg/PHSX815_Project4/blob/main/PoissonGraphs.png)

The likelihood for the Poisson Distribution is easily derived with Bayes Theorem.

$P(\lambda | X) \approx \prod_{i = 1}^{N_{meas}} P(X_{i} | \lambda) = \prod_{i = 1}^{N_{meas}} \frac{\lambda^{X_{i}} e^{- \lambda}}{X_{i}!}$

Taking the logarithm allows us to separate the products into summations,

$ln(P(\lambda | X)) =  ln(\prod_{i = 1}^{N_{meas}} \frac{\lambda^{X_{i}} e^{- \lambda}}{X_{i}!}) = -N_{meas} \lambda + ln(\lambda) \sum_{i = 1}^{N_{meas}} X_{i} - \sum_{i = 1}^{N_{meas}} X_{i}!$.

Taking a derivative allows us to find the maximum likelihood estimate for our parameter $\lambda$, 

$\frac{d ln(P(\lambda | X))}{d \lambda} = -N + \frac{1}{\lambda} \sum_{i = 1}^{N_{meas}} X_{i} = 0$.

Solving for $\lambda$ gives,

$\lambda_{most-likely} = \frac{1}{N_{meas}} \sum_{i = 1}^{N_{meas}} X_{i}$,

showing that our parameter is most likely to be the mean of all of the measurements in an experiment, which can easily be seen as the peak of the distribution in the Figure **PoissonGraphs.png**.
 
Numerical Parameter Estimation for each experiments is done using the function, scipy.optimize.minimize_scalar(), and is then averaged over many experiments to calculate the average value of $\lambda$ and its uncertainty, $\sigma_{\lambda}$. 

**Shot Noise**

The Poisson Distribution describes how many times you expect an event to occur given an average rate parameter $\lambda$. One example of the application of this phenomenon is that of Shot Noise. 

In electronics, current is due to the movement of electrons. For a  current of one ampere, the number of electrons that pass through a given part of a wire is approximately $6.25 * 10^{18}$ electrons per second. For currents of this magnitude, the fluctuation in the number of electrons per second is infitesimal. However, for small currents where only a few electrons pass through a part of the wire per second the fluctuation will be quite large. These fluctuations are shot noise. Shot noise is most commonly observed (and is the dominant form of the noise) for low currents that have been amplified. However, for most applications in electrons, shot noise is negligible when compared to other form of noise such as Johnson-Nyquist noise. 

**Experimental Procedure**

The data can be generated with the following code.

>python3 Poisson.py -Nmeas xx -Nexp xx -lambda xx -output xx.txt

Where 'Nmeas' is the number of measurements per experiment, 'Nexp' is the total number of experiemnts, and 'lambda' is the parameter that describes the Poisson Distribution. 

The data is the graphed with **PoissonPlot.py** and can be seen below in **PoissonData.png**

>python3 PoissonPlot.py -lambda xx -simpledata.txt

![PoissonData.png](https://github.com/DJDdawg/PHSX815_Project4/blob/main/PoissonData.png)

The code is then analyzed in **PoissonAnalysis.py** using the following:

>python3 PoissonAnalysis.py -Nmeas xx -Nexp xx -lambda xx
>
>Number of measurements/experiment: 10000
>
>Number of experiments: 100
>
>Log likelihood is maximized at x = 5.0 for the analytical solution
>
>Scipy minimization was successful: True
>
>Numerical x-value found to maximize log likelihood for experiment 1: xxx
>
>Maximimum log likelihood: xxx
>
>Numerical Mean value of all experiments: xxx ± xxx

It also produces the graphs **LogLikelihood.png** where the parameter is numerically estimated from a single experiment and compared to the analytical solution.

![LogLikelihood.png]()

Another graph produced is **MeanDistribution.png** where the parameter is estimated for all experiments and the distrubtion of parameters is graphed in a histogram. 

![MeanDistribution.png]()
