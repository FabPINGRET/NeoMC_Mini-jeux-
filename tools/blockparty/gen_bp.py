"""▦ Block Party : musique (chaises musicales + scratch de DJ), sols en bandes, mode mixte.

    python tools/blockparty/gen_bp.py .

- id 28 : carrés (sols 1..10, d'origine) ; id 91 : bandes (sols 11..20) ; id 92 : mixte (1..20 au hasard)
  → remappés sur le jeu 28 avec $bpm (0 carrés, 1 bandes, 2 mixte) dans core/request.
- Musique (note blocks) pendant la course ; elle se coupe net avec un « bzibzibzi » de platine au moment
  où les autres blocs disparaissent. Tempo plus rapide au fil des manches.
"""
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'arcade'))
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
COLORS = ['red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'light_blue', 'blue', 'purple', 'magenta', 'pink',
          'white', 'light_gray', 'gray', 'brown', 'black']
X0, Z0, N = -12, 6388, 24   # sol 24×24 en y 80


def pitch(n):          # n = 0..24 (note block), 12 = hauteur 1.0
    return round(2 ** ((n - 12) / 12), 4)


# ---------- sols en bandes (11..20) : 16 bandes (8 de largeur 2, 8 de largeur 1) = 24, chaque couleur une fois
def stripes(seed):
    rnd = random.Random(seed)
    kind = ['x', 'z', 'diag', 'anti', 'x', 'z', 'chevron', 'diag', 'frame', 'anti'][seed - 11]
    cols = COLORS[:]
    rnd.shuffle(cols)
    widths = [2] * 8 + [1] * 8
    rnd.shuffle(widths)
    L = [f'# Block Party — sol n°{seed} : bandes ({kind}), 16 couleurs (généré par tools/blockparty/gen_bp.py)']
    if kind in ('x', 'z'):
        p = 0
        for c, wd in zip(cols, widths):
            if kind == 'x':
                L.append(f'fill {X0 + p} 80 {Z0} {X0 + p + wd - 1} 80 {Z0 + N - 1} minecraft:{c}_concrete')
            else:
                L.append(f'fill {X0} 80 {Z0 + p} {X0 + N - 1} 80 {Z0 + p + wd - 1} minecraft:{c}_concrete')
            p += wd
        return L
    # bandes calculées case par case, regroupées en segments de ligne
    bounds = []
    p = 0
    for wd in widths:
        bounds.append((p, p + wd))
        p += wd

    def band_of(v, maxv):   # v ∈ [0, maxv) → bande 0..15 (bandes étirées sur maxv)
        u = v * 24 / maxv
        for i, (a, b) in enumerate(bounds):
            if a <= u < b:
                return i
        return 15

    def cell(i, j):
        if kind == 'diag':
            return band_of(i + j, 2 * N - 1)
        if kind == 'anti':
            return band_of(i + (N - 1 - j), 2 * N - 1)
        if kind == 'chevron':
            return band_of(i + abs(j - N // 2 + 0.5) * 2, N + N)
        if kind == 'frame':   # carrés concentriques (12 anneaux), les 4 extérieurs coupés en deux
            r = min(i, j, N - 1 - i, N - 1 - j)
            return 12 + r if r < 4 and i >= N // 2 else r
    for j in range(N):
        i = 0
        while i < N:
            b = cell(i, j)
            k = i
            while k + 1 < N and cell(k + 1, j) == b:
                k += 1
            L.append(f'fill {X0 + i} 80 {Z0 + j} {X0 + k} 80 {Z0 + j} minecraft:{cols[b]}_concrete')
            i = k + 1
    # toutes les couleurs présentes ?
    present = {cell(i, j) for i in range(N) for j in range(N)}
    assert present == set(range(16)), (seed, kind, sorted(present))
    return L


for s in range(11, 21):
    w(f'blockparty/pattern_{s}', stripes(s))

# ---------- nouvelle manche : le sol dépend du mode
lines = C.lines_of('blockparty/new_round')
start = lines.index('# Couleur cible')
head = ['# Nouvelle manche : nouveau sol (carrés, bandes ou les deux selon $bpm), nouvelle couleur, minuteur 5 s → 2 s',
        'scoreboard players add $rd mg.st 1',
        'execute if score $bpm mg.st matches 0 store result score $k mg.st run random value 1..10',
        'execute if score $bpm mg.st matches 1 store result score $k mg.st run random value 11..20',
        'execute if score $bpm mg.st matches 2 store result score $k mg.st run random value 1..20']
head += [f'execute if score $k mg.st matches {i} run function mg:blockparty/pattern_{i}' for i in range(1, 21)]
tail = [l for l in lines[start:] if l.strip() and 'blockparty/music_start' not in l]
w('blockparty/new_round', head + [''] + tail + ['function mg:blockparty/music_start'])

# ---------- musique : 32 pas, boucle ; tempo $bms ticks par pas (3 → 2 au fil des manches)
# notes (0..24, F#3 = 0) : do = 6, ré 8, mi 10, fa 11, sol 13, la 15, si 17, do' 18, ré' 20, mi' 22
MEL = [22, None, 18, None, 13, None, 18, 20, 20, None, 17, None, 13, None, 17, None,
       18, None, 15, None, 10, None, 15, 17, 17, None, 13, None, 20, 18, 17, 13]
BASS = {0: 6, 4: 6, 6: 18, 8: 13, 12: 13, 14: 1, 16: 15, 20: 15, 22: 3, 24: 13, 28: 13, 30: 1}
CHORD = {0: [10, 13], 8: [8, 13], 16: [6, 10], 24: [8, 11]}
M = ['# ▦ Block Party — un pas de musique ($bmp = 0..31), joué pour les joueurs et les spectateurs de la partie',
     'scoreboard players operation $bmp mg.st %= #32 mg.st']
snd = lambda s, p, v=0.7: f'playsound minecraft:block.note_block.{s} record @a[tag=!mg.surv] 0 81 6400 {v} {p} {v}'
for k in range(32):
    parts = []
    if MEL[k] is not None:
        parts.append(snd('bell' if k % 8 == 0 else 'pling', pitch(MEL[k]), 0.55))
    if k in BASS:
        parts.append(snd('bass', pitch(BASS[k]), 0.9))
    for n in CHORD.get(k, []):
        parts.append(snd('harp', pitch(n), 0.35))
    parts.append(snd('basedrum', 1, 0.8) if k % 4 == 0 else (snd('snare', 1.2, 0.5) if k % 4 == 2 else snd('hat', 1.6, 0.35)))
    if parts:
        M += [f'execute if score $bmp mg.st matches {k} run {p}' for p in parts]
w('blockparty/music', M)
w('blockparty/music_start', ['# Début de manche : la musique repart (plus vite au fil des manches)',
                             'scoreboard players set #32 mg.st 32', 'scoreboard players set $bmt mg.st 0',
                             'scoreboard players set $bmp mg.st 0', 'scoreboard players set $bms mg.st 3',
                             'execute if score $rd mg.st matches 7.. run scoreboard players set $bms mg.st 2',
                             'scoreboard players set $bsc mg.st 0'])
w('blockparty/music_tick', ['# Avance la musique d\'un tick',
                            'scoreboard players add $bmt mg.st 1',
                            'execute if score $bmt mg.st >= $bms mg.st run function mg:blockparty/music_step'])
w('blockparty/music_step', ['scoreboard players set $bmt mg.st 0', 'function mg:blockparty/music', 'scoreboard players add $bmp mg.st 1'])
# scratch de platine : 12 ticks de « bzibzibzi » (aller-retour de hauteur), puis silence
SCR = []
for t in range(12):
    up = t % 2 == 0
    p1 = round(1.9 - t * 0.05, 2) if up else round(0.55 + t * 0.03, 2)
    SCR.append(f'execute if score $bsc mg.st matches {12 - t} run playsound minecraft:block.note_block.didgeridoo record @a[tag=!mg.surv] 0 81 6400 0.9 {p1} 0.9')
    if t % 3 == 0:
        SCR.append(f'execute if score $bsc mg.st matches {12 - t} run playsound minecraft:ui.loom.take_result record @a[tag=!mg.surv] 0 81 6400 0.8 {1.8 if up else 0.7} 0.8')
    if t % 4 == 1:
        SCR.append(f'execute if score $bsc mg.st matches {12 - t} run playsound minecraft:block.grindstone.use record @a[tag=!mg.surv] 0 81 6400 0.5 2 0.5')
SCR.append('execute if score $bsc mg.st matches 1 run playsound minecraft:block.note_block.basedrum record @a[tag=!mg.surv] 0 81 6400 0.9 0.5 0.9')
w('blockparty/scratch', ['# « Bzibzibzi » : la platine du DJ s\'arrête (chaises musicales)'] + SCR + ['scoreboard players remove $bsc mg.st 1'])

# ---------- câblage : musique pendant la course, scratch au moment où le sol disparaît
C.patch('blockparty/run_tick', '# Compte à rebours de la manche', ['function mg:blockparty/music_tick'])
sn = C.lines_of('blockparty/strip_now')
sn = [l for l in sn if 'scoreboard players set $bsc mg.st 12' not in l and 'block.piston.contract' not in l and not l.startswith('stopsound') and l.strip()]
sn.insert(1, 'scoreboard players set $bsc mg.st 12')
sn.insert(1, 'stopsound @a[tag=!mg.surv] record')
w('blockparty/strip_now', sn + ['execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.piston.contract master @s ~ ~ ~ 0.6 0.8'])
C.patch('blockparty/pause_tick', 'scoreboard players remove $bt mg.st 1', ['execute if score $bsc mg.st matches 1.. run function mg:blockparty/scratch'], where='before')

# ---------- modes : ids 91 (bandes) et 92 (mixte) → jeu 28
C.go_range(92)
C.patch('core/request', '# Mini Party : 59 = 8 tours, 60 = 15 tours. Un jeu lancé hors Mini Party ($mpl) met fin à la partie en cours', [
    '# Block Party : 28 = carrés, 91 = bandes, 92 = mixte → jeu 28 + sol $bpm (0..2)',
    'execute if score $game mg.st matches 28 run scoreboard players set $bpm mg.st 0',
    'execute if score $game mg.st matches 91 run scoreboard players set $bpm mg.st 1',
    'execute if score $game mg.st matches 92 run scoreboard players set $bpm mg.st 2',
    'execute if score $game mg.st matches 91..92 run scoreboard players set $game mg.st 28', ''], where='before')
go = C.lines_of('blockparty/go')
msg = ['execute if score $bpm mg.st matches 1 run tellraw @a[tag=mg.play] {"text":"▦ Version BANDES : le sol est fait de bandes de couleur.","color":"light_purple"}',
       'execute if score $bpm mg.st matches 2 run tellraw @a[tag=mg.play] {"text":"▦ Version MIXTE : carrés ou bandes, ça change à chaque manche !","color":"light_purple"}']
txt = 'Quand la musique s\'arrête (bzibzibzi…), les autres blocs disparaissent !'
go = [l.replace('cours sur un bloc de cette couleur avant que tous les autres disparaissent !',
                'cours sur un bloc de cette couleur : ' + txt) for l in go if l not in msg and l.strip()]
i = go.index('function mg:blockparty/new_round')
go[i:i] = msg
w('blockparty/go', go)
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['stopsound @a record'])
print('Block Party OK')
