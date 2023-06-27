# bxlogs

**bxlogs** is a minimal Python module for a basic logging setup. It exposes a single function, `get_logger`, which acts
as a wrapper around `logging.getLogger` to set a default output on stderr with a sensible format. That’s all.


## Install

With pip:

    pip install bxlogs

With poetry:

    poetry add bxlogs


## Usage

```python
from bxlogs import get_logger

logger = get_logger("my.module")
logger.info("all set!")
```

The default level is `INFO`.

You can set the level to `DEBUG` using various means:
* `debug=True`
* `level="DEBUG"` or `level=logging.DEBUG`
* Set the environment variable `BX_DEBUG`

```python
from bxlogs import get_logger

# All the calls below are equivalent

logger = get_logger("my.module", debug=True)
logger = get_logger("my.module", level="DEBUG")

import logging
logger = get_logger("my.module", level=logging.DEBUG)

import os
os.environ["BX_DEBUG"] = "1"
logger = get_logger("my.module")
```

You can set any other level using `level=`.

There’s nothing more. If you need anything more complex than that, use the Python `logging` module directly.
