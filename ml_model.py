from sklearn.ensemble import RandomForestClassifier

def run_model(df):

    # CREATE TARGET
    # This predicts if NEXT day's return is positive (1) or negative (0)
    df["Target"] = (df["Return"].shift(-1) > 0).astype(int)

    # Remove last row (because shift creates NaN)
    df = df.dropna()

    # SPLIT DATA
    # Train = past data
    # Test = future data (this is important for realism)

    train = df[df.index < "2022-01-01"]
    test = df[df.index >= "2022-01-01"]

    # FEATURES (what the model uses to learn patterns)
    X_train = train[["SMA_10", "SMA_50"]]
    y_train = train["Target"]

    X_test = test[["SMA_10", "SMA_50"]]
    y_test = test["Target"]

    # CREATE MODEL
    # RandomForest = many decision trees combined
    model = RandomForestClassifier()

    # TRAIN MODEL
    # The model learns patterns from historical data
    model.fit(X_train, y_train)

    # PREDICT ON NEW DATA
    predictions = model.predict(X_test)

    # CALCULATE ACCURACY
    # Compare predictions vs real outcomes
    accuracy = (predictions == y_test).mean()
    

# GET LATEST DATA FOR REAL PREDICTION
    # This is today's market condition (what we know now)
    latest_data = df[["SMA_10", "SMA_50"]].iloc[-1:]

    # NOTE:
    # iloc[-1:] keeps it as a table (DataFrame)
    # iloc[-1] would break model input

    # MODEL MAKES NEXT DAY PREDICTION
    prediction = model.predict(latest_data)[0]

    # Convert to human-readable output
    if prediction == 1:
        signal = "UP"
    else:
        signal = "DOWN"
    # IMPORTANT:
    print("DEBUG: returning signal:", signal)
    # We RETURN the result instead of printing
    return accuracy,signal
   