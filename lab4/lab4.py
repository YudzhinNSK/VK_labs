import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from tol import tolsolvty

A_first = np.array([[3, -5, 2], [7, -4, 1], [5, 7, -4]])
c = [0, 0, 0, 1, 1, 1]
inf_b = np.array([3, 1, -1]).reshape(3,1)
sup_b = np.array([7, 3, 3]).reshape(3,1)
[tolmax, argmax, envs, ccode] = tolsolvty(A_first, A_first, inf_b, sup_b)
print("tolmax = ", tolmax)
print("argmax = ", argmax)
mid_b = np.array([4, 2, 3])
rad_b = np.array([2, 2, 2])

n = 3
neg_diag = -np.diag(rad_b)
r = np.hstack([-mid_b, mid_b])
C = np.block([[-A_first, neg_diag], [A_first, neg_diag]])
print("r = ", r)
print("C = ", C)

#1.6
bounds = ((None, None), (None, None), (None, None), (None, None), (None, None), (None, None))
res = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='interior-point')
print('Interior-method results:')
print('x: (' + str(np.around(res.x[0],decimals=4)) + ',' + str(np.around(res.x[1], decimals=4))
      + ',' + str(np.around(res.x[2], decimals=4)) + ')')
print('w: (' + str(np.around(res.x[3], decimals=4)) + ',' + str(np.around(res.x[4], decimals=4))
      + ',' + str(np.around(res.x[5], decimals=4)) + ')')
print()

#0.6045
bounds = ((None, None), (None, None), (None, None), (None, None), (None, None), (None, None))
res_simpl = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='simplex')
print('Simplex results:')
print('x: (' + str(res_simpl.x[0]) + ',' + str(res_simpl.x[1]) + ',' +
      str(np.around(res_simpl.x[2], decimals=4)) + ')')
print('w: (' + str(res_simpl.x[3]) + ',' + str(np.around(res_simpl.x[4], decimals=4)) + ','
      + str(np.around(res_simpl.x[5], decimals=4)) + ')')

##########################################

points_1 = []
simplex_1 = []
points_2 = []
points_3 = []
simplex_2 = []
simplex_3 = []
points_w = []
simplex_w = []
points_sum_w = []
simplex_sum_w = []
steps = np.arange(0, 2, 0.1)
for i in steps:
    bounds = ((i, i+0.2), (None, None), (None, None), (None, None), (None, None), (None, None))
    res_p = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='interior-point')
    res_s = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='simplex')
    points_1.append(res_p.x[0])
    simplex_1.append(res_s.x[0])
    points_2.append(res_p.x[1])
    simplex_2.append(res_s.x[1])
    points_3.append(res_p.x[2])
    simplex_3.append(res_s.x[2])
    points_w.append(res_p.x[3])
    simplex_w.append(res_s.x[3])
    points_sum_w.append(res_p.x[3]+res_p.x[4]+res_p.x[5])
    simplex_sum_w.append(res_s.x[3]+res_s.x[4]+res_s.x[5])
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(steps, points_2, label='i_2')
plt.plot(steps, points_3, label='i_ 3')
plt.plot(steps, points_w, label='i_w')
plt.plot(steps, points_sum_w, label='i_sum_w')
plt.legend()
plt.title('Change 1coord with interior-point')
plt.savefig('i_1.png', format='png')

plt.subplot(2, 1, 2)
plt.plot(steps, simplex_2, label='s_2')
plt.plot(steps, simplex_3, label='s_3')
plt.plot(steps, simplex_w, label='s_w')
plt.plot(steps, simplex_sum_w, label='s_sum_w')
plt.legend()
plt.title('Change 1coord with simplex')
plt.savefig('s_1.png', format='png')

points_1 = []
simplex_1 = []
points_2 = []
points_3 = []
simplex_2 = []
simplex_3 = []
points_w = []
simplex_w = []
points_sum_w = []
simplex_sum_w = []
for i in steps:
    bounds = ((None, None), (i, i+0.2), (None, None), (None, None), (None, None), (None, None))
    res_p = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='interior-point')
    res_s = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='simplex')
    points_1.append(res_p.x[0])
    simplex_1.append(res_s.x[0])
    points_2.append(res_p.x[1])
    simplex_2.append(res_s.x[1])
    points_3.append(res_p.x[2])
    simplex_3.append(res_s.x[2])
    points_w.append(res_p.x[4])
    simplex_w.append(res_s.x[4])
    points_sum_w.append(res_p.x[3]+res_p.x[4]+res_p.x[5])
    simplex_sum_w.append(res_s.x[3]+res_s.x[4]+res_s.x[5])
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(steps, points_1, label='i_1')
plt.plot(steps, points_3, label='i_3')
plt.plot(steps, points_w, label='i_w')
plt.plot(steps, points_sum_w, label='i_sum_w')
plt.legend()
plt.title('Change 2coord with interior-point')
plt.savefig('i_2.png', format='png')

plt.subplot(2, 1, 2)
plt.plot(steps, simplex_1, label='s_1')
plt.plot(steps, simplex_3, label='s_3')
plt.plot(steps, simplex_w, label='s_w')
plt.plot(steps, simplex_sum_w, label='s_sum_w')
plt.legend()
plt.title('Change 2coord with simplex')
plt.savefig('s_2.png', format='png')


points_1 = []
simplex_1 = []
points_2 = []
points_3 = []
simplex_2 = []
simplex_3 = []
points_w = []
simplex_w = []
points_sum_w = []
simplex_sum_w = []
for i in steps:
    bounds = ((None, None), (None, None), (i, i+0.2), (None, None), (None, None), (None, None))
    res_p = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='interior-point')
    res_s = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='simplex')
    points_1.append(res_p.x[0])
    simplex_1.append(res_s.x[0])
    points_2.append(res_p.x[1])
    simplex_2.append(res_s.x[1])
    points_3.append(res_p.x[2])
    simplex_3.append(res_s.x[2])
    points_w.append(res_p.x[5])
    simplex_w.append(res_s.x[5])
    points_sum_w.append(res_p.x[3]+res_p.x[4]+res_p.x[5])
    simplex_sum_w.append(res_s.x[3]+res_s.x[4]+res_s.x[5])
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(steps, points_1, label='i_1')
plt.plot(steps, points_2, label='i_2')
plt.plot(steps, points_w, label='i_w')
plt.plot(steps, points_sum_w, label='i_sum_w')
plt.legend()
plt.title('Change 3coord with interior-point')
plt.savefig('i_3.png', format='png')

plt.subplot(2, 1, 2)
plt.plot(steps, simplex_1, label='s_1')
plt.plot(steps, simplex_2, label='s_2')
plt.plot(steps, simplex_w, label='s_w')
plt.plot(steps, simplex_sum_w, label='s_sum_w')
plt.legend()
plt.title('Change3coord with simplex')
plt.savefig('s_3.png', format='png')
#plt.show()


##########################################33333

points_3 = []
simplex_3 = []
for i in steps:
    bounds = ((None, None), (i, i+0.2), (None, None), (None, None), (None, None), (None, None))
    res_p = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='interior-point')
    res_s = opt.linprog(c, A_ub=C, b_ub=r, bounds=bounds, method='simplex')
    points_3.append(res_p.x[2])
    simplex_3.append(res_s.x[2])
plt.figure()

plt.plot(steps, points_3, label='Interior-point')
plt.plot(steps, simplex_3, label='Simplex')
plt.legend()
plt.title('Change 2coord with interior-point & simplex')
plt.savefig('i_s.png', format='png')

plt.show()
