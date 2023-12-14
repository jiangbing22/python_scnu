import matplotlib.pyplot as plt


def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    TransE = {'MRR': [], 'Hit': [], 'Epochs': []}
    TransD = {'MRR': [], 'Hit': [], 'Epochs': []}
    ComplEx = {'MRR': [], 'Hit': [], 'Epochs': []}
    init_data = None
    for line in lines:
        if line.strip() == 'TransE':
            init_data = 1
            continue
        elif line.strip() == 'TransD':
            init_data = 2
            continue
        elif line.strip() == 'ComplEx':
            init_data = 3
            continue
        if init_data == 1:
            mrr, hit, epochs = map(float, line.strip().split())
            TransE['MRR'].append(mrr)
            TransE['Hit'].append(hit)
            TransE['Epochs'].append(epochs)
        elif init_data == 2:
            mrr, hit, epochs = map(float, line.strip().split())
            TransD['MRR'].append(mrr)
            TransD['Hit'].append(hit)
            TransD['Epochs'].append(epochs)
        elif init_data == 3:
            mrr, hit, epochs = map(float, line.strip().split())
            ComplEx['MRR'].append(mrr)
            ComplEx['Hit'].append(hit)
            ComplEx['Epochs'].append(epochs)
    models = [TransE, TransD, ComplEx]
    return models


index = ['MRR', 'Hit']


def plot_metrics(models, vars):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 9))
    temp = 0
    colors = ['red', 'green', 'blue']
    model_names = ['TransE', 'TransD', 'ComplEx']
    for var in vars:
        for model, color,model_name in zip(models, colors,model_names):
            axes[temp].plot(model['Epochs'], model[var], label=model_name, color=color)
            axes[temp].set_title(f"{var} ")
            axes[temp].legend()

        temp = temp + 1
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    file_path = 'wn18.txt'
    data = read_data(file_path)
    plot_metrics(data, index)
