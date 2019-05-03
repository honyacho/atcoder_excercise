gets.to_i.times{a,b=gets.split(' ').map(&:to_i);r=Math.sqrt(a*b).to_i;n=!(r*(r+1)<a*b);p 2*(r-(n ?1:0))-(!((n&&r*r<a*b)||a==b)?1:0)}
