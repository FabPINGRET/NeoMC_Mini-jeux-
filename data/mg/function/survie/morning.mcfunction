time set 1000
execute as @a[tag=mg.surv] if dimension mg:survie run tellraw @s [{"text":"☀ La nuit est passée.","color":"yellow"}]
