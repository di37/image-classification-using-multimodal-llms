# Custom Logger - `custom_logger`

This module provides a customized logging setup for the project. It implements a rotating file handler to manage log file sizes and a console handler for immediate feedback. The logger captures different levels of messages, with more verbose logging to files and concise output to the console.

To use in other parts of the project, simply import the logger with `from custom_logger import logger` and use methods like `logger.info()`, `logger.debug()`, etc.