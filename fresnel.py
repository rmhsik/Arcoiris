from numpy import *


def coefficients(n1, n2, theta_i):
    theta_t = arcsin(n1 * sin(theta_i) / n2)

    r_p = (n2 * cos(theta_i) - n1 * cos(theta_t)) / \
        (n1 * cos(theta_i) + n2 * cos(theta_t))
    t_p = 2 * n1 * cos(theta_i) / \
        (n2 * cos(theta_i) + n1 * cos(theta_t))
    r_s = (n1 * cos(theta_i) - n2 * cos(theta_t)) / \
        (n1 * cos(theta_i) + n2 * cos(theta_t))
    t_s = 2 * n1 * cos(theta_i) / \
        (n1 * cos(theta_i) + n2 * cos(theta_t))

    cos_t = cos(theta_t)
    cos_i = cos(theta_i)

    R_s = absolute(r_s)**2
    R_p = absolute(r_p)**2
    T_s = absolute(t_s)**2 * (n2 * cos_t) / (n1 * cos_i)
    T_p = absolute(t_p)**2 * (n2 * cos_t) / (n1 * cos_i)

    return {'r_p': r_p, 't_p': t_p, 'r_s': r_s, 't_s': t_s, 'R_p': R_p, 'T_p': T_p, 'R_s': R_s, 'T_s': T_s}
