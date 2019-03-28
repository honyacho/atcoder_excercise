lines = STDIN.each_line

num_stops, num_lines = lines.next.chomp!.split(" ").map(&:to_i)
memo = Array.new(num_stops) { Array.new(num_stops, 10000000) }

(0...num_lines).each do |num|
  i, j, cost = lines.next.chomp!.split(" ").map(&:to_i)
  memo[i-1][j-1] = cost
  memo[j-1][i-1] = cost
end

(0...num_stops).each do |i|
  (0...num_stops).each do |j|
    (0...num_stops).each do |k|
      if j == k
        memo[j][k] = 0
      else
        memo[j][k] = memo[j][k] < (memo[j][i] + memo[i][k]) ? memo[j][k] : (memo[j][i] + memo[i][k])
      end
    end
  end
end

puts memo.map(&:max).min
