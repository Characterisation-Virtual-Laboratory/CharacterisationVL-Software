set V :={"a","b","s","t"};
set A :={<"s","a">, <"s","b">, <"a","b">, <"a","t">, <"b","t">};
param c[A] := <"s","a"> 17, <"s","b"> 47, <"a","b"> 19, <"a","t"> 53,
<"b","t"> 23;
defset dminus(v) := {<i,v> in A};
defset dplus(v) := {<v,j> in A};
var x[A] binary;
minimize cost: sum<i,j> in A: c[i,j] * x[i,j];
subto fc:
forall <v> in V - {"s","t"}:
sum<i,v> in dminus(v): x[i,v] == sum<v,i> in dplus(v): x[v,i];
subto uf:
sum<s,i> in dplus("s"): x[s,i] == 1;
