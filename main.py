from tlogger import TLogger

if __name__ == "__main__":
    base_logger = TLogger("Base Logger")
    test_logger = TLogger("Test Logger")
    base_logger.info("This should show - 1")
    test_logger.info("This should show - 1")
    base_logger.debug("Debug should not show - 2")
    test_logger.debug("Debug should not show - 2")
    base_logger.info("Base LogLevel remains at info - 3")
    test_logger.info(f"Changing Test LogLevel to {test_logger.setLevel(10)}")
    base_logger.debug("Debug should not show - 4")
    test_logger.debug("Debug should show - 4")
