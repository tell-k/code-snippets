$KCODE = "UTF-8"

class String
    def kaibun?
        n = self.size
        h = n / 2 
        h.times do |i|
            return false unless self[i] == self[n-1-i]
            end 
        true
    end 
end
str = "hogegoh"
puts str.kaibun?
