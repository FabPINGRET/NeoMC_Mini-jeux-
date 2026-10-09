"""Branche le contre-la-montre solo de la Course d'elytres dans le moteur : python wire_elyrace3.py <racine du depot>. A lancer APRES
gen_elyrace.py (apres wire_elyrace2.py). Idempotent : chaque branchement porte un marqueur (son propre texte) ; s'il est deja dans le
fichier, le branchement est saute. Sur l'amont non cable tout s'applique ; sur un depot deja cable, seuls les branchements ajoutes
depuis s'appliquent ; une 3e execution n'ecrit rien. Chaque ancre d'un branchement a appliquer doit exister EXACTEMENT une fois
(wirelib.Patcher : tout se fait en memoire, rien n'est ecrit si une ancre manque) ; les fins de ligne de chaque fichier sont conservees.
Les crochets du moteur (verifies par checks_solo.py) :
  core/tick       active le trigger mg.xs pour tous les joueurs et appelle solo/cmd quand il est utilise
  core/countdown  aiguille le compte a rebours d'un solo vers solo/countdown (avant la decrementation commune de $timer)
  core/begin      pas de statistique « parties jouees » (mg.stp, classement mg:hall/top) pour un solo ; le cor de raid du GO n'est
                  joue qu'au joueur du solo (et non a tout le lobby)
  core/reconnect  un solo n'a rien a regarder : le joueur qui revient retourne au lobby au lieu de devenir spectateur
Plus l'aide, le README et docs/GAMES.md. Les fonctions solo/* et les records sont generes par gen_elyrace.py.
OBSOLETE depuis wire_elyrace4.py (le solo est devenu par joueur, hors machine a etats) : wire4 retire ces crochets de la 2c, et ce script ne
fait plus rien une fois que wire4 est passe (son crochet solo/tick est dans core/tick). Il reste dans la chaine pour un amont non cable.
"""
import os
import sys

from wirelib import Patcher

NOT_SOLO = 'unless score $xs mg.st matches 1'      # garde des lignes que le solo ne doit pas executer
HOOK_COUNTDOWN = 'execute if score $xs mg.st matches 1 if score $game mg.st matches 66 run return run function mg:elyrace/solo/countdown'
HORN = 'playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.7 1.4'
HORN_SOLO = 'execute if score $xs mg.st matches 1 as @a[tag=mg.play] at @s run ' + HORN


def pending(p, path, marker):
    """Vrai si le branchement n'est pas encore dans le fichier (son marqueur est absent du texte courant)."""
    return marker not in p.text(path)[0]


def wired_by_4(p):
    """Vrai si wire_elyrace4.py est deja passe (son crochet solo/tick est dans core/tick) : le solo n'est plus dans la machine a etats,
    les crochets ci-dessous (countdown, begin, reconnect) ont ete retires exprès et ne doivent pas revenir."""
    return 'mg:elyrace/solo/tick' in p.text(p.fn_path('core/tick'))[0]


def core_hooks(p):
    tick = p.fn_path('core/tick')
    if pending(p, tick, 'mg:elyrace/solo/cmd'):
        p.between(tick, 'scoreboard players enable @a mg.dice', 'function mg:survie/tick', 'scoreboard players enable @a mg.xs\n')
        p.between(tick, 'execute as @a[scores={mg.opt=1..}] run function mg:core/opt', '\n# Armurerie du lobby',
                  'execute as @a[scores={mg.xs=1..}] run function mg:elyrace/solo/cmd\n')
    countdown = p.fn_path('core/countdown')
    if pending(p, countdown, HOOK_COUNTDOWN):
        p.between(countdown, 'execute if score $game mg.st matches 61 if function mg:kart/hold run return 0',
                  'scoreboard players remove $timer mg.st 1',
                  "# Contre-la-montre solo : son propre compte à rebours (titres et sons pour le joueur seul)\n" + HOOK_COUNTDOWN + '\n')
    begin = p.fn_path('core/begin')
    if pending(p, begin, '(pas en contre-la-montre solo)'):
        p.patch(begin, '# Stats : une partie jouée de plus\n', '# Stats : une partie jouée de plus (pas en contre-la-montre solo)\n')
        p.replace_line(begin, 'scoreboard players add @a[tag=mg.play] mg.stp 1', 'execute %s run scoreboard players add @a[tag=mg.play] mg.stp 1' % NOT_SOLO)
        p.patch(begin, 'execute as @a[tag=mg.play] run function mg:hall/top {obj:"mg.stp"',
                'execute %s as @a[tag=mg.play] run function mg:hall/top {obj:"mg.stp"' % NOT_SOLO)
    if pending(p, begin, HORN_SOLO):
        p.replace_line(begin, 'execute as @a[tag=!mg.surv] at @s run ' + HORN,
                       'execute %s as @a[tag=!mg.surv] at @s run %s\n%s' % (NOT_SOLO, HORN, HORN_SOLO))
    reconnect = p.fn_path('core/reconnect')
    if pending(p, reconnect, 'sauf contre-la-montre solo'):
        p.patch(reconnect,
                "SPECTATEUR\nexecute if score $state mg.st matches 1..3 run return run function mg:core/reconnect_spec",
                "SPECTATEUR (sauf contre-la-montre solo : rien à regarder, il retourne au lobby)\n"
                "execute if score $state mg.st matches 1..3 %s run return run function mg:core/reconnect_spec" % NOT_SOLO)


def docs(p):
    """aide, README (texte et table des commandes), docs/GAMES.md."""
    aide = p.fn_path('aide')
    if pending(p, aide, '/trigger mg.xs'):
        p.between(aide, '(Pic Blanc, 20 anneaux) ; reconstruire : /function mg:elyrace/build","color":"gray"}]', 'tellraw @s [{"text":"• Bataille de karts',
                  'tellraw @s [{"text":"• Course d\'élytres, contre-la-montre solo (tous) : ","color":"gray"},{"text":"/trigger mg.xs","color":"yellow"},'
                  '{"text":" (fenêtre), ","color":"gray"},{"text":"set 2","color":"yellow"},{"text":" (abandonner), ","color":"gray"},'
                  '{"text":"set 3","color":"yellow"},{"text":" (tes records) ; seul en piste quand aucune partie ne tourne, 30 s entre deux solos","color":"gray"}]\n')
    readme = p.path('README.md')
    if pending(p, readme, '`/trigger mg.xs`'):
        p.patch(readme, 'au bout de 3 minutes le plus avancé gagne. Parcours vérifié par un pilote automatique simulé.',
                'au bout de 3 minutes le plus avancé gagne. **Contre-la-montre solo** (ouvert à tous, `/trigger mg.xs` : fenêtre, un parcours au choix ou au hasard) : '
                'seul en piste quand aucune partie ne tourne, compte à rebours de 5 s, 30 s d\'attente entre deux solos (sauf admins) ; **meilleur temps personnel** et '
                '**record du serveur** par parcours, partagés avec la course de groupe (le détenteur figure au classement du hall). '
                'Parcours vérifié par un pilote automatique simulé.')
        p.between(readme, "| `/trigger mg.go set 82` | Course d'élytres : Pic Blanc | admins |", '| `/trigger mg.menu` (non-admin)',
                  "| `/trigger mg.xs` / `set 1` | Course d'élytres : fenêtre du contre-la-montre solo | tous |\n"
                  "| `/trigger mg.xs set 11` / `12` / `10` | Contre-la-montre solo : Canyon du Couchant / Pic Blanc / parcours au hasard (aucune partie en cours, 30 s entre deux solos) | tous |\n"
                  "| `/trigger mg.xs set 2` / `set 3` | Contre-la-montre solo : abandonner / afficher ses meilleurs temps et les records du serveur | tous |\n")
    games = p.path('docs', 'GAMES.md')
    if pending(p, games, '`/trigger mg.xs`'):
        p.patch(games, '→ 66 + `$xc` (remappage dans `core/request`).',
                '→ 66 + `$xc` (remappage dans `core/request`) ; contre-la-montre solo (`/trigger mg.xs`, ouvert à tous) : même jeu 66 avec `$xs` = 1, '
                'lancé par `mg:elyrace/solo/start` sans passer par `core/request`.')


def wire_all(p):
    if wired_by_4(p):
        return
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
