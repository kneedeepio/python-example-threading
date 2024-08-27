#!/usr/bin/env python3

### IMPORTS ###
import logging

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ThreadWrapper:
    def __init__(self, input_queue, other_data, number_threads, thread_class):
        self.logger = logging.getLogger(type(self).__name__)
        self.input_queue = input_queue
        self.other_data = other_data
        self.number_threads = number_threads
        self.thread_class = thread_class
        self._threads = []

    def start(self):
        self.logger.debug("Starting the threads.")
        for count in range(self.number_threads):
            self._threads.append(self.thread_class(self.input_queue, self.other_data))
        for thread in self._threads:
            thread.start()

    def stop(self):
        self.logger.debug("Stopping the threads.")
        for thread in self._threads:
            thread.stop()

    def any_alive(self):
        #self.logger.debug("Checking for any threads are still alive.") # noisy
        for thread in self._threads:
            if thread.is_alive():
                return True
        return False

    def join(self):
        self.logger.debug("Joining threads and waiting for them to finish.")
        for thread in self._threads:
            thread.join()
