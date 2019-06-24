proto =['ssh', 'http',' https']
print(proto)
print(proto[1])

proto.extend('dns')
print(proto)
proto.extend(['dns'])
print(proto)
proto.append('umar')
print(proto)

proto2=[22, 80, 443, 53]
proto.extend(proto2)
print(proto)
proto.append(proto2)
print(proto)
