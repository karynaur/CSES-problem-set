import numpy as np
import matplotlib.pyplot as plt


f=open("test_input (1).txt","r")
lines=f.readlines()
data=np.array([list(map(int,e.strip().split())) for e in lines])


t=open("test_output.txt","r")
goal=np.array([list(e.strip())for e in t.readlines()])

goal=np.array([1 if x[0]=='Y' else 0 for x in goal]).reshape(-1,1)

def softmax(x):
  exp_element=np.exp(x-x.max())
  return exp_element/np.sum(exp_element,axis=0)
def d_softmax(x):
  exp_element=np.exp(x-x.max())
  return exp_element/np.sum(exp_element,axis=0)*(1-exp_element/np.sum(exp_element,axis=0))


   
#Initializing weights
def init(x,y):
  layer=np.random.uniform(-1.,1.,size=(x,y))/np.sqrt(x*y)
  return layer.astype(np.float32)

np.random.seed(11)
l1=init(2,8)
l2=init(8,2)

#forward and backward pass
def forward_backward_pass(x,y):
  targets = np.zeros((len(y),2), np.float32)
  targets[range(targets.shape[0]),y] = 1
  x_l1p=x.dot(l1)
  x_softmax=softmax(x_l1p)
  x_l2p=x_softmax.dot(l2)
  out=softmax(x_l2p)
  
  error=2*(out-y)/out.shape[0]*d_softmax(x_l2p)
  update_l2=x_softmax.T@error
    
    
  error=((l2).dot(error.T)).T*d_softmax(x_l1p)
  update_l1=x.T@error

  return out,update_l1,update_l2 

#training
epochs=2
lr=0.1

losses,accuries,val_accuracies=[],[],[]

for i in range(epochs):
    #randomize and create batches
    y=goal 

    out,update_l1,update_l2=forward_backward_pass(data,goal)   
    category=np.argmax(out,axis=1)
    accuracy=(category==y).mean()
    accuries.append(accuracy.item())
    
    loss=((category-y)**2).mean()
    losses.append(loss.item())
    
    #SGD 
    l1=l1-lr*update_l1
    l2=l2-lr*update_l2


    #testing our model using the validation set every 20 epochs
    if i%10==0:print(f'For {i}th epoch: train accuracy: {accuracy:.3f}')


a=np.array([2,1])
print(softmax(softmax(a.dot(l1)).dot(l2)))

