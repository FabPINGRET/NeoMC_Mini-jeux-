execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.hoglin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] unless items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Grumblegut","color":"green"},{"text":"> Brmm grmm grud. Gruh? Spub. Spub GRMGMGMGMMG Grud! Bagrogo buhhhhhh.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ as @a[distance=..10,tag=mg.flw] if items entity @s weapon.* blaze_rod run tellraw @s [{"text":"<"},{"text":"Grumblegut","color":"green"},{"text":"> Have you spoken with the wizard? He is a man of great wisdom. His tower arrived in a magnificent explosion, and since then he has imparted many secrets to us Orcs. He is far more welcome than those foolish Germ Eaters.","color":"white"}]

# ","color":"white"},{"text":"
#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
