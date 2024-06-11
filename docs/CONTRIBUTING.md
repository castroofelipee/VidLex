## Code

For small fixes or incremental improvements simply fork the repo and follow the process below. For larger changes submit an [RFC:](RFC.md)
1. [Fork](https://help.github.com/articles/fork-a-repo/) the repository and [clone](https://help.github.com/articles/cloning-a-repository/) your fork.

2. Start coding!
    - Implement your feature.
    - Check your code works as expected.
    - Run the code formatter: `clang-format -i $(git ls-files "*.cpp" "*.h")`

3. Commit your changes to a new branch (not `master`, one change per branch) and push it:
    - Commit messages should:
        - Header line: explain the commit in one line (use the imperative)
        - Be descriptive.
        - Have a first line with less than *80 characters* and have a second line that is *empty* if you want to add a description.

4. Once you are happy with your changes, submit a pull request.
     - Open the pull-request.
     - Add a short description explaining briefly what you've done (or if it's a work-in-progress - what you need to do)