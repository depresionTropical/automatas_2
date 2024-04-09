# Generación de Código Intermedio

Representar en código intermedio –triplo en notación posfijo- el siguiente código
## Ejercicio 1
```
int x, y, c ;
y = 6 ;
…. (x == 0 && x < 5 )
{
c = a + w ;
x = 4 + y ;
}
y = 6 + c ;
```


-| Dato Objeto | Dato Fuente|Operador 
-|-|-|-
1| T1 | 6 | =
2| y | T1 | =
3| T1 | x | =
4| T1 | 0 | ==
5| TR1 | true|**9**
6| TR1 | false| **18**
7|T1 | x | =
8| x | 5 | <
9| TR2 | true | **11**
10| TR2 | false | **18**
11| T1 | a | =
12| T1| w | +
13|c | T1 | =
14| T1 | 4 |=
15 |T1 | y | +
16| x | T1 |=
17|
18|T1|6|=
19|T1|c|+
20|y|T1|=

## Ejercicio 2

```
int x, y, c ;
y = 6 ;
…. (x == 0 || x < 5 )
{
c = a + w ;
x = 4 + y ;
}
y = 6 + c ;
```

-| Dato Objeto | Dato Fuente|Operador 
-|-|-|-
1|T1|6|=
2|y|T1|=
3|T1|x | =
4|T1|0|==
5|TR1| true|**11**
6|TR1| false|**7**
7|T1|x|=
8|T1|5|<
9|TR2|true|**11**
10|TR2|false|**18**
11|T1|a|=
12|T1|w|+
13|c|T1|=
14|T1|4|=
15|T1|y|+
16|x|T1|=
17|
18|T1|6|=
19|T1|c|+
20|y|T1|=

