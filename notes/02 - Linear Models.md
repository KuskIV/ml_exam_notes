---
title: 02 - Linear Models
created: '2022-06-02T07:46:43.557Z'
modified: '2022-06-07T07:50:16.015Z'
---

# 02 - Linear Models

##### Data transformation
A mapping is when we transform the data from som representation into another. This can be defined like this:
$$\phi:\mathbb{R}^D \rightarrow \mathbb{R}^{D'}$$
Usually the transformed data has more dimensions than the original data.
It is also the case that it is typically non-linear. The new space created with the transformed data is called the feature space.

support vector machines are a type of linear model that can be used to predict the classes of the data.

Kernels can be defined, and SVM classifiers can be learned, for data with very different spaces.

The dot product $\phi(x)\cdot\phi(x')$ can be computed without actually constructing the vectors $\phi(x)$ and $\phi(x')$.

$K(x,x')=(x \cdot x' + 1 )^2$ is an example of a **kernel function**.
Kernel functions can be interpreted as measures of similarity between two vectors.

##### Kernel trick
The following strategy can be obtain for construction of kernelized SVM classifiers:
- **Given:** a classifier problem
- **Define:** similarity function between two vectors $\phi(x)$ and $\phi(x')$
$$K(x,x')$$
- **Verify:** That $k(x,x')$ is positive semi-definite
- **Learn:** an SVM classifier using the kernel trick 

##### Constructing Kernels

**Basic Kernels**
- Polynomial Kernel: $(x*z+1)^p$
- Gaussian Kernel: $e^{-\left \| x - z \right \| / 2\sigma^2}$
- Hyperbolic Tangent Kernel: $tanh(k*X*Z-\sigma)$

**Kernel Building Rules**
if $K(x,x')$ is positive semi-definite, then so is:
- $q(k(x,x'))$, where $q()$ is a polynomial with non-negative coefficients
- $e^{K(x,x')}$
- $K(x,x')K'(x,x')$, where $K'()$ is another positive definite.
- $\frac{K(x,x')}{\sqrt{K(x,x),K(x',x')}}$ the normalization of $K()$

##### Cosine similarity
$cos-sim(t_1,t_2)=cosine(\theta)=\frac{tf(t_1 \cdot tf(t_2))}{ \| tf(t_1) \|  \cdot \| tf(t_2) \|}$

cos-sim is a positive semi-definite kernel: Normalization of plain dot-product.

alternatively cos-sim is the dot-product of the feature vectors $tf(t)$ and $\| tf(t) \|$

cs-sim is extensively used in information retrieval as a measure of similarity between documents.
- $t_1$: a short query text
- $t_2$: a candidate document


##### SVM + Kernel functions:
- $+$ Powerful method for classification
- $+$ Successful applications
- $+$ Wide variety of data types and classification problems reduced to a single type of optimization problem
- $-$ Binary classifier only: Generalization to multi-class only via multiple binary classifiers
- $-$ Complexity quadratic in number of instances
- $-$ To find the "right" kernel function may require a lot of engineering.
