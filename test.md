
<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

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

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"fdsa"</j>     |
| <c>GPU</c>        | <d>bool</d>       | <e>False</e>      |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>b</c>          | <d>float</d>      | <f>2.0</f>        |
| <c>a</c>          | <d>int</d>        | <f>1</f>          |
| <c>d</c>          | <d>str</d>        | <j>"fd"</j>       |
| <c>k</c>          | <d>Param</d>      | <d>Param</d><k>(</k><j>"sdf sdf"</j><k>,</k> <c>s</c><k>=</k>78<k>)</k> |
| <c>l</c>          | <d>Param2</d>     | <d>Param2</d><k>(</k><j>"s f"</j><k>,</k> <f>5</f><k>,</k> <c>s</c><k>=</k>1<k>,</k> <c>d</c><k>=</k>'76f'<k>)</k> | 

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"fdsa"</j>     |
| <c>GPU</c>        | <d>bool</d>       | <e>False</e>      |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>b</c>          | <d>float</d>      | <f>2.0</f>        |
| <c>a</c>          | <d>int</d>        | <f>1</f>          |
| <c>d</c>          | <d>str</d>        | <j>"fd"</j>       |
| <c>k</c>          | <d>Param</d>      | <d>Param</d><k>(</k>'sdf sdf'<k>,</k> <c>s</c><k>=</k>78<k>)</k> |
| <c>l</c>          | <d>Param2</d>     | <d>Param2</d><k>(</k>'s f', 5<k>,</k> <c>s</c><k>=</k>1<k>,</k> <c>d</c><k>=</k>'76f'<k>)</k> |


| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>fdsa</j>       |
| <c>GPU</c>        | <d>bool</d>       | <e>False</e>      |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>b</c>          | <d>float</d>      | <f>2.0</f>        |
| <c>a</c>          | <d>int</d>        | <f>1</f>          |
| <c>d</c>          | <d>str</d>        | <j>fd</j>         |
| <c>k</c>          | <d>Param</d>      | <d>Param</d><k>(</k>'sdf sdf'<k>,</k> <c>s</c><k>=</k>78<k>)</k> |
| <c>l</c>          | <d>Param2</d>     | <d>Param2</d><k>(</k>'s f', 5<k>,</k> <c>s</c><k>=</k>1<k>,</k> <c>d</c><k>=</k>'76f'<k>)</k> |

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>fdsa</j>       |
| <c>GPU</c>        | <d>bool</d>       | <e>False</e>      |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>b</c>          | <d>float</d>      | <f>2.0</f>        |
| <c>a</c>          | <d>int</d>        | <f>1</f>          |
| <c>d</c>          | <d>str</d>        | <j>fd</j>         |
| <c>k</c>          | <d>Param</d>      | Param('sdf sdf', s=78) |
| <c>l</c>          | <d>Param2</d>     | Param2('s f', 5, s=1, d='76f') |

# Output

    2.0 fd 3600 True
    sdf sdf 2 78

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>              | <d>str</d>            | <j>Example3-1</j>        |
| <c>GPU</c>               | <d>bool</d>            | <e>False</e>             |
| <c>time</c>              | <d>int</d>             | <f>3600</f>              |
| <c>b</c>                 | <d>float</d>           | <f>2.0</f>               |
| <c>a</c>                 | <d>int</d>             | <f>2</f>                 |
| <c>d</c>                 | <d>str</d>             | <j>fd</j>                |
| <c>k</c>                 | <d>Param</d>           | <d>Param</d><k>(</k><j>'name2'</j><k>,</k> <c>s</c><k>=</k><f>11</f><k>)</k> |
| <c>l</c>                 | <d>Param2</d>          | <d>Param2</d><k>(</k><j>'fff'</j><k>,</k> <f>1119</f><k>,</k> <c>s</c><k>=</k><f>2</f><k>,</k> <c>d</c><k>=</k><j>'fgrs'</j><k>)</k> |

# Output
