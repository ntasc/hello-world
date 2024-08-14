In the following document, we prove that:

$${n-1 \choose k-1}+{n-1 \choose k} = {n \choose k}$$

Firstly, we see that for $n$ ranging from $0$ to $10$, and $k$ ranges from $0$ to $n$, this equality remains true:

```python
from binom import *

for i in range(1,11):
  n = i
  for j in range(1,i+1):
    k = j
    print(binom(n-1,k-1)+binom(n-1, k) == binom(n,k))
```

But this does not cover every case. we must perfrm a proof by induction on $k$. Let us start with $k=1$:

Now, 

$${n-1 \choose 0} = \frac{(n-1)!}{0!(n-1)!} = 1$$

$${n-1 \choose 1} = \frac{(n-1)!}{1!(n-2)!} = n-1$$

So, the LHS simplfies to $n$. 

$${n \choose 1} = \frac{n!}{1!(n-1)!}=n$$

So, this holds true for the base case $k=1$. Now, we assume it to be true up to $k = i $, and prove it true for $k = i + 1$:

$$
  {n - 1 \choose i - 1}+{n -1 \choose i} = {n \choose i} 
$$

We calculate the next term:

$$
   {n \choose  i}  + {n \choose i +1 } = \frac{n!}{i!(n-i)!} + \frac{n!}{(i+1)!(n-i-1)!} = \frac{n!}{i!(n-i)!} + \frac{n!}{i!(n-i)!} \cdot \frac{n-i}{i+1}
$$

We perform addition:

$$
  \frac{n!}{i!(n-i)!} \cdot \frac{1}{1} + \frac{n!}{i!(n-i)!} \cdot \frac{n-i}{i+1} = \frac{n!}{i!(n-i)!} \frac{(i+1)+(n-i)}{i+1} =\frac{n!}{i!(n-i)!} \frac{n+1}{i+1}
$$

Finally:

$$
  \frac{n!}{i!(n-i)!} \frac{n+1}{i+1}= \frac{(n+1)n!}{(i+1)i!(n+1-i-1)!}=\frac{(n+1)!}{(i+1)!((n+1)-(i+1))!} = {n+1 \choose i+1} 
$$

So, we see that this equality holds true for any $n, k \in \mathbb{Z}^+$
