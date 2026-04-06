import matplotlib.pyplot as plt
import seaborn as sns

def plot_hist(df, col, save_path=None, title=None):
    plt.figure(figsize=(8,5))
    sns.histplot(df[col], bins=15, kde=True)
    if title: plt.title(title)
    plt.xlabel(col)
    plt.ylabel("Count")
    if save_path: plt.savefig(save_path)
    plt.show()

def plot_box(df, x_col, y_col, save_path=None, title=None):
    plt.figure(figsize=(8,5))
    sns.boxplot(data=df, x=x_col, y=y_col)
    if title: plt.title(title)
    if save_path: plt.savefig(save_path)
    plt.show()

def plot_count(df, x_col, y_col=None, hue=None, save_path=None, title=None):
    plt.figure(figsize=(10,6))
    if y_col:
        sns.countplot(data=df, y=y_col, x=x_col, hue=hue, order=df[y_col].value_counts().index)
    else:
        sns.countplot(data=df, x=x_col, hue=hue)
    if title: plt.title(title)
    if save_path: plt.savefig(save_path)
    plt.show()
