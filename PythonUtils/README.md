# PythonUtils
-   Random, possibly useful stuff\...

-   Some of the utilities here will contain file I/O so please use
    extreme caution!

-   Current progress:

    -   Search Indexing:

        -   **CreateCache.py** creates cache for files/directories
            visited by the program. It creates a HashMap for a key of
            string of two chars from the file/directory name and for a
            value of HashSet containing the full file/directory
            addresses. For each name, it will take every pair of
            adjacent chars and repeat the hashing process.

        -   **FileSearch.py** allows users to search for a desired
            search term. It will take each pair of adjacent chars, read
            the cached HashSet and sequentially intersect among the
            sets.

        -   Few miscellaneous optimizations were done to allow indexing
            to finish within a reasonable timeline. (\~1.5hrs -- \~2.0
            hrs for 900GB worth of files and directories, although names
            of length greater than 40 were ignored).

    -   Algorithms and Data Structures Toolbox:

        -   Currently only has a simple queue structure that's used in
            **CreateCache.py**. Thought about using min priority queue
            to avoid queue size from diverging but it seems like it's
            unnecessary since when using a regular queue, the queue size
            stabilizes around 25k files and directories. Very
            insignificant memory usage.

        -   Planning on adding more algorithms and data structures for
            both practice and for requirements to grow this utilities
            library.

*\"PythonUtils\" Disclaimer of Liability:*

*Please read this disclaimer carefully before using \"PythonUtils\".*

*\"PythonUtils\" is provided \"as is\" without any representations or
warranties, express or implied. The software provider makes no
representations or warranties in relation to \"PythonUtils\" or the
information and materials provided with the software.*

*In no event shall the software provider be liable for any direct,
indirect, special, incidental, consequential, or punitive damages,
including without limitation, loss of profits, data, or use, arising out
of or in connection with \"PythonUtils\" or the use or performance of
\"PythonUtils\".*

*You agree to use \"PythonUtils\" at your own risk, and you acknowledge
that you have been advised of the potential risks. The software provider
shall not be liable for any damages or losses that may arise from your
use of \"PythonUtils\".*

*By using \"PythonUtils\", you accept this disclaimer in full. If you do
not agree with any part of this disclaimer, do not use \"PythonUtils\".*
