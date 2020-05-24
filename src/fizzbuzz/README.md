Problem ID:  fizzbuzz

CPU Time limit:  1 second

Memory limit:  1024 MB

Difficulty:  1.3

## Problem Description 


<img alt="/problems/fizzbuzz/file/statement/en/img-0001.png" class="illustration" src="https://open.kattis.com/problems/fizzbuzz/file/statement/en/img-0001.png"/>

Basically, this is how it works: you print the integers from
    `1` to `N`, replacing any of them divisible
    by `X` with Fizz or, if they are divisible by `Y`, with Buzz. If the number is divisible by both
    `X` and `Y`, you print FizzBuzz instead.

Check the samples for further clarification.

## Input

Input contains a single test case. Each test case contains
    three integers on a single line, `X`, `Y` and `N` (`1
    <= X < Y <= N <= 100`).

## Output

Print integers from `1`
    to `N` in order, each on
    its own line, replacing the ones divisible by `X` with Fizz, the ones divisible by `Y` with Buzz and ones divisible by both `X` and `Y` with FizzBuzz.


<table class="sample" summary="sample data">
<tr>
<th>Sample Input 1</th>
<th>Sample Output 1</th>
</tr>
<tr>
<td>
<pre>2 3 7
</pre>
</td>
<td>
<pre>1
Fizz
Buzz
Fizz
5
FizzBuzz
7
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
<pre>2 4 7
</pre>
</td>
<td>
<pre>1
Fizz
3
FizzBuzz
5
Fizz
7
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
<pre>3 5 7
</pre>
</td>
<td>
<pre>1
2
Fizz
4
Buzz
Fizz
7
</pre>
</td>
</tr>
</table>
