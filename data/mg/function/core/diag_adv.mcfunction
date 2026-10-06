# Diagnostic des advancements (@s = joueur) — isolé, sans effet de bord
execute if entity @s[advancements={mg:menu=false}] run tellraw @s {"text":"✔ Advancement mg:menu présent (prêt)","color":"green"}
execute if entity @s[advancements={mg:menu=true}] run tellraw @s {"text":"✖ mg:menu bloqué (déjà obtenu) → révocation automatique","color":"red"}
execute if entity @s[advancements={mg:menu=true}] run advancement revoke @s only mg:menu
execute if entity @s[advancements={mg:sheep_launch=true}] run advancement revoke @s only mg:sheep_launch
