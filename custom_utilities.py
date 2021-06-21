from time import time


def progress_bar(iterable, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    """
    Credit to @Greenstick on StackOverflow for the the general setup.
    Changes: Added iteration timer
    """
    total = len(iterable)
    start_time = time()

    # Progress Bar Printing Function
    def printProgressBar(iteration):
        delta_time = (time() - start_time) / (iteration + 1)
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}, {delta_time:.2f} it/s, {iteration = }', end=print_end)

    # Initial Call
    printProgressBar(0)

    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()
