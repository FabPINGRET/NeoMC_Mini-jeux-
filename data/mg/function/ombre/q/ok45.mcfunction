# Étape 45 validée (liora)
function mg:ombre/xp {n:800}
scoreboard players set @s mg.olwt 9
scoreboard players set @s mg.olbless 1
function mg:ombre/kit
title @s times 10 60 20
title @s title {"text":"LAME DE L'AUBE","color":"gold","bold":true}
title @s subtitle {"text":"Arme de palier 9 · bénédiction contre les ténèbres","color":"yellow"}
execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.5 1 0.5 0.4 80
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
