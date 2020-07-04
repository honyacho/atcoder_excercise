N_INPUTS, @bottles = gets.chomp.split(' ').map &:to_i

arr = (0...N_INPUTS).map do |n|
  gets.chomp.split(' ').map &:to_i
end.sort do |l, r|
  l[0] <=> r[0]
end

@result = 0
arr.each do |pair|
  # p pair
  price, zaiko = pair
  if zaiko > @bottles
    @result += price*@bottles
    @bottles = 0
  else
    @result += zaiko*price
    @bottles -= zaiko
  end
end

puts @result
