# caz in care o sa fac interfata pentru ac tema :D
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import chromosome as chrm

matplotlib.use('TkAgg')

def visualizer(config: dict, generations: list[list[chrm.Chromosome]], delay: float) -> None:
    plt.ion()

    # setarea intervalului
    max_x = -config["b"] / (2 * config["a"])
    max_y = chrm.get_fitness(max_x, config)

    for generation, population in enumerate(generations, 1):
        # repaint
        plt.clf()

        # luam valorile de pe grafic according to generatia la care ma aflu
        x = np.linspace(config["start"], config["end"], 1000)
        y = chrm.get_fitness(x, config)
        x_values = [chromosome.decimal for chromosome in population]
        y_values = [chromosome.fitness for chromosome in population]

        # cromozomul best for now
        best_chromosome = max(population, key=lambda chrom: chrom.fitness)

        # plotarea graficului: functia si valorile + marcarea celui mai bun
        plt.plot(x, y, 'gray', linewidth=2,
                 label="f(x) = " + str(config["a"]) + "x² + " + str(config["b"]) + "x + " + str(config["c"]))
        plt.scatter(x_values, y_values, c='pink', s=25, zorder=2, label="Generation " + str(generation) + " Chromosomes")

        plt.scatter(best_chromosome.decimal, best_chromosome.fitness, c='purple', s=25, marker='*', zorder=3, label=f"Best: {best_chromosome.fitness:0.7f}")

        # axa xoy cu coord x f(x)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title("Cromozomii selectati pe functie - Generatia " + str(generation))
        plt.gcf().canvas.manager.set_window_title("Evolutie")
        plt.legend()

        # distanta intre generatii
        plt.pause(delay)

    plt.ioff()
    plt.show()