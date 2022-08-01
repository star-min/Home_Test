# 이미지 파일 다루기
import os
from PIL import Image
from PIL import ImageFilter
print(os.getcwd())
img = Image.open(os.getcwd()+"/data/img1.jpg")
# img.show()
print("이미지 매타 정보 출력")
print(type(img))
print(f'이미지 파일 이름 : {img.filename}')
print(f'이미지 파일 형식 : {img.format}')
print(f'이미지 용량 : {img.size}')
print(f'이미지 색상 모드 : {img.mode}')
print(f'이미지 폭 : {img.width}')
print(f'이미지 높이 : {img.height}')

# 이미지 크기 조절
resize_img = img.resize((720, 1200))
resize_img.save(os.getcwd()+'/data/img1_1.jpg')
#resize_img.show()

# 이미지 오리기
crop_img = img.crop((100,100,500,500))
crop_img.save(os.getcwd()+'/data/img1_2.jpg')
# crop_img.show()

# 이미지 회전 및 뒤집기
# img.rotate(45).show()     # 반시계 방향 45도 회전
# img.transpose(Image.FLIP_LEFT_RIGHT).show()       # 좌우 뒤집기
# img.transpose(Image.FLIP_TOP_BOTTOM).show()       # 살하 뒤집기
# img.transpose(Image.ROTATE_90).show()

# 이미지 필터
# img.show()
# img.filter(ImageFilter.BLUR).show()
# img.filter(ImageFilter.BoxBlur(20)).show()
# img.filter(ImageFilter.GaussianBlur(20)).show()
# img.filter(ImageFilter.EMBOSS).show()
# img.filter(ImageFilter.DETAIL).show()                 # 선명하게
# img.filter(ImageFilter.EDGE_ENHANCE_MORE).show()      # 샤프하게
# img.filter(ImageFilter.EMBOSS).show()

filter_type = [ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE_MORE]
for i in range(len(filter_type)) :
    filter_img = img.filter(filter_type[i])
    filter_img.save(os.getcwd()+'/data/filter_img_{}.jpg'.format(i))

img1 = Image.open(os.getcwd()+'/data/img2.jpg')
img2 = Image.open(os.getcwd()+'/data/img3.jpg')
img3 = Image.open(os.getcwd()+'/data/img4.jpg')

# 이미지 합치기
new_img = Image.new('RGB',(1280,720), 3000000)      # 마지막은 해상도 300이면 300쓰고 0을 4개 추가
new_img.paste(img1, (100, 100))
new_img.paste(img2, (300, 300))
new_img.paste(img3, (500, 500))
new_img.show()