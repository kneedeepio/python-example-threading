#!/usr/bin/env python3

### IMPORTS ###
import logging
import queue
import threading

import time

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class CustomThread(threading.Thread):
    def __init__(self, input_queue, other_data):
        super().__init__()
        self.logger = logging.getLogger(type(self).__name__)
        self._shutdown = False
        self._input_queue = input_queue
        self.other_data = other_data

    def stop(self):
        self.logger.debug("Thread Stop Command")
        self._shutdown = True

    def run(self):
        self.logger.debug("Starting the thread")
        while not self._shutdown:
            try:
                work_item = self._input_queue.get_nowait()
            except queue.Empty:
                self.logger.debug("No more work items, shutting down.")
                self.stop()
                break # Force the while loop to end

            # Do work on the work_item here
            time.sleep(3)
            self.logger.info(work_item)

            self._input_queue.task_done()
        self.logger.debug("Ending the thread")
