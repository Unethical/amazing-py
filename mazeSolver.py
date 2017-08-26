from PIL import Image, ImageDraw
from collections import deque

im = Image.open("maze.jpg")
pixelMatrix = im.load()

start = (185, 0)
end = (395, 380)

boundX, boundY = im.size
for j in range(boundY):
	for i in range(boundX):
		r,g,b = pixelMatrix[i,j]
		if r > 150 and g > 150 and b > 150:
			pixelMatrix[i,j] = (255,255,255)




def getAdjacentPixels(pixel):
	x, y = pixel
	top = (x, y+1)
	bottom = (x, y-1)
	left = (x-1, y)
	right = (x+1, y)
	
	return [top, bottom, left, right]
 
def withinBounds(pixel):
	x, y = pixel
	if(x < 0 or x >= boundX or y < 0 or y >= boundY):
		return False
	return True
   
def bfs(start, end):
	Q = [[start]] # list of paths
	visited = set() # set of visited pixels
	while len(Q) != 0: # while not empty
		currentPath = Q.pop(0) # deque a path
		current = currentPath[-1] # get last element of path
		if current == end: # we have found a solution
			print("maze is solved")
			for pixel in currentPath: # draw path
				draw = ImageDraw.Draw(im)
				draw.point(pixel, fill=255)
			im.show() # show the glory
			return currentPath
		for pixel in getAdjacentPixels(current): # get the pixels(nodes) around current
			x, y = pixel
			if withinBounds(pixel):
				if pixelMatrix[pixel] == (255,255,255) and pixel not in visited:
					visited.add(pixel) # keep track of visited
					pixelMatrix[pixel] = (100,100,100) # color visited
					path_branch = list(currentPath) # brach off 
					path_branch.append(pixel)
					Q += [path_branch] # add new branch
				
bfs(start, end)
				
				
				

				
				
				
				
				
				
				



