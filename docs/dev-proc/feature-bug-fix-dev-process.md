# Features and bug fixes development

We are in favor of Test Driven Bug Fixing methodology for which process looks
as follows:

1. Create automated test that validates feature or reproduces bug - test fails at
   this point
2. Pull upstream `master` branch to Dasharo forked repository `master` branch
3. Merge `master` to `<platform>/develop`
4. Create new branch `<platform>/<feature>` from `<platform>/develop`
5. Commit changes to `<platform>/<feature>`
6. Run test written in point 1 and make sure it pass.
7. Run `<platform>` regression test suite and make sure new feature does not
   introduce new bugs.
8. Submit PR to `<platform>/develop`
