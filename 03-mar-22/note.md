# Ejercio Triplos

Representar las siguientes expresiones aritméticas:
1. A = 2*8 * (2-3)
2. B=(6+6) * 5+6
3. H = 3-5/8*2
4. S = 6*5 / 4-3
5. Q = (7-9) / 1*(9-4)

## I. En triplo en notación prefijo y posfijo

1. A = 2*8 * (2-3)

**posfijo**

 Dato Objeto | Dato Fuente | Operador 
-|-|-
T1|2|=
T1|3|-
T2|2|=
T2|8|*
T2|T1|*
A|T2|=

**prefijo**

Operador | Dato Objeto | Dato Fuente
-|-|-
=|T1|2
-|T1|3
=|T2|2
*|T2|8
*|T2|T1
=|A|T2

2. B=(6+6) * 5+6

**posfijo**

 Dato Objeto | Dato Fuente | Operador 
-|-|-
T1|6|=
T1|6|+
T1|5|*
T1|6|+
B|T1|=

**prefijo**

Operador | Dato Objeto | Dato Fuente
-|-|-
=|T1|6
+|T1|6
*|T1|5
+|T1|6
=|B|T1

3. H = 3-5/8*2

**posfijo**

 Dato Objeto | Dato Fuente | Operador 
-|-|-
T1|5|=
T1|8|/
T1|2|*
T2|3|=
T2|T1|-
H|T2|=

**prefijo**

Operador | Dato Objeto | Dato Fuente
-|-|-
=|T1|5
/|T1|8
*|T1|2
=|T2|3
-|T2|T1
=|H|T2

4. S = 6*5 / 4-3

**posfijo**

 Dato Objeto | Dato Fuente | Operador 
-|-|-
T1|6|=
T1|5|*
T1|4|/
T1|3|-
S|T1|=

**prefijo**

Operador | Dato Objeto | Dato Fuente
-|-|-
=|T1|6
*|T1|5
/|T1|4
-|T1|3
=|S|T1

5. Q = (7-9) / 1*(9-4)

**posfijo**

 Dato Objeto | Dato Fuente | Operador 
-|-|-
T1|7|=
T1|9|-
T2|9|=
T2|4|-
T1|1|/
T1|T2|*
Q|T1|=

**prefijo**

Operador | Dato Objeto | Dato Fuente
-|-|-
=|T1|7
-|T1|9
=|T2|9
-|T2|4
/|T1|1
*|T1|T2
=|Q|T1



## II. En cuádruplo en notación posfijo.

1. A = 2*8 * (2-3)

Dato Objeto|Dato Fuente 1| Dato Fuente 2 | Operador
-|-|-|-
T1|2|3|-
T2|2|8|*
T2|T2|T1|*
A||T2|=

2. B=(6+6) * 5+6

Dato Objeto|Dato Fuente 1| Dato Fuente 2 | Operador
-|-|-|-
T1|

3. H = 3-5/8*2


Dato Objeto|Dato Fuente 1| Dato Fuente 2 | Operador
-|-|-|-

4. S = 6*5 / 4-3

Dato Objeto|Dato Fuente 1| Dato Fuente 2 | Operador
-|-|-|-

5. Q = (7-9) / 1*(9-4)

Dato Objeto|Dato Fuente 1| Dato Fuente 2 | Operador
-|-|-|-
