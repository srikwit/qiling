#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org)

import struct
import time
from qiling.os.windows.const import *
from qiling.os.const import *
from qiling.os.windows.fncc import *
from qiling.os.windows.utils import *
from qiling.os.windows.thread import *
from qiling.os.windows.handle import *
from qiling.exception import *


# void InitializeSListHead(
#   PSLIST_HEADER ListHead
# );
@winapi(cc=STDCALL, params={
    "ListHead": POINTER
})
def hook_InitializeSListHead(self, address, params):
    addr = params["ListHead"]
    handle = Handle(obj=[], id=addr)
    self.handle_manager.append(handle)
    return 0