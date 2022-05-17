import matplotlib.pyplot as plt
import pandas as pd
import re
import seaborn as sns
from typing import Tuple, List


def get_perplexities(*files) -> List[List[str]]:

    with open("mt-exercise-4/logs/baseline.log") as base, \
        open("mt-exercise-4/logs/prenorm.log") as pre, \
        open("mt-exercise-4/logs/postnorm.log") as post:

        base_ppl = re.findall(r"\sppl:\s\s\s?(\d\d?.\d+)", base.read())
        pre_ppl = re.findall(r"\sppl:\s\s\s?(\d\d?.\d+)", pre.read())
        post_ppl = re.findall(r"\sppl:\s\s\s?(\d\d?.\d+)", post.read())

    return [base_ppl, pre_ppl, post_ppl]



def get_data_frame(models: List[str], step:List[str], 
                    ppls: List[str]) -> pd.DataFrame:
    """Generate data frame for creating tables and charts:
        :param models: List containing models' names to define columns.
        :param step: List containing epochs.
        :param ppl: List of tuples containing perplexity values.
        :return: Data frame with perplexities of each model.
    """
    df = pd.DataFrame(columns = ["Validation ppl"] + models)

    for model, ppl in zip(models, ppls):
        df["Validation ppl"] = step
        df[model] = ppl
        
    return df

            
def save_charts(name: str, table: pd.DataFrame):
    """Generate line chart three models.
        :param name: Path to save a line chart as string.
        :param table: Data frame for the corresponding perplexity.
    """
    sns.set(font_scale=1.5, style="darkgrid")
    table = table.drop(labels="Validation ppl", axis=1).apply(pd.to_numeric)
    sns.relplot(data=table, kind="line", palette="tab10", height=6, aspect=1.5).set(ylabel="Perplexity", xlabel="Epoch step")
    plt.savefig("line_chart.png")


def main():

    models = ["Baseline", "Prenorm", "Postnorm"]
    step = [num for num in range(500, 42500, 500)]

    ppls = get_perplexities()
    table = get_data_frame(models, step, ppls)
    table.to_markdown("table.md", index=False)
    table.to_latex("table.tex", index=False)
    save_charts("line_chart.png", table)

    
if __name__ == '__main__':
    main()

