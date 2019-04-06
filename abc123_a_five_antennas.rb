arr = (0...5).map { gets.to_i }
k = gets.to_i

(0...5).each do |i|
  (i...5).each do |j|
    if (arr[i] - arr[j]).abs > k
      puts ":("
      exit(0)
    end
  end
end

puts "Yay!"
