execute as @a[scores={horn_blow=1..},tag=mg.flw] at @s run function utility:horn_blow

# END HORN BLOW CHECKS
scoreboard players set @a[tag=mg.flw] horn_blow 0
