"""Branche le contre-la-montre solo PAR JOUEUR de la Course d'elytres dans le moteur : python wire_elyrace4.py <racine du depot>. A lancer
APRES gen_elyrace.py (apres wire_elyrace3.py : sur un amont non cable, wire3 pose les crochets de la 2c, que ce script retire). Idempotent :
chaque branchement porte un marqueur (son propre texte) ; s'il est deja dans le fichier, le branchement est saute. Chaque ancre d'un
branchement a appliquer doit exister EXACTEMENT une fois (wirelib.Patcher : tout se fait en memoire, rien n'est ecrit si une ancre
manque) ; les fins de ligne de chaque fichier sont conservees. wire_elyrace3.py ne fait plus rien quand ce script est passe (MARKER).
Branchements (verifies par checks_solo.py) :
  core/tick       + 1 ligne solo/tick, apres core/opt et core/reconnect (le solo lit la presence et la pause du tick) et avant void_catch ;
                  le nettoyage des elytres mg_elyr (toutes les secondes) epargne les joueurs en solo (tag=!mg.xso)
  core/countdown, core/begin, core/reconnect : les crochets de la 2c (solo dans la machine a etats, $xs) sont RETIRES
  aide, README, docs/GAMES.md : textes du solo mis a jour
core/request n'est PAS touche (le solo ignore la machine a etats : request ne tague mg.play que les joueurs hors pause).
Plus d'ancre en jeu : les fonctions solo/* sont generees par gen_elyrace.py. Python stdlib uniquement (compatible 3.8).
"""
import os
import sys

from wirelib import Patcher

MARKER = 'mg:elyrace/solo/tick'                  # present dans core/tick une fois ce script passe (wire_elyrace3.py le teste)
CMD_LINE = 'execute as @a[scores={mg.xs=1..}] run function mg:elyrace/solo/cmd'
TICK_HOOK = 'execute if entity @a[tag=mg.xso] run function ' + MARKER
HOLD_COMMENT = "# Contre-la-montre solo : son propre compte à rebours (titres et sons pour le joueur seul)\n"
HOOK_COUNTDOWN = 'execute if score $xs mg.st matches 1 if score $game mg.st matches 66 run return run function mg:elyrace/solo/countdown'
NOT_SOLO = 'unless score $xs mg.st matches 1'
HORN = 'playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.7 1.4'
HORN_SOLO = 'execute if score $xs mg.st matches 1 as @a[tag=mg.play] at @s run ' + HORN
RECONNECT_OLD = ("SPECTATEUR (sauf contre-la-montre solo : rien à regarder, il retourne au lobby)\n"
                 "execute if score $state mg.st matches 1..3 %s run return run function mg:core/reconnect_spec" % NOT_SOLO)
RECONNECT_NEW = "SPECTATEUR\nexecute if score $state mg.st matches 1..3 run return run function mg:core/reconnect_spec"
CLEARS = ('clear @a[tag=!mg.play] minecraft:elytra[minecraft:custom_data~{mg_elyr:1b}]',
          'clear @a[tag=!mg.play] minecraft:firework_rocket[minecraft:custom_data~{mg_elyr:1b}]')


def has(p, path, text):
    return text in p.text(path)[0]


def core_hooks(p):
    tick = p.fn_path('core/tick')
    if not has(p, tick, MARKER):
        p.between(tick, CMD_LINE, '\n# Armurerie du lobby', TICK_HOOK + '\n')
    for old in CLEARS:
        if has(p, tick, old):
            p.patch(tick, old, old.replace('tag=!mg.play]', 'tag=!mg.play,tag=!mg.xso]'))
    countdown = p.fn_path('core/countdown')
    if has(p, countdown, HOOK_COUNTDOWN):
        p.patch(countdown, HOLD_COMMENT + HOOK_COUNTDOWN + '\n', '')
    begin = p.fn_path('core/begin')
    if has(p, begin, '$xs'):
        p.patch(begin, '# Stats : une partie jouée de plus (pas en contre-la-montre solo)\n', '# Stats : une partie jouée de plus\n')
        p.replace_line(begin, 'execute %s run scoreboard players add @a[tag=mg.play] mg.stp 1' % NOT_SOLO, 'scoreboard players add @a[tag=mg.play] mg.stp 1')
        p.patch(begin, 'execute %s as @a[tag=mg.play] run function mg:hall/top {obj:"mg.stp"' % NOT_SOLO,
                'execute as @a[tag=mg.play] run function mg:hall/top {obj:"mg.stp"')
        p.patch(begin, HORN_SOLO + '\n', '')
        p.replace_line(begin, 'execute %s as @a[tag=!mg.surv] at @s run ' % NOT_SOLO, 'execute as @a[tag=!mg.surv] at @s run ' + HORN)
    reconnect = p.fn_path('core/reconnect')
    if has(p, reconnect, '$xs'):
        p.patch(reconnect, RECONNECT_OLD, RECONNECT_NEW)


def docs(p):
    """aide, README (texte et table des commandes), docs/GAMES.md."""
    aide = p.fn_path('aide')
    if not has(p, aide, 'te met en pause'):
        p.replace_line(aide, 'tellraw @s [{"text":"• Course d\'élytres, contre-la-montre solo (tous) : "',
                       'tellraw @s [{"text":"• Course d\'élytres, contre-la-montre solo (tous) : ","color":"gray"},{"text":"/trigger mg.xs","color":"yellow"},'
                       '{"text":" (fenêtre), ","color":"gray"},{"text":"set 2","color":"yellow"},{"text":" (abandonner), ","color":"gray"},'
                       '{"text":"set 3","color":"yellow"},{"text":" (tes records), ","color":"gray"},{"text":"set 4","color":"yellow"},'
                       '{"text":" (admin : arrêter tous les solos) ; seul en piste, même pendant une partie sauf une course de groupe ; te met en pause '
                       'pendant le solo ; 30 s entre deux solos","color":"gray"}]')
    readme = p.path('README.md')
    if not has(p, readme, 'mis **en pause** pendant le solo'):
        p.patch(readme, 'seul en piste quand aucune partie ne tourne, compte à rebours de 5 s, 30 s d\'attente entre deux solos (sauf admins)',
                'seul en piste, **pendant n\'importe quelle partie sauf une course d\'élytres de groupe** (4 solos au plus ; le joueur est mis **en pause** pendant le solo, '
                'reprendre la pause l\'arrête), compte à rebours de 5 s, 30 s d\'attente entre deux solos (sauf admins)')
        p.patch(readme, '(aucune partie en cours, 30 s entre deux solos)', '(même pendant une partie sauf une course de groupe, 4 solos au plus, 30 s entre deux solos)')
        p.after(readme, "| `/trigger mg.xs set 2` / `set 3` | Contre-la-montre solo : abandonner / afficher ses meilleurs temps et les records du serveur | tous |",
                "| `/trigger mg.xs set 4` | Contre-la-montre solo : arrêter tous les solos en cours | admins |\n")
    games = p.path('docs', 'GAMES.md')
    if not has(p, games, 'tag `mg.xso`'):
        p.patch(games, 'même jeu 66 avec `$xs` = 1, lancé par `mg:elyrace/solo/start` sans passer par `core/request`.',
                'hors machine à états (ni `$state` ni `$game` : tag `mg.xso`, scores par joueur `mg.xph` / `xst` / `xcr` / `xse` / `xsl`, 4 solos au plus, '
                'joueur mis en pause `mg.spectate`), lancé par `mg:elyrace/solo/start`, tick `mg:elyrace/solo/tick` (appelé par `core/tick`).')


def wire_all(p):
    core_hooks(p)
    docs(p)


def main():
    if len(sys.argv) != 2 or not os.path.isdir(os.path.join(sys.argv[1], 'data', 'mg', 'function')):
        raise SystemExit(__doc__)
    p = Patcher(os.path.abspath(sys.argv[1]))
    wire_all(p)
    print('%d fichiers modifies' % p.commit())


if __name__ == '__main__':
    main()
