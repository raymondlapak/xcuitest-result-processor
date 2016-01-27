XCUITest (Xcode UI test framework) results parser
===
When you run UI tests in Xcode or using xcodebuild, the results of test execution get stored in a huge .plist file that can be opened in Xcode for later analysis. However, it's not convenient to use it as is to understand the reasons of test failures after the tests are run at CI servers. This project is aimed to convert XCUITest results to a more human friendly format.
   
Project goals:

* File system report. For each test case executed by Xcode, create a directory with test results, associated screenshots and a gif with them.

* Html report. A web interface to browse the file system report.

It should be possible to easily extract information about the failing tests for displaying together with other build artifacts at CI servers.

Usage
===
* `xcuitest-result-processor [options] <path-to-plist>` for converting test results.

* `xcuitest-result-processor -h` for help.

License
===
Free as whatever free you can imagine.