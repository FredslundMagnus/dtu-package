<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"local"</j>    |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>b</c>          | <d>float</d>      | <f>3.0</f>        |
| <c>a</c>          | <d>int</d>        | <f>1</f>          |
| <c>d</c>          | <d>str</d>        | <j>"fd"</j>       |
| <c>k</c>          | <d>Param</d>      | <d>Param</d><k>(</k><j>"sdf sdf"</j><k>,</k> <c>s</c><k>=</k><f>78</f><k>)</k> |

# Output

```
3.0 fd 3600 True
sdf sdf 78
```