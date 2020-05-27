Problem ID:  twostones

CPU Time limit:  1 second

Memory limit:  1024 MB

Difficulty:  1.2

## Problem Description 

Alice and Bob are playing a new game of stones. There are
    `N` stones placed on the
    ground, forming a sequence. The stones are labeled from
    `1` to `N`.

Alice and Bob in turns take exactly two consecutive stones
    on the ground until there are no consecutive stones on the
    ground. That is, each player can take stone `i` and stone `i+1`, where `1 <= i <= N - 1`. If the number
    of stone left is odd, Alice wins. Otherwise, Bob wins.

Assume both Alice and Bob play optimally and Alice plays
    first, do you know who the winner is?

## Input

The input contains an integer `N` `(1
    <= N <= 10\, 000\, 000)`, the number of stones.

## Output

Output the winner, “Alice” or
    “Bob” (without the quotes), on a
    line.


<table class="sample" summary="sample data">
<tr>
<th>Sample Input 1</th>
<th>Sample Output 1</th>
</tr>
<tr>
<td>
<pre>1
</pre>
</td>
<td>
<pre>Alice
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
<pre>2
</pre>
</td>
<td>
<pre>Bob
</pre>
</td>
</tr>
</table>

<table class="sample" summary="sample data">
<tr>
<th>Sample Input 3</th>
<th>Sample Output 3</th>
</tr>
<tr>
<td>
<pre>5
</pre>
</td>
<td>
<pre>Alice
</pre>
</td>
</tr>
</table>
