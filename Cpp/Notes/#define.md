# `#define`

The `#define` is part of the preprocessor language for C and C++. When they're used in code, the compiler just replaces the `#define` statement with whatever you want. For example, if you're sick of writing `for (int i = 0; i <= 10; i++)` often, you could be doing the following,

```C++
#include <iostream>

using namespace std;

#define fori10 for (int i = 0; i <= 10; i++)

int main()
{
    fori10 {
        cout << i << endl;
    }

    return 0;
}
```

Will output `1` to `10`.
