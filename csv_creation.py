import pandas as pd

def create_genre_csv(dataframe):
    genre_df = pd.DataFrame(columns=['movie_title', 'genre'])
    
    num_rows = dataframe.shape[0]
    k = 0
    for i in range(num_rows):
        row = dataframe.iloc[i]
        movie_title = row['movie_title']
        movie_title = movie_title.rstrip()
        genres = row['genres']
        genres = genres.rstrip()
        genres = genres.split('|')
        for j in range(len(genres)):
            genre_df.loc[k] = [movie_title, genres[j]]
            k += 1
        
    return genre_df


def create_director_csv(dataframe):
    director_df = dataframe[['director_name', 'director_facebook_likes']]
    director_df.drop_duplicates(subset='director_name', keep="first")
    return director_df


def read_in_csv():
    df = pd.read_csv('movie_metadata.csv')
    bool_series = pd.notnull(df['director_name'])
    df = df[bool_series]

    bool_series = pd.notnull(df['movie_title'])
    df = df[bool_series]

    bool_series = pd.notnull(df['actor_1_name'])
    df = df[bool_series]

    bool_series = pd.notnull(df['actor_2_name'])
    df = df[bool_series]

    bool_series = pd.notnull(df['actor_3_name'])
    df = df[bool_series]
    return df


def create_actor_csv(dataframe):
    actor_df = pd.DataFrame(columns=['actor_name', 'numfacebooklikes'])

    num_rows = dataframe.shape[0]
    k = 0
    for i in range(num_rows):
        row = dataframe.iloc[i]
        actor1 = row['actor_1_name']
        actor1 = actor1.rstrip()
        actor1_likes = row['actor_1_facebook_likes']
        actor_df.loc[k] = [actor1, actor1_likes]
        k += 1

        actor2 = row['actor_2_name']
        actor2 = actor2.rstrip()
        actor2_likes = row['actor_2_facebook_likes']
        actor_df.loc[k] = [actor2, actor2_likes]
        k += 1

        actor3 = row['actor_3_name']
        actor3 = actor3.rstrip()
        actor3_likes = row['actor_3_facebook_likes']
        actor_df.loc[k] = [actor3, actor3_likes]
        k += 1

    actor_df.drop_duplicates(subset='actor_name', keep="first")
    return actor_df

df = read_in_csv()
#director_df = create_director_csv(df)
#genre_df = create_genre_csv(df)
actor_df = create_actor_csv(df)