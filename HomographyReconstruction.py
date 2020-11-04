import homography 
import sfm 
import sift

# calibration 
k = array ([2394,0,932],[0,2398,628],[0,0,1])

# load images and compute features
im1 = array(Image.open('Building_1.jpg'))
sift.process_image('Building_1.jpg','im1.sift')
l1,d1 = sift.read_features_from_file('im1.sift')

im2 = array(Image.open('Building_1.jpg'))
sift.process_image('Building_2.jpg','im2.sift')
l2,d2 = sift.read_features_from_file('im2.sift')

# match features 
matches = sift.match_twosided(d1,d2)
ndx = matches.nonzero()[0]

# make homogenous and normalize  with inv(k) 
x1 = homography.make_homo(l1[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx] 
x2 = homography.make_homog(l2[ndx2,:2].T)

x1n = dot(inv(k),x1)
x2n = dot(inv(k),x2)

#estunage E with RANSAC
model = sfm.RansacModel()
E,inliers = sfm.F_from_ransac(x1n,x2n,model)

# compute camera matrices (p2 will be list of four solutions) 
P1 = array([1,0,0,0],[0,1,0,0],[0,0,1,0])
P2 = sfm.compute_P_from_essential(E)

