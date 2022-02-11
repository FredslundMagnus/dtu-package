
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
| <c>name</c>       | <d>str</d>        | <j>"fdsa"</j>     |
| <c>GPU</c>        | <d>bool</d>       | <e>False</e>      |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>b</c>          | <d>float</d>      | <f>2.0</f>        |
| <c>a</c>          | <d>int</d>        | <f>1</f>          |
| <c>d</c>          | <d>str</d>        | <j>"fd"</j>       |
| <c>k</c>          | <d>Param</d>      | <d>Param</d><k>(</k><j>"sdf sdf"</j><k>,</k> <c>s</c><k>=</k><f>78</f><k>)</k> |
| <c>l</c>          | <d>Param2</d>     | <d>Param2</d><k>(</k><j>"s f"</j><k>,</k> <f>5</f><k>,</k> <c>s</c><k>=</k><f>1</f><k>,</k> <c>d</c><k>=</k><j>"76f"</j><k>)</k> |
| <c>m</c>          | <d>Param3</d>     | <d>Param3</d><k>(</k><k>)</k> |

# Output

```
2.0 fd 3600 True
sdf sdf 2 78
```