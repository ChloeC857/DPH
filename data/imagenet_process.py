import os
import shutil
import random

# 完整的 ImageNet 数据集路径
imagenet_path = './images_imagenet'

# 需要提取的 txt 文件路径
txt_path = 'imagenet/train.txt'

# 新的数据集文件夹
new_dataset_path = './imagenet/train_images'
os.makedirs(new_dataset_path, exist_ok=True)

# 获取所有图片文件名
all_images = os.listdir(imagenet_path)

# 读取train.txt中的所有行
with open(txt_path, 'r') as file:
    lines = file.readlines()

# 随机选择 20000 行
selected_lines = random.sample(lines, 20000)

# 处理每一行
for line in selected_lines:
    # 读取train.txt中图像相对路径
    rel_path_in_txt = line.split()[0]
    # 提取文件名
    filename = os.path.basename(rel_path_in_txt)
    # 构建实际的文件路径
    actual_path = os.path.join(imagenet_path, filename)
    # 检查文件是否存在
    if os.path.exists(actual_path):
        # 文件存在，复制到输出目录
        output_path = os.path.join(new_dataset_path, filename)
        shutil.copy(actual_path, output_path)
        print(f"Copied {filename} to {output_path}")
    else:
        # 文件不存在，打印错误消息
        print(f"Image not found: {actual_path}")