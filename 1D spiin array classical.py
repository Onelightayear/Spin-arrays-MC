import random as rnd
from math import exp as exp
from matplotlib import pyplot as plt

def Energy(arr, J):
    E = 0
    for i in range(len(arr)):
        if i == len(arr)-1:
            E += J*0.25*arr[i]*arr[0]
        else:
            E += J*0.25*arr[i]*arr[i+1]
    return E

def S_tot(arr):
    S = 0
    for i in arr:
        S+=0.5*i
    return S

class Spin_chain():
    def __init__(self, Num_spins=18):
        self.Num_spins = Num_spins
        self.Temp = float(input('Temperature:'))
        self.start_state = [rnd.randrange(-1,2,2) for i in range(Num_spins)]
        self.J = float(input('J value:'))
        self.start_E = Energy(self.start_state, self.J)
        self.E_arr = []
        self.S_t = []

    def update(self):
        old_state = self.start_state
        old_E = self.start_E
        counter = 0
        old_S = S_tot(old_state)

        while(counter < 100000):
            spin_change_1 = rnd.randint(0,self.Num_spins-1)

            new_state = old_state
            new_state[spin_change_1] = -1*new_state[spin_change_1]

            new_E = Energy(new_state, self.J)
            new_S = S_tot(new_state)

            #making a state transfer choice
            u = rnd.uniform(0,1)

            if self.Temp == 0:
                if new_E < old_E:
                    k = 0
                else:
                    k=1
            else:
                if new_E > old_E:
                    k = 1
                else:
                    k = exp((new_E-old_E)/self.Temp)
            if u >= k:
                old_E = new_E
                old_S = new_S
                old_state = new_state
                self.S_t.append(old_S)
                # print(old_state)
                self.E_arr.append(old_E)  
            else:
                # print(old_state)
                self.E_arr.append(old_E)
                self.S_t.append(old_S)
            counter +=1

J_pos = Spin_chain()
J_neg = Spin_chain()

J_pos.update()
J_neg.update()

fig, axs = plt.subplots(2,2)
axs[0,0].plot(J_pos.E_arr, label='Energy, J = '+str(J_pos.J))
axs[0,0].legend()
axs[1,0].plot(J_pos.S_t, label='Total spin, J = '+str(J_pos.J), color='orange')
axs[1,0].legend()
axs[0,1].plot(J_neg.E_arr, label='Energy, J = '+str(J_neg.J))
axs[0,1].legend()
axs[1,1].plot(J_neg.S_t, label='Total spin, J = '+str(J_neg.J), color='orange')
axs[1,1].legend()

plt.show()

