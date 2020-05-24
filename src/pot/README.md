Problem ID:  pot

CPU Time limit:  1 second

Memory limit:  1024 MB

Difficulty:  1.3

## Problem Description 

The teacher has sent an e-mail to her students with the
    following task: “Write a program that will determine and output
    the value of `X` if given
    the statement:

and it holds that `\mathit{number}_1`, `\mathit{number}_2` to `\mathit{number}_ N` are integers, and
    `\mathit{pow}_1`,
    `\mathit{pow_2}` to
    `\mathit{pow}_ N` are
    one-digit integers.” Unfortunately, when the teacher downloaded
    the task to her computer, the text formatting was lost so the
    task transformed into a sum of `N` integers:

For example, without text formatting, the original task in
    the form of `X = 21^2 +
    125^3` became a task in the form of `X = 212 + 1253`. Help the teacher by
    writing a program that will, for given `N` integers from `P_1` to `P_ N` determine and output the value
    of `X` from the original
    task.

## Input

The first line of input contains the integer `N` (`1
    <= N <= 10`), the number of the addends from the
    task. Each of the following `N` lines contains the integer
    `P_ i` (`10 <= P_ i <= 9999`, `i = 1, \ldots , N`) from the
    task.

## Output

The first and only line of output must contain the value of
    `X` (`X <= 1\, 000\, 000\, 000`) from the
    original task.


<table class="sample" summary="sample data">
<tr>
<th>Sample Input 1</th>
<th>Sample Output 1</th>
</tr>
<tr>
<td>
<pre>2
212
1253
</pre>
</td>
<td>
<pre>1953566
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
<pre>5
23
17
43
52
22
</pre>
</td>
<td>
<pre>102
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
<pre>3
213
102
45
</pre>
</td>
<td>
<pre>10385
</pre>
</td>
</tr>
</table>
