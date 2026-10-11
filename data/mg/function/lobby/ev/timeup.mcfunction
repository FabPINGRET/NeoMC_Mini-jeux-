execute if score $evon mg.st matches 1 run function mg:lobby/ev/e1_end
execute if score $evon mg.st matches 2 run function mg:lobby/ev/e2_end
execute if score $evon mg.st matches 3 run tellraw @a {"text":"🗝 Personne n'a trouvé le trésor... il a disparu !","color":"gray"}
function mg:lobby/ev/stop
