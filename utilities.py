import numpy as np
import pandas as pd 

def predict_input(single_input, imputer, scaler, numeric_cols, encoder, categorical_cols, model):
    input_df = pd.DataFrame([single_input])
    print(single_input)
    print(single_input['Age'])

    # Transform numeric_cols
    input_df['Age'] = imputer.transform(input_df[['Age']])

    input_df[numeric_cols]= scaler.transform(input_df[numeric_cols])

    input_df["Title"] = input_df['Name'].str.extract(r',\s*([^\.]+)\.')

    input_df['Deck'] = input_df['Cabin'].astype(str).str[0]
    input_df = input_df.drop(columns=['Cabin', 'Name'])

    #encoded_data = encoder.transform(input_df[categorical_cols])

    # Transform cateorical cols
    encoded_cols = list(encoder.get_feature_names_out(categorical_cols))
    input_df_encoded= pd.DataFrame(encoder.transform(input_df[categorical_cols]), columns=encoded_cols, index=input_df.index)
    input_df= pd.concat([input_df.drop(columns=categorical_cols), input_df_encoded], axis=1)

    pred = model.predict(input_df)[0]
    probs = model.predict_proba(input_df)[0][list(model.classes_).index(pred)]

    return pred, probs
