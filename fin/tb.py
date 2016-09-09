from fin import *


a = UNIFORM_FIN(10, 5, 0.05, 0.06, 0.0002, 60, 28);

x = 0
tl = 30

test = a.T(x, 'convection');
print "T = %lf" %(test)
test = a.QRate('convection')
print "Q = %lf" %(test)
test = a.getResistance('convection')
print "R = %lf" %(test)

print "\n"
test = a.T(x, 'adiabatic');
print "T = %lf" %(test)
test = a.QRate('adiabatic')
print "Q = %lf" %(test)
test = a.getResistance('adiabatic')
print "R = %lf" %(test)

print "\n"
test = a.T(x, 'constant temperature', tl);
print "T = %lf" %(test)
test = a.QRate('constant temperature', tl)
print "Q = %lf" %(test)
test = a.getResistance('constant temperature')
print "R = %lf" %(test)

print "\n"
test = a.T(x, 'infinite');
print "T = %lf" %(test)
test = a.QRate('infinite')
print "Q = %lf" %(test)
test = a.getResistance('infinite')
print "R = %lf" %(test)
