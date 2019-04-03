REGEX = /(.AGC|A.GC|AG.C|.ACG|.GAC)/
DIVISOR = 10**9 + 7

def calc(n)
  return { "A" => 1, "C" => 1, "G" => 1, "T" => 1 } if n == 1
  res = calc(n-1)
  new_res = {}
  res.each do |k, v|
    "AGCT".each_char do |ch|
      cand = k + ch
      cand.slice!(0, 1) if cand.size > 4
      if cand.size < 4
        if cand != "AGC" && cand != "ACG" && cand != "GAC"
          new_res[cand] = 1
        end
      elsif !REGEX.match(cand)
        new_res[cand] ||= 0
        new_res[cand] += v
      end
    end
  end
  new_res
end

puts (calc gets.to_i).values.inject(&:+) % DIVISOR
