def process_df_function(df):

    index_to_remove = df[df['Number of Outliers'] != 0]

    df.drop(index_to_remove.index, inplace=True)

    df.reset_index(drop=True, inplace=True)

    return df