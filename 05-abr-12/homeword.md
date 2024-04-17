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

```
b=c/2
DO
  a=a+1;
  b=a*2;
FINDO MIENTRAS (a>10 & b<20)
```


-| Dato Objeto | Dato Fuente|Operador 
-|-|-|-
1|T1|c|=
2|T1|2|/
3|b|T1|=
4|T1|a|=
5|T1|1|+
6|a|T1|=
7|T1|a|=
8|T1|2|*
9|b|T1|=
10|T1|a|=
11|T1|10|<
12|TR1|True|16
13|TR1|False|18
14|T1|b|=
15|T1|20|<
16|TR2|True|4
17|TR2|False|18
18|...|...|...


```
y=10; par=0;impar=0;

for(x=10;x<=y;x=x+1){
  do{
    par=par+1;
  }while(x==0);
}

```

-| Dato Objeto | Dato Fuente|Operador 
-|-|-|-
1|T1|10|=
2|y|T1|=
3|T1|0|=
4|par|T1|=
5|T1|0|=
6|impar|T1|=
7|T1|10|=
8|x|T1|=
9|T1|x|=
10|T1|y|<=
11|TR1|True|13
12|TR1|False|24
13|T1|1|=
14|T1|par|+
15|par|T1|=
16|T1|x|=
17|T1|0|==
18|TR2|True|13
19|Tr2|False|20
20|T1|x|=
21|T1|1|+
22|x|T1|=
23||7|JR
24|...|...|...

