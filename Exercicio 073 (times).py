times = ('Internacional', 'Flamengo', 'São Paulo', 'Atlético-MG', 'Fluminense','Palmeiras', 'Grêmio', 'Santos',
         'Athletico', 'Corinthians','Red Bull Bragantino', 'Ceará','Atlético-GO', 'Sport','Fortaleza','Bahia',
         'Vasco', 'Goiás', 'Coritiba','Botafogo')
print(f'os 5 primeiro times são: {times[0:5]}')
print(f'os 4 ultimos colocados são {times[16:20]}') # ou desse outro jeito {times{-4:}}
print(f'em ordem alfabetica {sorted(times)}')
print(times.index('Ceará')+ 1 )