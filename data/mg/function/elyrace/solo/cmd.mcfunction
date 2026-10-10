# @s = joueur qui a utilise /trigger mg.xs : 1 = fenêtre, 2 = abandon, 3 = ses records, 4 = (admin) arrêter tous les solos, 10 = solo au hasard, 10 + NUM = solo sur le parcours NUM, 5 = rejouer (phase 4)
# la valeur est lue dans #xv, puis le trigger est remis à zéro d'abord (core/tick le réactive à chaque tick)
scoreboard players operation #xv mg.st = @s mg.xs
scoreboard players reset @s mg.xs
execute if score #xv mg.st matches 1 run function mg:elyrace/solo/menu
execute if score #xv mg.st matches 2 run function mg:elyrace/solo/quit
execute if score #xv mg.st matches 5 run function mg:elyrace/solo/retry
execute if score #xv mg.st matches 3 run function mg:elyrace/records
execute if score #xv mg.st matches 4 run function mg:elyrace/solo/stop_all
execute if score #xv mg.st matches 10.. run function mg:elyrace/solo/start
