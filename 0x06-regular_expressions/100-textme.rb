#!/usr/bin/env ruby
print ARGV[0].scan(/from:([+a-zA-Z0-9]+)/).join
print ','
print ARGV[0].scan(/to:([+a-zA-Z0-9]+)/).join
print ','
puts ARGV[0].scan(/flags:([\-:+a-zA-Z0-9]+)/).join
