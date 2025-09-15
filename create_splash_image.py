#!/usr/bin/env python3
"""
创建启动画面图片的脚本
运行此脚本可以生成一个漂亮的启动画面图片
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_splash_image():
    """创建启动画面图片"""
    # 图片尺寸
    width, height = 400, 300
    
    # 创建图片
    img = Image.new('RGBA', (width, height), (45, 45, 45, 255))
    draw = ImageDraw.Draw(img)
    
    # 尝试加载字体
    try:
        # 在Windows上尝试使用系统字体
        title_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 24)
        subtitle_font = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", 14)
    except:
        try:
            # 备用字体
            title_font = ImageFont.truetype("arial.ttf", 24)
            subtitle_font = ImageFont.truetype("arial.ttf", 14)
        except:
            # 使用默认字体
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
    
    # 绘制标题
    title_text = "SEIG 虚空终端"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    title_y = height // 2 - 40
    
    draw.text((title_x, title_y), title_text, fill=(255, 255, 255, 255), font=title_font)
    
    # 绘制版本号
    version_text = "v1.22"
    version_bbox = draw.textbbox((0, 0), version_text, font=subtitle_font)
    version_width = version_bbox[2] - version_bbox[0]
    version_x = (width - version_width) // 2
    version_y = title_y + 35
    
    draw.text((version_x, version_y), version_text, fill=(200, 200, 200, 255), font=subtitle_font)
    
    # 绘制状态文本
    status_text = "正在初始化程序..."
    status_bbox = draw.textbbox((0, 0), status_text, font=subtitle_font)
    status_width = status_bbox[2] - status_bbox[0]
    status_x = (width - status_width) // 2
    status_y = version_y + 35
    
    draw.text((status_x, status_y), status_text, fill=(150, 150, 150, 255), font=subtitle_font)
    
    # 添加装饰性边框
    border_color = (100, 100, 100, 255)
    draw.rectangle([5, 5, width-5, height-5], outline=border_color, width=2)
    
    # 添加一些装饰性元素
    # 左上角装饰
    draw.rectangle([15, 15, 25, 25], outline=(80, 150, 255, 255), width=2)
    draw.rectangle([30, 15, 40, 25], outline=(80, 150, 255, 255), width=2)
    
    # 右下角装饰
    draw.rectangle([width-40, height-25, width-30, height-15], outline=(80, 150, 255, 255), width=2)
    draw.rectangle([width-25, height-25, width-15, height-15], outline=(80, 150, 255, 255), width=2)
    
    # 保存图片
    img.save('splash.png', 'PNG')
    print("启动画面图片已创建: splash.png")

if __name__ == "__main__":
    create_splash_image()
