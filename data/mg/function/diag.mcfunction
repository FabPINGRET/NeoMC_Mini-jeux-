# Diagnostic du menu : /function mg:diag  (à lancer par l'admin concerné)
tellraw @s [{"text":"\n✦ DIAGNOSTIC MINI-JEUX ✦","color":"gold","bold":true}]
tellraw @s {"text":"✔ Datapack chargé (cette commande a répondu)","color":"green"}
execute if score $setup mg.st matches 1 run tellraw @s {"text":"✔ Setup effectué ($setup=1)","color":"green"}
execute unless score $setup mg.st matches 1 run tellraw @s {"text":"✖ Setup non fait : lance /function mg:setup","color":"red"}
execute if entity @s[tag=mg.admin] run tellraw @s {"text":"✔ Tu as le tag mg.admin","color":"green"}
execute unless entity @s[tag=mg.admin] run tellraw @s {"text":"✖ Pas de tag mg.admin : /function mg:admin","color":"red"}
execute if items entity @s hotbar.4 minecraft:carrot_on_a_stick run tellraw @s {"text":"✔ L'objet menu est dans la barre (case 5)","color":"green"}
execute unless items entity @s hotbar.4 minecraft:carrot_on_a_stick run tellraw @s {"text":"✖ Pas d'objet menu en case 5","color":"red"}
function mg:core/diag_adv
scoreboard players operation $tc0 mg.st = $tc mg.st
schedule function mg:core/diag_late 10t
tellraw @s {"text":"→ Test de la fenêtre du menu ci-dessous (si rien ne s'ouvre, le menu texte s'affiche) :","color":"gray"}
function mg:core/menu_use
