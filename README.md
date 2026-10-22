## Mathematical Proof (Cantor's Diagonal Argument)

### Algorithm

Given an array `nums` containing `n` unique binary strings, each of length `n`, construct a binary string `s` by flipping the diagonal characters.

For every index `i`, define:

$$
s_i =
\begin{cases}
1 & \text{if } nums[i][i] = 0, \\
0 & \text{if } nums[i][i] = 1.
\end{cases}
$$

In other words, each character `s[i]` is the opposite of `nums[i][i]`.

### Proof by Contradiction

Suppose, for the sake of contradiction, that the constructed string `s` appears in `nums`.

Then there must exist an index `k`, where `0 <= k < n`, such that:

$$
s = nums[k]
$$

Since the two strings are equal, all their corresponding characters must be equal. In particular, their characters at index `k` must satisfy:

$$
s_k = nums[k][k]
$$

However, by the construction of `s`, we deliberately flipped the character at that position. Therefore:

$$
s_k \neq nums[k][k]
$$

This is a contradiction.

Hence, the constructed string `s` cannot appear in `nums`.

Furthermore, since we construct exactly one binary character for each of the `n` indices, `s` has length `n`.

Therefore, **`s` is a valid binary string of length `n` that does not appear in `nums`.** Q.E.D.

### Complexity Analysis

- **Time Complexity:** `O(n)`, because we iterate through the array once.
- **Space Complexity:** `O(n)`, because the resulting string contains `n` characters.

### Conclusion

The algorithm guarantees a valid answer without generating all possible binary strings or searching the array. By flipping the diagonal characters, it ensures that the result differs from every input string in at least one position.

This technique is known as **Cantor's Diagonal Argument**.
