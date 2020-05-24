Problem ID:  tarifa
CPU Time limit:  1 second
Memory limit:  1024 MB
Difficulty:  1.3

Tarifa

Pero has negotiated a Very Good data plan with his internet
    provider. The provider will let Pero use up $X$ megabytes to surf the internet per
    month. Each megabyte that he doesn’t spend in that month gets
    transferred to the next month and can still be spent. Of
    course, Pero can only spend the megabytes he actually has.

$X$

If we know how much megabytes Pero has spent in each of the
    first $N$ months of using
    the plan, determine how many megabytes Pero will have available
    in the $N + 1$ month of
    using the plan.

$N$

$N + 1$

Input

The first line of input contains the integer $X$ ($1
    \leq X \leq 100$). The second line of input contains the
    integer $N$ ($1 \leq N \leq 100$). Each of the
    following $N$ lines
    contains an integer $P_ i$
    ($0 \leq P_ i \leq 10\,
    000$), the number of megabytes spent in each of the
    first $N$ months of using
    the plan. Numbers $P_ i$
    will be such that Pero will never use more megabytes than he
    actually has.

$X$

$1
    \leq X \leq 100$

$N$

$1 \leq N \leq 100$

$N$

$P_ i$

$0 \leq P_ i \leq 10\,
    000$

$N$

$P_ i$

Output

The first and only line of output must contain the required
    value from the task.
