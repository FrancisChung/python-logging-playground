from slogger import SLogger
import logging

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

if __name__ == "__main__":
    # Going to be using 2 Loggers during this sequence of tests
    # Apologies if the code below looks messy. I tried my best in my limited to time to make it more readable

    base_logger = SLogger("Base Logger")    # Base(line) Logger will be at INFO loglevel at all times
    test_logger = SLogger("Test Logger")    # Test Logger's LogLevel will change over the course of the tests
    base_logger.warning("***** PRE TEST *****")
    base_logger.info("#1. This should show. #2 Should be invisible")
    test_logger.info("#1. This should show. #2 Should be invisible")
    base_logger.debug("#2. Debug should not show")
    test_logger.debug("#2. Debug should not show")
    base_logger.warning("")
    # Scenario 1 : Use change loglevel using getLogger().level. Seems to work going up but not down. Try go which doesn't work as advertised

    base_logger.warning("***** Scenario 1: getLogger().level up (Works) *****")
    base_logger.info("#3. Base LogLevel remains at info")
    # test_logger.info(f"Changing Test LogLevel to {test_logger.setLevel(10)}")
    # test_logger.info(f"Changing Test LogLevel to {logging.getLogger("Test Logger").setLevel(10)}")
    logging.getLogger("Test Logger").level =30
    test_logger.info(f"#3. Test Logger loglevel set to {logging.getLogger('Test Logger').level}")  # Level 'up' to Warning
    base_logger.warning("#4. Warning should show")
    test_logger.warning("#4. Warning should show. Going up Levels seems to work")
    base_logger.warning("")

    # Scenario 2 : Use change loglevel using getLogger().level to go down to debug. It doesn't work

    base_logger.warning("***** Scenario 2: getLogger().level down (Doesn't work) *****")
    logging.getLogger("Test Logger").level =10
    test_logger.info(f"#5. Test Logger loglevel set to {logging.getLogger('Test Logger').level}")  # Level 'down' to debug
    base_logger.debug("#6. Debug should not show")
    test_logger.debug("#6. Debug should show. But it doesn't so going down Levels does not work")
    base_logger.warning("")

    # Scenario 3 : Use slogger's setLevel (down) command which works

    base_logger.warning("***** Scenario 3: Tlogger setLevel down (Works) *****")
    test_logger.info(f"#7. Use SLogger to change Test LogLevel to {test_logger.setLevel(10)}")  # Debug
    base_logger.debug("#8. Debug should not show")
    test_logger.debug("#8. Debug should show, so SLogger works")
    base_logger.warning("")

    # Scenario 4 : Use slogger's setLevel (up) command which works
    # test_logger should not show debug, info, warning
    base_logger.warning("***** Scenario 4: Tlogger setLevel Up (Works) *****")
    test_logger.error(f"#9. Use SLogger to change Test LogLevel to {test_logger.setLevel(40)}")  # Error
    base_logger.debug("#10. Debug should not show")
    test_logger.debug("#10. Debug should NOT show, so SLogger works")
    base_logger.info("#11. Info should show")
    test_logger.info("#11. Info should NOT show, so SLogger works")
    base_logger.warning("#12. Warning should show")
    test_logger.warning("#12. Warning should NOT show, so SLogger works")
    base_logger.error("#13. Error should show")
    test_logger.error("#13. Error should show, so SLogger works")
    base_logger.critical("#14. Critical should show")
    test_logger.critical("#14. Critical should show, so SLogger works")

    base_logger.warning("")


    # Scenario 5 : Use logging.basicConfig which causes duplicate logs and also doesn't work

    base_logger.warning("***** Scenario 5: basicConfig *****")
    # Set log level it to Highest (50, Critical) again to ensure there's no side effects following through
    test_logger.critical(f"#15. Use SLogger to change Test LogLevel to {test_logger.setLevel(50)}")  # Critical
    base_logger.warning("")

    logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s %(funcName)s] %(message)s', level=40)
    base_logger.info("#16. LogLevel Set to 40. Info should not show but shows. Base Logger has started to duplicate also. BasicConfig seems to have no effect")
    test_logger.info("#16. Info should not show")
    logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s %(funcName)s] %(message)s', level=20)
    base_logger.info("#17. LogLevel set to 20. Base Logger is is still duplicating. Test Logger should show but not showing")
    test_logger.info("#17. Info is not showing. BasicConfig did not work for Test Logger")
    base_logger.warning("")




