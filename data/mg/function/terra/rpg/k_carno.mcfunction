# Bonus RPG d'un carnotaure abattu
scoreboard players add @s mg.trdn 2
function mg:terra/rpg/xpk {n:120}
function mg:terra/rpg/kc_hook
tellraw @s {"text":"  +2 dents de carnotaure (forge de Jo)","color":"red"}
