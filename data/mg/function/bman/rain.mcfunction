# Mort subite : une bombe tombe sur une case libre au hasard
execute store result storage mg:ym r.i int 1 run random value 0..20
execute store result storage mg:ym r.j int 1 run random value 0..18
function mg:bman/rain_m with storage mg:ym r
