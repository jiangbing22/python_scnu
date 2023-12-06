import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def biominal():
    n_trials = 50  # 试验次数
    p_success = 0.5  # 成功的概率

    uniform_samples = np.random.rand(1000, n_trials)
    binomial_samples = (uniform_samples < p_success).sum(axis=1)

    # 画出二项分布样本的直方图
    plt.hist(binomial_samples, bins=np.arange(0, n_trials + 2) - 0.5, edgecolor='black', alpha=0.7)
    plt.title('Binomial')
    plt.xlabel('Number of Successes')
    plt.ylabel('Frequency')
    plt.savefig("Biominal.png",format="png")
    plt.close()
def normal():
    sample_size = 1000
    # 生成正态分布样本（算法1：均匀分布）
    def generate_normal_uniform(size):
        u1 = np.random.rand(size)
        u2 = np.random.rand(size)
        z = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
        return z

    # 生成正态分布样本（算法2：标准正态分布分布律）
    def generate_normal_cdf(size):
        u = np.random.rand(size)
        z = norm.ppf(u)
        return z

    # 生成正态分布样本
    normal_samples_uniform = generate_normal_uniform(sample_size)
    normal_samples_cdf = generate_normal_cdf(sample_size)

    # 绘制正态分布样本的直方图
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(normal_samples_uniform, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Normal Distribution (Uniform Algorithm)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    plt.hist(normal_samples_cdf, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Normal Distribution (CDF Algorithm)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    # 保存图片
    plt.savefig("normal_distributions.png", format="png")
    plt.close()



def central_limit_theorem(sample_size=1000, n_trials=100, p_success=0.5):
    # 生成均匀分布样本
    uniform_samples = np.random.rand(sample_size, 100)

    # 生成两点分布样本
    binomial_samples = (np.random.rand(sample_size, n_trials) < p_success).sum(axis=1)

    # 计算均匀分布的和的分布
    sum_uniform_distribution = uniform_samples.sum(axis=1)

    # 计算两点分布的和的分布
    sum_binomial_distribution = binomial_samples



    # 绘制均匀分布和两点分布的正态分布拟合曲线
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(sum_uniform_distribution, bins=30, density=True, edgecolor='black', alpha=0.7)

    # 计算均匀分布的正态分布参数（均值和标准差）
    mu_uniform, std_uniform = norm.fit(sum_uniform_distribution)
    x_uniform = np.linspace(min(sum_uniform_distribution), max(sum_uniform_distribution), 100)
    p_uniform = norm.pdf(x_uniform, mu_uniform, std_uniform)
    plt.plot(x_uniform, p_uniform, 'k', linewidth=2)
    title_uniform = "Fit results: mu = %.2f,  std = %.2f" % (mu_uniform, std_uniform)
    plt.title('Uniform Distribution Sum vs Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Density')

    plt.subplot(1, 2, 2)
    plt.hist(sum_binomial_distribution, bins=30, density=True, edgecolor='black', alpha=0.7)

    # 计算两点分布的正态分布参数（均值和标准差）
    mu_binomial, std_binomial = norm.fit(sum_binomial_distribution)
    x_binomial = np.linspace(min(sum_binomial_distribution), max(sum_binomial_distribution), 100)
    p_binomial = norm.pdf(x_binomial, mu_binomial, std_binomial)
    plt.plot(x_binomial, p_binomial, 'k', linewidth=2)
    title_binomial = "Fit results: mu = %.2f,  std = %.2f" % (mu_binomial, std_binomial)
    plt.title('Binomial Distribution Sum vs Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Density')

    plt.tight_layout()
    plt.savefig("central.png", format="png")


def large_numbers():
    def law_of_large_numbers_demo(ax, distribution_type, true_mean, sample_sizes):
        means = []

        for size in sample_sizes:
            if distribution_type == 'uniform':
                samples = np.random.rand(size)
            elif distribution_type == 'binomial':
                samples = np.random.binomial(1, 0.2, size)
            elif distribution_type == 'normal':
                samples = np.random.normal(0, 1, size)
            else:
                raise ValueError("Invalid distribution type")


            sample_mean = np.mean(samples)
            means.append(sample_mean)


        ax.plot(sample_sizes, means, label=f'{distribution_type.capitalize()} Distribution')


        ax.axhline(true_mean, color='red', linestyle='--', label=f'True Mean ({distribution_type.capitalize()})')


    true_mean_uniform = 0.5
    true_mean_binomial = 0.2
    true_mean_normal = 0
    sample_sizes = [10,50, 100,200, 500,800,1000,2000,5000,6000,8000, 10000]


    fig, ax = plt.subplots()


    law_of_large_numbers_demo(ax, 'uniform', true_mean_uniform, sample_sizes)
    law_of_large_numbers_demo(ax, 'binomial', true_mean_binomial, sample_sizes)
    law_of_large_numbers_demo(ax, 'normal', true_mean_normal, sample_sizes)


    ax.set_xscale('log')
    ax.set_title('Law of Large Numbers')
    ax.set_xlabel('Sample Size (log scale)')
    ax.set_ylabel('Sample Mean')
    ax.legend()
    plt.savefig("large_numbers.png", format="png",dpi=1000)


if __name__ == '__main__':
    biominal()
    normal()
    central_limit_theorem()
    large_numbers()
