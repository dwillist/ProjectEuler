def P( n): # pentagonal
   return (3*n*n-n)/2
def Pn2n( pentagonal): # find `n' using given P(n)
   return int((1 + sqrt( 1 + 24*pentagonal))/6 +0.5)
def ispentagonal( number):
   return P( Pn2n( number)) == number


def isdoubleP( x): # where `x' is P(m)+P(k) or P(m)-P(k)
   q, r = divmod( x, 2)
   return r == 0 and ispentagonal( q)
# main
for m, Pm in enumerate( map( P, count(1))):
   for Pk in imap( P, xrange(1, m+1)):
      if isdoubleP( Pm - Pk) and isdoubleP( Pm + Pk):
         print Pk; sys.exit(0) # 18 seconds
