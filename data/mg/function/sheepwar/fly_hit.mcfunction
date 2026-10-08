# Impact (@s = mouton) : il arrête de voler et tombe au sol (la mèche démarre à l'atterrissage, sheep_tick)
tag @s remove mg.fly
data merge entity @s {NoGravity:0b,Motion:[0.0d,0.0d,0.0d]}
