# scripts_sparse

1. Begin with ||Dictionary*Alpha - y||sq + Tau||alpha|| for high and low and Determine yp or patch overlaps
2. Minimizer of overlapping patch errors through Beta||PDhigh*alpha-yp||sq where Beta is patch overlap factor (Tool: Matrix operations using Python)
3. The final equation makes use of the Orthogonal Matching Pursuit which can be access via Scikit Learn library of Python 
4. Dh: Atom acquisition from rndom sampling from the DEM for the dictionary using Yang et al 2008 Method
5. Dl: bicubic interpolation of the Dh samples from step 4. 
6. *
7. K-SVD on Python to Improve Dictionaries over time.

*Absorb: "The slope is extracted using Horn’s formula Horn (1981) to find the first or-
der derivatives in x and y direction. Roughness refers to the height variation
within a local neighborhood and can be measured in different ways using, e.g.,
the standard deviation or fractal dimension. We have experimented with several
methods and found the entropy to perform best for our purposes. The entropy
E(x, y) is defined as E(x, y) =
(p × log p), where p are the probability den-
sities of the heights, approximated by histogram counts. Each output grid cell
contains the entropy value of the surrounding n × n neighborhood. We point
out that the residuals vary (increase or decrease) in a non-random pattern with
the two extracted geomorphological parameters. We learn the mapping from a
parameter to the expected residual (accuracy) with Gaussian process regression.
An example is shown in Figure 2(b). After the mapping, we adjust the expected
residuals by linearly scaling the values between 0 and 100, eventually yielding
an accuracy map. In the last step, we normalize the resulting accuracy maps
of both input DEMs at each overlapping point. The reciprocal values are the
weights used for the fusion"


