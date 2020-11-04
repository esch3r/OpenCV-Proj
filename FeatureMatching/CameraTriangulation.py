# 3D plotting 
import camera
from mpl_toolkits.mplot3d import axes3d

# Pick the solution with points in front of camera

 ind = 0 
 maxres =0 
  for i in range(4) 
     # triangulat inliers and compute depth for each camera 
        X = sfm.triangulate(x1n[:,inliers],x2n[:,inliers],P1,P2[i])
        d1 = dot(P1,X)[2]
        d2 = dot(P2[i],X)[2]
        if sum(d1>0)+sum(d2>0) > maxres: 
           maxres = sum(d1>0)+sum(d2>0)
           ind = i 
           infront = (d1>0) & (d2>0)
# triangulate inliers and remove points not in front of both cameras 
X = sfm.triangulate(x1n[:,inliers],x2n[:,inliers],P1,P2[ind])
X = X[:,infront]

fig = figure()
ax = fig.gca(projection='3d')
ax.plot(-X[0],X[1],X[2],'k.')
axis('off')

# project 3D points
 cam1 = camera.Camera(P1)
 cam2 = camera.Camera(P2[ind])
 x1p = cam1.project(X)
 x2p = cam2.project(X)
 
 # reverse K normalization 
 x1p = dot(k,x1p)
 x2p = dot(k,x2p)
 
 figure()
 imshow(im1)
 gray()
 plot(x1p[0],x1p[1],'o')
 plot(x2[0],x2[1],'r.')
 axis('off')
 show()
