scoreboard players set $l mg.st 90
scoreboard players operation $s mg.st = $sqc mg.st
scoreboard players operation $s mg.st /= #20 mg.st
scoreboard players operation $l mg.st -= $s mg.st
execute store result storage mg:sq b.l int 1 run scoreboard players get $l mg.st
execute store result storage mg:sq b.n int 1 run scoreboard players get $sqn mg.st
function mg:soleil/bar with storage mg:sq b
execute if score $l mg.st matches 10 run tellraw @a[tag=mg.play] {"text":"⏳ Plus que 10 secondes !","color":"gold","bold":true}
