# (marqueur) drapeau ROUGE posé au sol ici
scoreboard players set $cfr mg.st 2
scoreboard players set $cfrt mg.st 600
summon minecraft:item_display ~ ~0.9 ~ {Tags:["mg.cfd","mg.cfdr"],billboard:"vertical",item:{id:"minecraft:red_banner",count:1},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
kill @s
tellraw @a[tag=mg.play] [{"text":"🚩 Le drapeau ROUGE est tombé ! ","color":"red"},{"text":"(retour automatique dans 30 s)","color":"gray"}]
