#-*- coding:utf-8 -*-
from PIL import Image

gray=[]
char=[]
ascii_char=list(r'''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^`' ''')
length=len(ascii_char)
with Image.open("123.jpg") as im:
	print(im.format,im.size,im.mode)
	# im.show()
	w,h=im.size
	print(w,h)
	row=h//100
	col=w//100
	print(row,col)
	ratio=length/255/(row*col)
	for i in range(1,h,row):
		temp=[]
		tempchar=[]
		for j in range(1,w,col):
			print(j)
			sumgray=0
			for s_i in range(0,row):
				for s_j in range(0,col):
					try:
						print(i,j,i+s_i,j+s_j)
						r,g,b=im.getpixel((j+s_j,i+s_i))
						sumgray+=int(0.2126*r+0.7152*g+0.0722*b)
					except:
						pass
			temp.append(sumgray//(col*row))
			tempchar.append(ascii_char[int(sumgray*ratio)])
		gray.append(temp)
		char.append(tempchar)
text=''
for i,em1 in enumerate(char):
	for j,em2 in enumerate(em1):
		text+=em2
	text+="\n"
print(text)
with open("charimage.txt",'w') as imtext:
	imtext.write(text)