Problem ID:  tripletexting

CPU Time limit:  2 seconds

Memory limit:  1024 MB

Difficulty:  1.4

## Problem Description 

Julia enjoys talking to her grandma, playing with legos, and
    inventing two-player card games where she has a winning
    strategy. Recently however, she has not been able to talk to
    her grandma in person because of some kind of “pandemonium”.
    Instead, they have resorted to texting, which is a very slow
    process since grandma types very slowly and often mistypes
    letters. To make matters worse, grandma has started to write
    every word three times so that Julia can correct her mistypes.
    For example, if grandma wants to write the word “hello”, she
    will instead write “hellohellohello”. If she mistypes one of
    those letters, it might instead be sent as
    “hellohrllohello’.’

Your task is to write a program that given a message sent by
    grandma, where possibly one letter has been changed to some
    other letter, finds the original word.

## Input

The input consists of one string `s` containing lower case English
    letters (`3 <= |s| <=
    99`). This is the message sent by grandma. It is
    guaranteed that this string is the result of a word being
    written three times, where possibly one letter was changed to
    some other letter.

## Output

Output one string `t`,
    the original word.


<table class="sample" summary="sample data">
<tr>
<th>Sample Input 1</th>
<th>Sample Output 1</th>
</tr>
<tr>
<td>
<pre>hellohrllohello
</pre>
</td>
<td>
<pre>hello
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
<pre>hejhejhej
</pre>
</td>
<td>
<pre>hej
</pre>
</td>
</tr>
</table>
