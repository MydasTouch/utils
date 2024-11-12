save_lines_before = 80

with open("train.log", "r") as f:
    lines = f.readlines()

# 用于保存结果的文件
with open("train_log_new.txt", "w") as f:
    # 创建一个集合来存储已经出现过的目标进度条行
    unique_progress = set()
    line_count = 0
    for line in lines:

        # 如果这行包含目标进度条部分，则写入结果文件
      if line_count < save_lines_before or "3475/3475" in line or "750/750" in line:
            # 检查是否已经找到了目标进度条行，如果是，则跳过
            if line not in unique_progress:
                f.write(line)
                # 将这一行添加到集合中
                unique_progress.add(line)
      line_count += 1

# 提示处理完成
print("Unique lines saved to 'train_log_new.txt'")
