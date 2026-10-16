# @s : récompense d'étape (macro xp, c crédits, n étape suivante)
$scoreboard players add @s mg.tvc $(c)
$tellraw @s [{"text":"  +$(c) ₵","color":"green"}]
$function mg:terra/rpg/xp {n:$(xp)}
$function mg:terra/rpg/ch {n:$(n)}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
