def checking_data_null(df):
    null_counts = df.isnull().sum()
    print("Null values in each column:")
    print(null_counts)
    # create a boolean mask of null values
    mask = df.isnull().any(axis=1)

    # filter the DataFrame to only show rows with null values
    print("\n\nDetails of rows with null values:")
    null_rows = df[mask]
    # print(null_rows)

    print("\n\n\nIndex of rows with null values:")
    invalid_rows = [index for index, row in df.iterrows() if row.isnull().any()]
    print(invalid_rows)

    return null_rows
