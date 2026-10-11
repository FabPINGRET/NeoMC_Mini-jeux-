# Explosion pour le spectacle : aucun bloc cassé, aucun dégât (petit saut pour ceux qui sont tout près)
execute at @s run particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force
execute at @s run particle minecraft:firework ~ ~ ~ 0.5 0.5 0.5 0.2 40 force
execute at @s run playsound minecraft:entity.generic.explode player @a ~ ~ ~ 2 1.1
execute at @s as @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,distance=..3] run effect give @s minecraft:levitation 1 3 true
kill @s
