# Ejercicio 

Convertir a prefijo y posfijo cada una de las siguientes expresiones:
- 2 * 8 * (2-3)


- (6+6)  5+6
- H = 3-5/82
- S = 6*5  4-3
- Q = (7-9)  1*(9-4)



## Estructura de Triplos 

Estructura de datos que represnta de lógica de la generación de operaciones, Almacena en una tabla de símbolo con tres columnas

```
w = x + y + 24 - z
```
```assembly 
MOV AX, x;
ADD AX, y;
ADD AX, 24;
SUB AX, z;
MOV w, AX;

```
1. Identificar cuál es le operador de mayor jerarquí y su respectivo operado 1. Variable temporal T1, diferente a las varibles que hay en la aritemetica

```
w = x + y + 24 - z
```

-|Dato objeto | Dato Fuente  | Operador
-|-|-|-
T1 = X [postfijo T1 X =]|T1|X|=
T1 + y [postfijo T1 y +]| T1|y|+
T1 + 24 [T1 24 +]|T1|24|+
T1 - z [T1 z -]|T1|z|-
w = T1 [w T1 =]|w1|T1|=

```
w = x + y / 24 
```

-|Dato objeto | Dato Fuente  | Operador
-|-|-|-
T1 = X [postfijo T1 X =]|T1|X|=
T1 + y [postfijo T1 y +]| T1|y|+
T1 + 24 [T1 24 +]|T1|24|+
T1 - z [T1 z -]|T1|z|-
w = T1 [w T1 =]|w1|T1|=