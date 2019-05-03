N,C=gets.split(" ").map &:to_i
I=N.times.map{gets.split(" ").map &:to_i}
M,S,r,I[N]=[0],[0],0,[C,0]
(0...N).each{|i|S[i+1]=S[i]+I[i][1];M[i+1]=[S[i+1]-I[i][0],M[i][0]].max,[S[i+1]-2*I[i][0],M[i][1]].max}
(0..N).map{|i|o=S[N]-S[i];r=[r,o+M[i][0]-2*(C-I[i][0]),o+M[i][1]-C+I[i][0]].max}
puts r
