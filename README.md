# python-logging-playground

Supplementary Materials for StackOverflow answer : https://stackoverflow.com/a/70360470/1622880

slogger.py contains a sample logger based on the standard logging library that correct changes loglevels without
using basicConfig that affects all loggers

main.py contains some sample test sequences showing the various scenarios where changing levels work and don't work. 

To run the tests: run python main.py to see the test results.

It's recommended to have main.py code side by side with the console results to understand the test output


```
λ python main.py
2021-12-15 19:12:06,183 WARNING [BASE LOGGER warning] ***** PRE TEST *****
2021-12-15 19:12:06,183 INFO [BASE LOGGER info] #1. This should show. #2 Should be invisible
2021-12-15 19:12:06,183 INFO [TEST LOGGER info] #1. This should show. #2 Should be invisible
2021-12-15 19:12:06,183 WARNING [BASE LOGGER warning]
2021-12-15 19:12:06,183 WARNING [BASE LOGGER warning] ***** Scenario 1: getLogger().level up (Works) *****
2021-12-15 19:12:06,183 INFO [BASE LOGGER info] #3. Base LogLevel remains at info
2021-12-15 19:12:06,185 INFO [TEST LOGGER info] #3. Test Logger loglevel set to 30
2021-12-15 19:12:06,185 WARNING [BASE LOGGER warning] #4. Warning should show
2021-12-15 19:12:06,185 WARNING [TEST LOGGER warning] #4. Warning should show. Going up Levels seems to work
2021-12-15 19:12:06,185 WARNING [BASE LOGGER warning]
2021-12-15 19:12:06,185 WARNING [BASE LOGGER warning] ***** Scenario 2: getLogger().level down (Doesn't work) *****
2021-12-15 19:12:06,186 INFO [TEST LOGGER info] #5. Test Logger loglevel set to 10
2021-12-15 19:12:06,186 WARNING [BASE LOGGER warning]
2021-12-15 19:12:06,186 WARNING [BASE LOGGER warning] ***** Scenario 3: Tlogger setLevel down (Works) *****
2021-12-15 19:12:06,186 INFO [TEST LOGGER info] #7. Use SLogger to change Test LogLevel to 10
2021-12-15 19:12:06,186 DEBUG [TEST LOGGER debug] #8. Debug should show, so SLogger works
2021-12-15 19:12:06,187 WARNING [BASE LOGGER warning]
2021-12-15 19:12:06,187 WARNING [BASE LOGGER warning] ***** Scenario 4: Tlogger setLevel Up (Works) *****
2021-12-15 19:12:06,187 ERROR [TEST LOGGER error] #9. Use SLogger to change Test LogLevel to 40
2021-12-15 19:12:06,187 INFO [BASE LOGGER info] #11. Info should show
2021-12-15 19:12:06,187 WARNING [BASE LOGGER warning] #12. Warning should show
2021-12-15 19:12:06,188 ERROR [BASE LOGGER error] #13. Error should show
2021-12-15 19:12:06,188 ERROR [TEST LOGGER error] #13. Error should show, so SLogger works
2021-12-15 19:12:06,188 CRITICAL [BASE LOGGER critical] #14. Critical should show
2021-12-15 19:12:06,188 CRITICAL [TEST LOGGER critical] #14. Critical should show, so SLogger works
2021-12-15 19:12:06,188 WARNING [BASE LOGGER warning]
2021-12-15 19:12:06,188 WARNING [BASE LOGGER warning] ***** Scenario 5: basicConfig *****
2021-12-15 19:12:06,189 CRITICAL [TEST LOGGER critical] #15. Use SLogger to change Test LogLevel to 50
2021-12-15 19:12:06,189 WARNING [BASE LOGGER warning]
2021-12-15 19:12:06,189 INFO [BASE LOGGER info] #16. LogLevel Set to 40. Info should not show but shows. Base Logger has started to duplicate also. BasicConfig seems to have no effect
2021-12-15 19:12:06,189 INFO [BASE LOGGER info] #16. LogLevel Set to 40. Info should not show but shows. Base Logger has started to duplicate also. BasicConfig seems to have no effect
2021-12-15 19:12:06,189 INFO [BASE LOGGER info] #17. LogLevel set to 20. Base Logger is is still duplicating. Test Logger should show but not showing
2021-12-15 19:12:06,189 INFO [BASE LOGGER info] #17. LogLevel set to 20. Base Logger is is still duplicating. Test Logger should show but not showing
2021-12-15 19:12:06,189 INFO [BASE LOGGER info] Base Logger is duplicating
2021-12-15 19:12:06,189 INFO [BASE LOGGER info] Base Logger is duplicating
2021-12-15 19:12:06,190 CRITICAL [TEST LOGGER critical] Test Logger is duplicating
2021-12-15 19:12:06,190 CRITICAL [TEST LOGGER critical] Test Logger is duplicating

```
