#!/usr/bin/env python3

### IMPORTS ###
import logging
import queue

import time

from customthread import CustomThread
from threadwrapper import ThreadWrapper

### GLOBALS ###
NUM_THREADS = 3

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    logging.basicConfig(
        format = "%(asctime)s:%(levelname)s:%(name)s:%(funcName)s: %(message)s",
        level = logging.DEBUG
    )

    logging.debug("Preparing the data and environment.")

    # Create some other data.  This can be config data or login data required
    #    by the thread.
    other_data = {}

    # Create some work items for the threads
    work_items = []
    for count in range(NUM_THREADS * 100):
        work_items.append("This is work item number {}.".format(count))

    # Queue up work items
    work_queue = queue.Queue()
    for item in work_items:
        work_queue.put(item)

    # Run the threads
    logging.debug("Starting the threads.")
    wrapper = ThreadWrapper(work_queue, other_data, NUM_THREADS, CustomThread)
    wrapper.start_threads()

    # Idle while the threads are working.  Could do other work here.
    while wrapper.any_threads_alive():
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            logging.warning("KeyboardInterrupt, stopping threads")
            wrapper.stop_threads()

    # Wait for the threads to finish
    logging.debug("Waiting for threads to finish.")
    wrapper.join_threads()
    logging.debug("Threads have completed.")

if __name__ == "__main__":
    main()
