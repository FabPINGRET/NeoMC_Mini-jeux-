# Première visite : point de départ ; sinon : inventaire, XP, position et point de réapparition restaurés
$execute unless data storage mg:survie p.k$(id).pos run return run function mg:survie/first {id:$(id)}
$function mg:survie/vault_load {x:$(x)}
$function mg:survie/restore {id:$(id)}
$execute unless entity @s[tag=mg.svg2] run function mg:survie/regen_place {id:$(id)}
tellraw @s [{"text":"🌲 Bienvenue en survie ! ","color":"green"},{"text":"Retour aux mini-jeux : menu Échap → ≡ Menu (ou /trigger mg.sv set 2).","color":"gray"}]
