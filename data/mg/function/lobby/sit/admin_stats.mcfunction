# Admin (@s) : compteurs d'usage (assis, emotes), depuis la création de l'objectif mg.lsn
execute unless score $sit mg.lsn matches 0.. run scoreboard players set $sit mg.lsn 0
execute unless score $bnc mg.lsn matches 0.. run scoreboard players set $bnc mg.lsn 0
execute unless score $itm mg.lsn matches 0.. run scoreboard players set $itm mg.lsn 0
execute unless score $emo1 mg.lsn matches 0.. run scoreboard players set $emo1 mg.lsn 0
execute unless score $emo2 mg.lsn matches 0.. run scoreboard players set $emo2 mg.lsn 0
execute unless score $emo3 mg.lsn matches 0.. run scoreboard players set $emo3 mg.lsn 0
execute unless score $emo4 mg.lsn matches 0.. run scoreboard players set $emo4 mg.lsn 0
execute if score $sitoff mg.st matches 1 run tellraw @s {"text":"🪑 Assis et emotes : désactivés","color":"red"}
execute unless score $sitoff mg.st matches 1 run tellraw @s {"text":"🪑 Assis et emotes : activés","color":"green"}
tellraw @s [{"text":"Usage : ","color":"gray"},{"text":"🪑 Assis ","color":"white"},{"score":{"name":"$sit","objective":"mg.lsn"},"color":"yellow"},{"text":" · 🪑 Clic banc ","color":"white"},{"score":{"name":"$bnc","objective":"mg.lsn"},"color":"yellow"},{"text":" · 🎉 Objet ","color":"white"},{"score":{"name":"$itm","objective":"mg.lsn"},"color":"yellow"},{"text":" · ✋ Salut ","color":"white"},{"score":{"name":"$emo1","objective":"mg.lsn"},"color":"yellow"},{"text":" · ♪ Danse ","color":"white"},{"score":{"name":"$emo2","objective":"mg.lsn"},"color":"yellow"},{"text":" · 🎉 Fête ","color":"white"},{"score":{"name":"$emo3","objective":"mg.lsn"},"color":"yellow"},{"text":" · 😵 Étourdi ","color":"white"},{"score":{"name":"$emo4","objective":"mg.lsn"},"color":"yellow"}]
