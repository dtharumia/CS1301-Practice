# f = open('employees.txt', 'r')

# print(f.name)

# f.close()

# with open('employees2.txt', 'w') as f:
#     # no need for f.close() with context manager
#     # f_contents = f.readline()
#     # print(f_contents)

#     # for line in f:
#     #     print(line, end='')

#     # size_to_read = 10

#     # f_contents = f.read(size_to_read)
#     # print(f_contents,end='%')

#     # f.seek(0)

#     # f_contents = f.read(size_to_read)
#     # print(f_contents)

#     # # while len(f_contents)>0:
#     # #     print(f_contents,end='%')
#     # #     f_contents = f.read(size_to_read)

#     # f.write('test')
#     # f.seek(0)
#     # f.write('F')
#     # when using seek, only writes what's needed aka doesn't overwrite

# with open('employees.txt', 'r') as rf:
#     # for line in rf:
#     #     print(line)
#     with open('employees_copy.txt', 'w') as wf:
#         for line in rf:
# wf.write(line)

# with open('youtube.png', 'rb') as rf:
#     with open('youtube_copy2.png', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
