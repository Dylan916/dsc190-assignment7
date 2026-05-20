import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv('data/features/events.csv')
    df['duration_minutes'].hist()
    return


if __name__ == "__main__":
    app.run()
