from PIL import Image, ImageDraw, ImageSequence
import imageio
import os
import sys
import shutil
mazeFilePath = sys.argv[1]
if not os.path.exists(mazeFilePath):
    sys.exit("Sorry, '" + mazeFilePath + "' not found.")
if not os.path.exists("gifdir"):
	os.mkdir("gifdir")

mazeName = mazeFilePath.partition('.')[0]
im = Image.open(mazeFilePath)
im = im.convert("RGB")
os.chdir("gifdir")
pixelMatrix = im.load()
start = (0,0)
end = (0,0)
if mazeName == "large_maze":
    start = (250, 3)
    end = (253, 495)


if mazeName == "maze":
    start = (185, 0)
    end = (395, 380)

if mazeName == "round_maze":
    start = (492,250)
    end = (250, 250)
boundX, boundY = im.size
for j in range(boundY):
	for i in range(boundX):
		r,g,b = pixelMatrix[i,j]
		if r > 150 and g > 150 and b > 150:
			pixelMatrix[i,j] = (255,255,255)




def getAdjacentPixels(pixel):
	x, y = pixel
	top = (x, y-1)
	bottom = (x, y+1)
	left = (x-1, y)
	right = (x+1, y)
	top_left = (x-1, y-1)
	top_right = (x+1, y-1)
	bottom_left = (x-1, y+1)
	bottom_right = (x+1, y+1)
	
	return [top, bottom, left, right, top_left, top_right, bottom_left, bottom_right]
images = []

def getint(name):
	num = name.partition('.')[0]
	return int(num)
def withinBounds(pixel):
	x, y = pixel
	if(x < 0 or x >= boundX or y < 0 or y >= boundY):
		return False
	return True
   
def bfs(start, end):
	Q = [[start]] # list of paths
	visited = set() # set of visited pixels
	counter = 0
	while len(Q) != 0: # while not empty
		currentPath = Q.pop(0) # deque a path
		current = currentPath[-1] # get last element of path
		if current == end: # we have found a solution
			print("maze is solved")
			for pixel in currentPath: # draw path
				draw = ImageDraw.Draw(im)
				draw.point(pixel, fill=(238,48,167))
				for nieghbor in getAdjacentPixels(pixel):
				    if(nieghbor in visited):
				        draw.point(nieghbor, fill=(238,48,167))
			im.show() # show the glory
			im.save(str(counter) + ".jpg")
			imgList = os.listdir(os.getcwd())
			imgList.sort(key=getint)
			for img in imgList:
				print(img)
				images.append(imageio.imread(img))
				if(img == str(counter) + ".jpg"):
					images.append(imageio.imread(img))
					images.append(imageio.imread(img))
					images.append(imageio.imread(img))
					images.append(imageio.imread(img))
					images.append(imageio.imread(img))
			os.chdir("..")
			shutil.rmtree("gifdir")
			imageio.mimsave(mazeName + '.gif', images, fps=15)
			
			return currentPath
		for pixel in getAdjacentPixels(current): # get the pixels(nodes) around current
			x, y = pixel
			if withinBounds(pixel):
				if pixelMatrix[pixel] == (255,255,255) and pixel not in visited:
					visited.add(pixel) # keep track of visited
					pixelMatrix[pixel] = (201,201,255) # color visited
					if counter % 1000 == 0:
						im.save(str(counter) + ".jpg")
					path_branch = list(currentPath) # brach off 
					path_branch.append(pixel)
					Q += [path_branch] # add new branch
		counter = counter + 1		
bfs(start, end)
				
				
				

				
				
				
				
				
				
				



