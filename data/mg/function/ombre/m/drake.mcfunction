# Drake des braises (créature articulée)
function mg:ombre/beast/drake
tag @e[tag=mg.ollast] add mg.olk_drake
tag @e[tag=mg.ollast] add mg.olm
execute as @e[tag=mg.ollast] run data merge entity @s {CustomName:{"text":"Drake des braises","color":"gold"}}
