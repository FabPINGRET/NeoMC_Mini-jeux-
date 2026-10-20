# Pose use_cooldown (n = arme, s = secondes) et le marqueur de variante gcr (m) sur l'objet en main
$item modify entity @s weapon.mainhand {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:$(s)f,cooldown_group:"mg:gun$(n)"}}}
$item modify entity @s weapon.mainhand {function:"minecraft:set_custom_data",tag:{gcr:$(m)b}}
