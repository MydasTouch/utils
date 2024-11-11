# 放在训练中，一般在system.py文件里

print(f"Allocated memory: {torch.cuda.memory_allocated() / 1024**2:.2f} MB")
print(f"Reserved memory: {torch.cuda.memory_reserved() / 1024**2:.2f} MB")
print(f"Max memory allocated: {torch.cuda.max_memory_allocated() / 1024**2:.2f} MB")
