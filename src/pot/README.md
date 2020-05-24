Problem ID:  pot
CPU Time limit:  1 second
Memory limit:  1024 MB
Difficulty:  1.3

Pot

The teacher has sent an e-mail to her students with the
    following task: “Write a program that will determine and output
    the value of $X$ if given
    the statement:

$X$

\[ X =
    \mathit{number}_1^{\mathit{pow}_1} +
    \mathit{number}_2^{\mathit{pow}_2} + \ldots + \mathit{number}_
    N^{\mathit{pow}_ N} \]

and it holds that $\mathit{number}_1$, $\mathit{number}_2$ to $\mathit{number}_ N$ are integers, and
    $\mathit{pow}_1$,
    $\mathit{pow_2}$ to
    $\mathit{pow}_ N$ are
    one-digit integers.” Unfortunately, when the teacher downloaded
    the task to her computer, the text formatting was lost so the
    task transformed into a sum of $N$ integers:

$\mathit{number}_1$

$\mathit{number}_2$

$\mathit{number}_ N$

$\mathit{pow}_1$

$\mathit{pow_2}$

$\mathit{pow}_ N$

$N$

\[ X = P_1 + P_2 + \ldots + P_ N \]

For example, without text formatting, the original task in
    the form of $X = 21^2 +
    125^3$ became a task in the form of $X = 212 + 1253$. Help the teacher by
    writing a program that will, for given $N$ integers from $P_1$ to $P_ N$ determine and output the value
    of $X$ from the original
    task.

$X = 21^2 +
    125^3$

$X = 212 + 1253$

$N$

$P_1$

$P_ N$

$X$

Input

The first line of input contains the integer $N$ ($1
    \leq N \leq 10$), the number of the addends from the
    task. Each of the following $N$ lines contains the integer
    $P_ i$ ($10 \leq P_ i \leq 9999$, $i = 1, \ldots , N$) from the
    task.

$N$

$1
    \leq N \leq 10$

$N$

$P_ i$

$10 \leq P_ i \leq 9999$

$i = 1, \ldots , N$

Output

The first and only line of output must contain the value of
    $X$ ($X \leq 1\, 000\, 000\, 000$) from the
    original task.

$X$

$X \leq 1\, 000\, 000\, 000$
