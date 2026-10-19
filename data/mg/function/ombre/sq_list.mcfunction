# @s : quêtes secondaires
tellraw @s {"text":"\n❗ Quêtes secondaires","color":"yellow","bold":true}
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Les loups du berger","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p0 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Les loups du berger","color":"yellow","bold":true},{"text":" (🐑 Gaspard, berger)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Le cidre des cryptes","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p1 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Le cidre des cryptes","color":"yellow","bold":true},{"text":" (🍺 Marthe, aubergiste)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Cordes d'arc","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p2 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Cordes d'arc","color":"yellow","bold":true},{"text":" (🏹 Thalion, archer elfe)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Le nid des tisseuses","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p3 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Le nid des tisseuses","color":"yellow","bold":true},{"text":" (🏹 Thalion, archer elfe)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Fourrures d'ours","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p4 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Fourrures d'ours","color":"yellow","bold":true},{"text":" (🧵 Sigrun, fourreuse)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"La grotte de givre","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p5 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"La grotte de givre","color":"yellow","bold":true},{"text":" (🪓 Jarl Bjorn)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Sangsues géantes","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p6 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Sangsues géantes","color":"yellow","bold":true},{"text":" (🌱 Odo, herboriste)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Le temple englouti","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p7 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Le temple englouti","color":"yellow","bold":true},{"text":" (✝ Sœur Maëlle)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Ambre du désert","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p8 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Ambre du désert","color":"yellow","bold":true},{"text":" (💍 Zahra, joaillière)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Les tombeaux d'Azhar","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p9 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p9 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Les tombeaux d'Azhar","color":"yellow","bold":true},{"text":" (🐪 Kassim, caravanier)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Élémentaires de feu","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p10 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Élémentaires de feu","color":"yellow","bold":true},{"text":" (🔥 Durgan, forgeron nain)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"La forge écarlate","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p11 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"La forge écarlate","color":"yellow","bold":true},{"text":" (🔥 Durgan, forgeron nain)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Runite pour la forge","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p12 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Runite pour la forge","color":"yellow","bold":true},{"text":" (👑 Roi Thrain)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Les mines profondes","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p13 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Les mines profondes","color":"yellow","bold":true},{"text":" (👑 Roi Thrain)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Chevaliers noirs","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p14 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Chevaliers noirs","color":"yellow","bold":true},{"text":" (🛡 Capitaine Aldric)","color":"gray"}]
scoreboard players operation $b mg.st = @s mg.olsd
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run tellraw @s [{"text":" ✔ ","color":"green"},{"text":"Le puits des âmes","color":"gray","strikethrough":true}]
scoreboard players set $d mg.st 0
scoreboard players operation $d mg.st = @s mg.olsd
scoreboard players operation $d mg.st /= #p15 mg.st
scoreboard players operation $d mg.st %= #2 mg.st
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score $d mg.st matches 0 run tellraw @s [{"text":" ▶ ","color":"yellow"},{"text":"Le puits des âmes","color":"yellow","bold":true},{"text":" (🛡 Capitaine Aldric)","color":"gray"}]
