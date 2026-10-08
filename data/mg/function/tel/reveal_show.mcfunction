# Macro : c (chaîne), a (auteur de l'étape), b (auteur de l'étape précédente), x (parcelle)
execute if score $rs mg.st matches 0 run tp @a[tag=!mg.surv,tag=mg.play] 0.5 66 19420.5
$execute if score $rs mg.st matches 0 run tellraw @a[tag=!mg.surv] [{"text":"\n📞 Chaîne ","color":"gold","bold":true},{"score":{"name":"$rcn","objective":"mg.st"},"color":"gold","bold":true},{"text":" — ","color":"gray"},{"selector":"@a[scores={mg.ti=$(a)}]","color":"yellow"},{"text":" a écrit : ","color":"gray"},{"nbt":"ch[$(c)].s0","storage":"mg:tel","color":"white","bold":true}]
$execute if score $rs mg.st matches 0 run title @a[tag=!mg.surv] title [{"text":"« ","color":"gold"},{"nbt":"ch[$(c)].s0","storage":"mg:tel","color":"white","bold":true},{"text":" »","color":"gold"}]
$execute if score $rs mg.st matches 1 run tp @a[tag=!mg.surv,tag=mg.play] $(x).5 74 19480.5 0 30
$execute if score $rs mg.st matches 1 run tellraw @a[tag=!mg.surv] [{"text":"  ✎ construit par ","color":"gray"},{"selector":"@a[scores={mg.ti=$(a)}]","color":"yellow"}]
$execute if score $rs mg.st matches 1 run title @a[tag=!mg.surv] subtitle [{"text":"✎ construit par ","color":"gray"},{"selector":"@a[scores={mg.ti=$(a)}]","color":"yellow"}]
execute if score $rs mg.st matches 1 run title @a[tag=!mg.surv] title {"text":""}
$execute if score $rs mg.st matches 2 run tellraw @a[tag=!mg.surv] [{"text":"  🔍 ","color":"gray"},{"selector":"@a[scores={mg.ti=$(a)}]","color":"yellow"},{"text":" a deviné : ","color":"gray"},{"nbt":"ch[$(c)].s2","storage":"mg:tel","color":"white","bold":true}]
$execute if score $rs mg.st matches 2 run title @a[tag=!mg.surv] title [{"text":"« ","color":"aqua"},{"nbt":"ch[$(c)].s2","storage":"mg:tel","color":"white","bold":true},{"text":" »","color":"aqua"}]
$execute if score $rs mg.st matches 2 run function mg:tel/check {c:$(c),a:$(a),b:$(b),k:"s2"}
$execute if score $rs mg.st matches 3 run tp @a[tag=!mg.surv,tag=mg.play] $(x).5 74 19544.5 0 30
$execute if score $rs mg.st matches 3 run tellraw @a[tag=!mg.surv] [{"text":"  ✎ construit par ","color":"gray"},{"selector":"@a[scores={mg.ti=$(a)}]","color":"yellow"}]
$execute if score $rs mg.st matches 3 run title @a[tag=!mg.surv] subtitle [{"text":"✎ construit par ","color":"gray"},{"selector":"@a[scores={mg.ti=$(a)}]","color":"yellow"}]
execute if score $rs mg.st matches 3 run title @a[tag=!mg.surv] title {"text":""}
$execute if score $rs mg.st matches 4 run tellraw @a[tag=!mg.surv] [{"text":"  🔍 ","color":"gray"},{"selector":"@a[scores={mg.ti=$(a)}]","color":"yellow"},{"text":" a deviné : ","color":"gray"},{"nbt":"ch[$(c)].s4","storage":"mg:tel","color":"white","bold":true}]
$execute if score $rs mg.st matches 4 run title @a[tag=!mg.surv] title [{"text":"« ","color":"aqua"},{"nbt":"ch[$(c)].s4","storage":"mg:tel","color":"white","bold":true},{"text":" »","color":"aqua"}]
$execute if score $rs mg.st matches 4 run function mg:tel/check {c:$(c),a:$(a),b:$(b),k:"s4"}
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1
