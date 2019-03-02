import pandas as pd

def create_directed_by_csv(dataframe):
    directed_by_df = dataframe[['director_name', 'movie_title']]
    directed_by_df = directed_by_df.rename(columns={'director_name': 'name'})
    directed_by_df['movie_title'] = directed_by_df['movie_title'].str.strip()
    return directed_by_df


def create_acted_in_csv(dataframe):
    acted_in_df = pd.DataFrame(columns=['name', 'movie_title'])

    num_rows = dataframe.shape[0]
    k = 0
    for i in range(num_rows):
        row = dataframe.iloc[i]
        movie_title = row['movie_title']
        movie_title = movie_title.rstrip()
        
        actor1 = row['actor_1_name']
        actor1 = actor1.rstrip()
        acted_in_df.loc[k] = [actor1, movie_title]
        k += 1

        actor2 = row['actor_2_name']
        actor2 = actor2.rstrip()
        acted_in_df.loc[k] = [actor2, movie_title]
        k += 1

        actor3 = row['actor_3_name']
        actor3 = actor3.rstrip()
        acted_in_df.loc[k] = [actor3, movie_title]
        k += 1

    return acted_in_df


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
    director_df = director_df.drop_duplicates(subset='director_name', keep="first")
    director_df = director_df.rename(columns={'director_name': 'name', 'director_facebook_likes': 'numfacebooklikes'})
    return director_df


def create_score_csv(dataframe):
    score_df = dataframe[['movie_title', 'num_critic_for_reviews', 'imdb_score']]
    score_df = score_df.rename(columns={'num_critic_for_reviews': 'numreviews'})
    score_df['movie_title'] = score_df['movie_title'].str.strip()
    return score_df


def create_movie_csv(dataframe):
    movie_df = dataframe[['movie_title', 'title_year', 'duration',
                          'budget', 'gross', 'content_rating',
                          'language', 'country', 'movie_facebook_likes']]
    movie_df = movie_df.astype({'title_year': int})
    movie_df = movie_df.rename(columns={'movie_title': 'title', 'title_year': 'year', 
                                        'content_rating': 'rating', 'movie_facebook_likes': 'numfacebooklikes'})
    movie_df['title'] = movie_df['title'].str.strip()
    return movie_df


def read_in_csv():
    df = pd.read_csv('movie_metadata.csv')
    bool_series = pd.notnull(df['director_name'])
    df = df[bool_series]

    bool_series = pd.notnull(df['movie_title'])
    df = df[bool_series]

    bool_series = pd.notnull(df['title_year'])
    df = df[bool_series]

    bool_series = pd.notnull(df['actor_1_name'])
    df = df[bool_series]

    bool_series = pd.notnull(df['actor_2_name'])
    df = df[bool_series]

    bool_series = pd.notnull(df['actor_3_name'])
    df = df[bool_series]

    df = df.drop_duplicates(subset='movie_title', keep="first")
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

    actor_df = actor_df.drop_duplicates(subset='actor_name', keep="first")
    return actor_df

df = read_in_csv()

director_df = create_director_csv(df)
director_csv = director_df.to_csv (r'directors.csv', index=False, header=True)

genre_df = create_genre_csv(df)
genre_csv = genre_df.to_csv (r'genres.csv', index=False, header=True)

actor_df = create_actor_csv(df)
actor_csv = actor_df.to_csv(r'actors.csv', index=False, header=True)

acted_in_df = create_acted_in_csv(df)
acted_in_csv = acted_in_df.to_csv(r'acted_in.csv', index=False, header=True)

directed_by_df = create_directed_by_csv(df)
directed_by_csv = directed_by_df.to_csv(r'directed_by.csv', index=False, header=True)

score_df = create_score_csv(df)
score_csv = score_df.to_csv(r'scores.csv', index=False, header=True)

movie_df = create_movie_csv(df)
movie_csv = movie_df.to_csv(r'movies.csv', index=False, header=True)