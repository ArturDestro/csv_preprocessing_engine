from pipeline import Pipeline

config = {
    "order": ["loader"],
    "loader": {
        "type": "csv",
        "path": "../dados_teste_engine.csv",
        "separator": ","
    }
}

pipeline = Pipeline(config)
df = pipeline.run()

print(df.head())
