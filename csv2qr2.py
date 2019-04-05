from functools import partial
from concurrent import futures

from csv2qr import autodetect, create_qr, main

# MAX_WORKERS = 10


def process_lines(csvreader, header, args):
    partial_function = partial(create_qr, header=header, args=args)
    # with futures.ThreadPoolExecutor(MAX_WORKERS) as executor:
    with futures.ProcessPoolExecutor() as executor:
        urls = executor.map(partial_function, csvreader)
    return urls


if __name__ == "__main__":
    main(process_lines)
