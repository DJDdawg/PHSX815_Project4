# PHSX815_Project4

The idea of Project 4 is to tie in the course concepts (parameter estimation or hypothesis testing) with an actual Physics experiment.

My experiment measures the charge of an electron based upon the amount of Shot Noise in an electronic system.

**Parameter Estimation**

The Poisson distribution is utilized to generate random data in **Poisson.py**, 

$P(X | \lambda) = \frac{\lambda^{X} e^{- \lambda}}{X!}$.

The data can be generated with the following code.

>python3 Poisson.py -Nmeas xx -Nexp xx -lambda xx -output xx.txt

Where 'Nmeas' is the number of measurements per experiment, 'Nexp' is the total number of experiemnts, and 'lambda' is the parameter that describes the Poisson Distribution. 

One should note that 'lambda' has to be a positive, real number and that the Poisson Distribution will only return whole numbers for X. 

Various graphs for the Poisson Distribution are shown in **xxx.png**.

![GaussianGraph1.png](https://github.com/DJDdawg/PHSX815_Project3/blob/main/GaussianGraph1.png)

The likelihood for the Poisson Distribution is easily derived with Bayes Theorem.

$P(\lambda | X) \approx \prod_{i = 1}^{N_{meas}} P(X_{i} | \lambda) = \prod_{i = 1}^{N_{meas}} \frac{\lambda^{X_{i}} e^{- \lambda}}{X_{i}!}$

Taking the logarithm allows us to separate the products into summations,

$ln(P(\lambda | X)) =  ln(\prod_{i = 1}^{N_{meas}} \frac{\lambda^{X_{i}} e^{- \lambda}}{X_{i}!}) = -N_{meas} \lambda + ln(\lambda) \sum_{i = 1}^{N_{meas}} X_{i} - \sum_{i = 1}^{N_{meas}} X_{i}!$
