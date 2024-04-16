# WHILE


```
par = 0
MIENTRAS (a%2 ==0 & a < 20)
 par ++
 a=a+2
FIN
```

-| Dato Objeto | Dato Fuente|Operador 
-|-|-|-
1| T1| 0 | =
2| par| T1|=
3| T1 | 2| =
4| T2 | a|=
5| T2 | T1 | %
6| T2 | 0 |==
7|TR1| true|**9**
8|TR1| false|**22**
9|T1|20|=
10|T2|a|=
11|T2|T1|<
12|TR2| true|**14**
13|TR2| false|**22**
14|T1|1|=
15|T1|par|+
16|par|T1|=
17|T1|2|=
18|T2|a|=
19|T2|T1|+
20|a|T2|=
21||3|JMP
22|...|...|...

```
if _D1 > 1 || _F1 >10 then
_D2 = 34 * 2 - _W2*_D4;	
_F2 = _A2 + _A3 / 3;	
else 
_F2 = 4 ;
end if	

while _F2 < 10 then
_d2 = _W2*_D4;		
_A1 = _A3 / 3 *10;	  
_F2 = _F2 +1 ;
end while
```