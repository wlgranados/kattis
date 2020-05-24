Problem ID:  transitwoes

CPU Time limit:  1 second

Memory limit:  1024 MB

Difficulty:  1.3

## Problem Description 

Everyday Yraglac relies on his city’s local transit system
    to get to and from campus. Since this is routine for him, he’s
    memorized exactly what time will let him leave his house and
    make it in time to his first morning class. Of course transit
    being transit, they decided to change around the schedules for
    some of the routes Yraglac takes.

Yraglac leaves his house everyday at time `s` to make it to his first class
    which starts at time `t`.
    To get there, he takes `n`
    transit routes, one after the other. When transferring from one
    transit route to another, going from his house to the first
    transit stop, and going from the last transit stop to his
    class, he must walk for `d_
    i` time. Yraglac rides the `i-th` bus for `b_ i` time before getting off and
    walking to the `i+1`-th
    bus stop. Last but not least, each bus only comes at an
    interval of every `c_ i`.
    The first one always leaving at time `0`.

Given the new schedules for the routes Yraglac takes, can
    you find out if he can make it to class on time?

## Input

The first line contains `3` space separated integers,
    `0 <= s <= t <= 1\,
    000`, and `1 <= n <=
    20`.

The second line contains `n +
    1` space separated integers `d_ i` `(0 <= d_ i <= 1\, 000)` denoting
    the time it takes to walk from the `i`-th bus’ drop-off point to the
    `i+1`-th bus stop. Note
    that `d_0` is the time it
    takes to walk from Yraglac’s house to the first bus stop, and
    `d_ n` is the time it
    takes to walk from the last bus’ drop-off point to his
    class.

The third line contains `n` space separated integers
    `b_ i` `(1 <= b_ i <= 1\, 000)` denoting
    the amount of time Yraglac rides the `i`-th bus.

The fourth line contains `n` space separated integers
    `c_ i` `(1 <= c_ i <= 1\, 000)` denoting
    the intervals the `i`-th
    bus arrives.

## Output

Output “yes” if Yraglac will be able to get to class in
    time, and “no” otherwise.


<table class="sample" summary="sample data">
<tr>
<th>Sample Input 1</th>
<th>Sample Output 1</th>
</tr>
<tr>
<td>
<pre>0 20 2
2 2 2
5 5
3 5
</pre>
</td>
<td>
<pre>yes
</pre>
</td>
</tr>
</table>

<table class="sample" summary="sample data">
<tr>
<th>Sample Input 2</th>
<th>Sample Output 2</th>
</tr>
<tr>
<td>
<pre>0 10 1
3 3
1
8
</pre>
</td>
<td>
<pre>no
</pre>
</td>
</tr>
</table>
