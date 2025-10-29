import pandas as pd
import streamlit as st

data = pd.read_csv('../data/spotify-2023.csv', 
    encoding="utf-8", 
    sep=',', 
    on_bad_lines='skip' 
)


data = data.dropna()
data = data.rename(columns={    
    'track_name':'nome_musica' ,'artist(s)_name':'nome_artista' ,'artist_count':'quantidade_de_artistas',
    'released_year':'ano_de_lancamento','released_month':'mes_de_lancamento', 'released_day':'dia_de_lancamento',
    'in_spotify_playlists':'em_playlists_do_spotify','in_spotify_charts':'em_paradas_do_spotify',
    'streams':'reproducoes','in_apple_playlists':'em_playlists_da_apple', 'in_apple_charts':'em_paradas_da_apple',
    'in_deezer_playlists':'em_playlists_do_deezer', 'in_deezer_charts':'em_paradas_do_deezer', 'in_shazam_charts':'em_paradas_do_shazam', 
    'bpm':'batidas_por_minutos','key':'tom', 'mode':'modo', 'danceability_%':'dancabilidade_%', 'valence_%':'positividade_%', 'energy_%':'energia_%',
    'acousticness_%':'acustica_%', 'instrumentalness_%':'instrumentalidade_%', 'liveness_%':'vivacidade_%', 'speechiness_%':'falabilidade_%'
    
})

todos_os_nomes = data['nome_artista'].str.split(',', n=1,expand=True)
data['nome_artista'] = todos_os_nomes[0].str.strip()
data['feat'] = todos_os_nomes[1].str.strip()

data = data[data['ano_de_lancamento'] <= 2023]



# data['reproducoes'].astype(int)
# data['reproducoes'] = data['reproducoes'].astype(int)
# print(data['reproducoes'].dtypes)
# # traduzindo o nome das tabelas

data['reproducoes'] = pd.to_numeric(data['reproducoes'], errors='coerce')
data.dropna(subset=['reproducoes'], inplace=True)
data['reproducoes'] = data['reproducoes'].astype(int)
# print(data['reproducoes'])

data['em_paradas_do_deezer'] = pd.to_numeric(data['em_paradas_do_deezer'], errors='coerce')
data.dropna(subset=['em_paradas_do_deezer'], inplace=True)
data['em_paradas_do_deezer'] = data['em_paradas_do_deezer'].astype(int)

data['em_playlists_do_deezer'] = pd.to_numeric(data['em_playlists_do_deezer'], errors='coerce')
data.dropna(subset=['em_playlists_do_deezer'], inplace=True)
data['em_playlists_do_deezer'] = data['em_playlists_do_deezer'].astype(int)

data['em_paradas_do_shazam'] = pd.to_numeric(data['em_paradas_do_shazam'], errors='coerce')
data.dropna(subset=['em_paradas_do_shazam'], inplace=True)
data['em_paradas_do_shazam'] = data['em_paradas_do_shazam'].astype(int)

data['batidas_por_minutos'] = pd.to_numeric(data['batidas_por_minutos'], errors='coerce')
data.dropna(subset=['batidas_por_minutos'], inplace=True)
data['batidas_por_minutos'] = data['batidas_por_minutos'].astype(int)

data.dropna(subset=['falabilidade_%'], inplace=True)
data['falabilidade_%'] = data['falabilidade_%'].astype(int)




