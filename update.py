import os

students = [
    ('Gily20', 'Gilary'),
    ('Japonte14', 'Jose Aaron'),
    ('Josanto21', 'Josue Antonio'),
    ('Mario-Barsallo', 'Mario Esteban Barsallo Vasquez'),
    ('Roseroselynn', 'Roselyn'),
    ('Savamg', 'Samantha Valentina'),
    ('Vianvavc', 'Vianca Vidal'),
    ('Villamil0128', 'Cesar Adrian'),
    ('aescobarg19', 'Ailyn Somilka'),
    ('arojasve-wq', 'Alice Alexandra'),
    ('bcharris1024-cloud', 'Brittany Grace Charris Wardrope'),
    ('ct24saretmedina', 'Saret Jezreel'),
    ('fbarriac', 'Fernando Ulises'),
    ('haza507', 'Hazael Eliezer'),
    ('jenireepr', 'Jeniree Parra'),
    ('jquielh1508', 'Juan Antonio'),
    ('lizmarie82', 'Lizmarie Loraine'),
    ('lventeu', 'Laura Victoria'),
    ('mgiraldoh-debug', 'Milena'),
    ('mrodriguezhe-alt', 'Maykol Arcenio'),
    ('olmedoalonso', 'Olmedo Alexander'),
    ('pablo-hdz', 'Pablo Daniel Hernandez Melendez'),
    ('skevin507', 'Kevin Alexander'),
    ('katherinegalvez047-stack', 'Katherine Galvez'),
    ('fpena1703-bit', 'Fidel Antonio Pena'),
]

base = '4. Estudiantes'

for user, name in students:
    path = os.path.join(base, user, 'README.md')
    lines = [
        '# ' + name,
        '',
        'Bienvenido al repositorio del curso **SINT-741 - Curso Activadores** - Universidad Cenfotec.',
        '',
        'Esta es tu carpeta personal. Aqui subes todos tus trabajos y entregas del curso.',
        '',
        '**Usuario GitHub:** ' + user,
        '',
        '## Mis entregas',
        '',
        '| # | Trabajo | Carpeta | Estado |',
        '|---|---------|---------|--------|',
        '| 1 | Laboratorio 1 | `lab-01/` | Pendiente |',
        '| 2 | Laboratorio 2 | `lab-02/` | Pendiente |',
        '| 3 | Proyecto final | `proyecto-final/` | Pendiente |',
        '',
        '## Como subir mis trabajos',
        '',
        'Consulta la guia completa con imagenes en **4. Estudiantes/README.md**.',
        '',
        '## Estructura sugerida',
        '',
        '```',
        user + '/',
        '+-- README.md',
        '+-- lab-01/',
        '+-- lab-02/',
        '+-- proyecto-final/',
        '```',
        '',
    ]
    content = '\n'.join(lines)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('OK:', user)

print('Listo - todos los README actualizados')
